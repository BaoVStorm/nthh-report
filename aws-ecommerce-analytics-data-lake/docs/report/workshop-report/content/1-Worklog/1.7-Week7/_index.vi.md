---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

## Tuần 7: Curated Data Catalog và validate dữ liệu sau ETL

**Thời gian:** 13/04/2026 - 17/04/2026

### Mục tiêu tuần 7:

* Kiểm tra dữ liệu đầu ra sau khi chạy Glue ETL Job.
* Tạo Glue Data Catalog cho dữ liệu curated.
* Tạo và chạy Glue Crawler cho dữ liệu Parquet trong Curated Zone.
* Query và validate dữ liệu curated bằng Athena.
* Kiểm tra chất lượng dữ liệu sau ETL trước khi tạo dashboard.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---:|---:|---|
| Thứ 2 | - Kiểm tra output sau Glue ETL Job trong S3.<br>- Kiểm tra curated/fact_events, curated/dim_products, curated/fact_transactions.<br>- Kiểm tra error/transactions.<br>- Ghi chú cấu trúc output sau ETL. | 13/04/2026 | 13/04/2026 | [Organizing objects using prefixes - Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html)<br>[Organizing, listing, and working with objects - Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/organizing-objects.html)<br>[Using the Parquet format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html) |
| Thứ 3 | - Tạo Glue Database ecommerce_curated.<br>- Tìm hiểu cách crawler đọc dữ liệu Parquet.<br>- Chuẩn bị cấu hình crawler cho Curated Zone.<br>- Ghi chú vai trò của curated database. | 14/04/2026 | 14/04/2026 | [Using crawlers to populate the Data Catalog - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)<br>[Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)<br>[Using the Parquet format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html)<br>[Create tables using AWS Glue or the Athena console - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/creating-tables-how-to.html) |
| Thứ 4 | - Tạo crawler_ecommerce_curated cho S3 Curated Zone.<br>- Cấu hình S3 path, IAM Role, target database và table prefix.<br>- Chạy crawler và kiểm tra trạng thái.<br>- Chụp màn hình cấu hình crawler. | 15/04/2026 | 15/04/2026 | [Using crawlers to populate the Data Catalog - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)<br>[Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)<br>[Use a crawler to add a table - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/schema-crawlers.html) |
| Thứ 5 | - Kiểm tra các bảng curated_fact_events, curated_dim_products, curated_fact_transactions.<br>- Kiểm tra schema, partition year/month/day và location trong S3.<br>- Query thử các bảng curated bằng Athena.<br>- Ghi chú kết quả crawl curated data. | 16/04/2026 | 16/04/2026 | [Query the AWS Glue Data Catalog - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)<br>[Partition your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)<br>[Managing partitions for ETL output in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-partitions.html) |
| Thứ 6 | - Validate curated data bằng Athena.<br>- Kiểm tra số dòng, null value, refund logic và transaction lỗi.<br>- Kiểm tra dữ liệu âm không hợp lệ đã bị loại khỏi curated layer.<br>- Viết phần Validate Curated Data trong report. | 17/04/2026 | 17/04/2026 | [SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Functions in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/functions.html)<br>[Query the AWS Glue Data Catalog - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html)<br>[Partition your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html) |

### Kết quả đạt được tuần 7:

* Kiểm tra được output sau ETL trong S3.
* Tạo thành công Glue Database ecommerce_curated.
* Tạo và chạy thành công Glue Crawler cho Curated Zone.
* Các bảng curated đã được tạo trong Glue Data Catalog.
* Kiểm tra được schema và partition của các bảng curated.
* Query được dữ liệu Parquet bằng Athena.
* Validate được các điều kiện dữ liệu quan trọng:
  + Không còn null ở các cột quan trọng trong fact_transactions.
  + Transaction có gross_revenue âm nhưng không phải refund đã được loại khỏi curated.
* fact_events và fact_transactions được partition theo year/month/day.
* Xác nhận dữ liệu curated đã đủ điều kiện để xây dựng semantic views và dashboard.
