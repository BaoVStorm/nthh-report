---
title: "5.8.3. Chạy Glue Crawler"
linkTitle: "5.8.3. Chạy Glue Crawler"
menuTitle: "5.8.3. Chạy Glue Crawler"
date: 2026-05-29
weight: 583
chapter: false
---

Sau khi tạo crawler thành công, chọn crawler **crawler_ecommerce_curated**.

Nhấn **Run crawler** để bắt đầu crawl dữ liệu Parquet trong folder **curated/**.

Crawler sẽ quét các folder con trong curated/, tự động nhận diện schema và tạo metadata table trong Glue Data Catalog.

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-006.png)

Sau khi crawler chạy thành công, trạng thái crawler sẽ hiển thị hoàn tất. Craw thành công data vào bảng **ecommerce_curated**.

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-007.png)

#### Kiểm tra các bảng trong Glue Data Catalog

Sau khi crawler chạy xong, vào **AWS Glue** → **Data Catalog** → **Tables**.

Trong database **ecommerce_curated**, kiểm tra các bảng đã được tạo.

Các bảng bao gồm:

- curated_fact_events

- curated_dim_products

- curated_fact_transactions

Chọn từng bảng để kiểm tra schema.

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-008.png)

#### Kiểm tra bảng curated_fact_events

Mở bảng **curated_fact_events**. Sau đó kiểm tra các thông tin chính:

- Dữ liệu nằm trong folder curated/fact_events/

- Định dạng dữ liệu là Parquet

- Có các cột thời gian như event_date, event_hour, year, month, day

- Có cột ingestion_timestamp

- Bảng được partition theo year, month, day

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-009.png)

#### Kiểm tra bảng curated_dim_products

Mở bảng **curated_dim_products**. Sau đó kiểm tra các thông tin chính:

- Dữ liệu nằm trong folder curated/dim_products/

- Định dạng dữ liệu là Parquet

- Có các cột như product_id, category, brand, base_price, launch_date, is_premium

- Cột is_premium đã được chuyển sang kiểu boolean

- Có cột ingestion_timestamp

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-010.png)

#### Kiểm tra bảng curated_fact_transactions

Mở bảng **curated_fact_transactions**. Sau đó kiểm tra các thông tin chính:

- Dữ liệu nằm trong folder curated/fact_transactions/

- Định dạng dữ liệu là Parquet

- Có các cột thời gian như transaction_date, transaction_hour, year, month, day

- Có cột ingestion_timestamp

- Bảng được partition theo year, month, day

- Chỉ chứa các transaction hợp lệ sau bước validate trong Glue ETL Job

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-011.png)
