---
title: "5.7. Glue ETL Job"
linkTitle: "5.7. Glue ETL Job"
menuTitle: "5.7. Glue ETL Job"
date: 2026-05-29
weight: 570
chapter: false
---

Ở bước này, ta sẽ tạo **AWS Glue ETL Job** để xử lý dữ liệu từ tầng raw sang tầng curated.

Mục tiêu của Glue ETL Job là raw CSV → clean / cast / validate → curated Parquet

Sau khi chạy ETL thành công, dữ liệu sẽ được ghi ra các thư mục sau trong S3:

- **curated/fact_events/**: lưu dữ liệu sự kiện sau khi làm sạch

- **curated/dim_products/**: lưu dữ liệu sản phẩm sau khi chuẩn hóa

- **curated/fact_transactions/**: lưu dữ liệu giao dịch hợp lệ

- **error/transactions/**: lưu các bản ghi giao dịch không hợp lệ

### Logic xử lý ETL

Glue ETL Job sẽ đọc dữ liệu CSV từ S3 Raw Zone, sau đó thực hiện các bước làm sạch, chuyển đổi kiểu dữ liệu, kiểm tra dữ liệu lỗi và ghi kết quả sang S3 Curated Zone dưới định dạng Parquet.

Glue Job đọc dữ liệu từ các đường dẫn:

- raw/events/

- raw/products/

- raw/transactions/

Dữ liệu đầu ra được ghi vào:

- curated/fact_events/

- curated/dim_products/

- curated/fact_transactions/

- error/transactions/

Khi đọc CSV, sử dụng header=true, inferSchema=false và recursiveFileLookup=true giúp Glue đọc tất cả file CSV trong các folder raw tương ứng và chủ động cast kiểu dữ liệu trong bước transform.

#### Xử lý bảng raw_events

- Nguồn dữ liệu đầu vào: **raw/events/**

- Dữ liệu sau xử lý được ghi vào: **curated/fact_events/**

**Các bước xử lý chính:**

- Parse cột event_timestamp sang kiểu timestamp với format yyyy-MM-dd HH:mm:ss.

- Cast các cột event_id, customer_id, session_id, campaign_id sang kiểu Long.

- Trim cột event_type.

- Cast product_id từ dạng số thực/string như "1004.0" sang Long.

- Chuẩn hóa giá trị null hoặc rỗng của device_type thành "unknown".

- Chuẩn hóa traffic_source để xử lý các giá trị viết hoa/thường không nhất quán, ví dụ:

  + ORGANIC → Organic

  + PAID SEARCH → Paid Search

  + SOCIAL → Social

  + EMAIL → Email

  + DIRECT → Direct

- Trim các cột page_category và experiment_group.

- Cast session_duration_sec sang Double.

- Tạo thêm các cột thời gian:

  + event_date

  + event_hour

  + year

  + month

  + day

- Thêm cột ingestion_timestamp để ghi nhận thời điểm xử lý dữ liệu.

- Chọn lại các cột cần thiết theo schema curated.

- Ghi dữ liệu ra định dạng Parquet vào curated/fact_events/

- Partition dữ liệu theo year/month/day.

Bảng **fact_events** sau xử lý được dùng để phân tích hành vi người dùng, funnel, traffic source, device type, campaign và A/B testing.

#### Xử lý bảng raw_products

- Nguồn dữ liệu đầu vào: **raw/products/**

- Dữ liệu sau xử lý được ghi vào: **curated/dim_products/**

**Các bước xử lý chính:**

- Cast product_id sang kiểu Long.

- Trim các cột category và brand.

- Cast base_price sang kiểu Double.

- Parse launch_date sang kiểu date với format yyyy-MM-dd.

- Cast is_premium sang kiểu boolean:

- is_premium = 1 → true

- các giá trị còn lại → false

- Thêm cột ingestion_timestamp để ghi nhận thời điểm xử lý dữ liệu.

- Chọn lại các cột cần thiết theo schema curated.

- Ghi dữ liệu ra định dạng Parquet vào curated/dim_products/.

Bảng này không được partition theo thời gian vì đây là bảng dimension sản phẩm. Bảng **dim_products** được dùng để join với fact_transactions và fact_events thông qua product_id.

#### Xử lý bảng raw_transactions

- Nguồn dữ liệu đầu vào: **raw/transactions/**

- Dữ liệu hợp lệ sau xử lý được ghi vào: **curated/fact_transactions/**

- Dữ liệu lỗi được ghi vào: **error/transactions/**

**Các bước xử lý chính:**

- Parse transaction_timestamp sang kiểu timestamp với format yyyy-MM-dd HH:mm:ss.

- Cast các cột transaction_id, customer_id, product_id, campaign_id sang kiểu Long.

- Cast product_id từ dạng số thực/string như "1004.0" sang Long.

- Cast quantity sang Integer.

- Cast discount_applied và gross_revenue sang Double.

- Cast is_refunded sang boolean:

  + is_refunded = 1 → true

  + Các giá trị còn lại → false

- Tạo thêm các cột thời gian:

  + transaction_date

  + transaction_hour

  + year

  + month

  + day

- Thêm cột ingestion_timestamp để ghi nhận thời điểm xử lý dữ liệu.

- Tách dữ liệu thành 2 nhóm:

  + **valid_transactions**: dữ liệu hợp lệ ghi vào curated/fact_transactions/

  + **invalid_transactions**: dữ liệu lỗi ghi vào error/transactions/

Một transaction được xem là **không hợp lệ** nếu thỏa một trong các điều kiện sau:

- transaction_timestamp parse thất bại hoặc bị null.

- product_id bị null.

- gross_revenue bị null.

- gross_revenue < 0 nhưng is_refunded = false.

Đối với dữ liệu lỗi, thêm cột **error_reason** để mô tả nguyên nhân lỗi:

- INVALID_TRANSACTION_TIMESTAMP

- MISSING_PRODUCT_ID

- MISSING_GROSS_REVENUE

- NEGATIVE_REVENUE_WITHOUT_REFUND_FLAG

Dữ liệu hợp lệ được chọn lại theo schema curated, ghi ra định dạng Parquet vào curated/fact_transactions/ và partition theo year/month/day.
Dữ liệu lỗi được ghi ra định dạng Parquet vào error/transactions/.
