---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

## Worklog Tuần 7: Curated Data Catalog và validate dữ liệu sau ETL

**Thời gian:** 13/04/2026 - 17/04/2026

### Mục tiêu tuần 7:

* Kiểm tra dữ liệu đầu ra sau khi chạy Glue ETL Job.
* Tạo Glue Data Catalog cho dữ liệu curated.
* Tạo và chạy Glue Crawler cho dữ liệu Parquet trong Curated Zone.
* Query và validate dữ liệu curated bằng Athena.
* Kiểm tra chất lượng dữ liệu sau ETL trước khi tạo dashboard.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Kiểm tra output sau Glue ETL Job trong S3.<br>- Kiểm tra curated/fact_events, curated/dim_products, curated/fact_transactions.<br>- Kiểm tra error/transactions.<br>- Ghi chú cấu trúc output sau ETL. | 13/04/2026 | 13/04/2026 | AWS S3 Console |
| Thứ 3 | - Tạo Glue Database ecommerce_curated.<br>- Tìm hiểu cách crawler đọc dữ liệu Parquet.<br>- Chuẩn bị cấu hình crawler cho Curated Zone.<br>- Ghi chú vai trò của curated database. | 14/04/2026 | 14/04/2026 | AWS Glue Console |
| Thứ 4 | - Tạo crawler_ecommerce_curated cho S3 Curated Zone.<br>- Cấu hình S3 path, IAM Role, target database và table prefix.<br>- Chạy crawler và kiểm tra trạng thái.<br>- Chụp màn hình cấu hình crawler. | 15/04/2026 | 15/04/2026 | AWS Glue Crawler Documentation |
| Thứ 5 | - Kiểm tra các bảng curated_fact_events, curated_dim_products, curated_fact_transactions.<br>- Kiểm tra schema, partition year/month/day và location trong S3.<br>- Query thử các bảng curated bằng Athena.<br>- Ghi chú kết quả crawl curated data. | 16/04/2026 | 16/04/2026 | AWS Glue, Athena |
| Thứ 6 | - Validate curated data bằng Athena.<br>- Kiểm tra số dòng, null value, refund logic và transaction lỗi.<br>- Kiểm tra dữ liệu âm không hợp lệ đã bị loại khỏi curated layer.<br>- Viết phần Validate Curated Data trong report. | 17/04/2026 | 17/04/2026 | Amazon Athena |

### Kết quả đạt được tuần 7:

* Kiểm tra được output sau ETL trong S3, bao gồm:
* curated/fact_events/
* curated/dim_products/
* curated/fact_transactions/
* error/transactions/
* Tạo thành công Glue Database ecommerce_curated.
* Tạo và chạy thành công Glue Crawler cho Curated Zone.
* Các bảng curated đã được tạo trong Glue Data Catalog, bao gồm:
* curated_fact_events
* curated_dim_products
* curated_fact_transactions
* Kiểm tra được schema và partition của các bảng curated.
* Query được dữ liệu Parquet bằng Athena.
* Validate được các điều kiện dữ liệu quan trọng:
* Không còn null ở các cột quan trọng trong fact_transactions.
* Transaction có gross_revenue âm nhưng không phải refund đã được loại khỏi curated.
* fact_events và fact_transactions được partition theo year/month/day.
* Xác nhận dữ liệu curated đã đủ điều kiện để xây dựng semantic views và dashboard.
