---
title: "5.8.2. Tạo Glue Crawler cho dữ liệu Curated Parquet"
linkTitle: "5.8.2. Tạo Glue Crawler cho dữ liệu Curated Parquet"
menuTitle: "5.8.2. Tạo Glue Crawler cho dữ liệu Curated Parquet"
date: 2026-05-29
weight: 582
chapter: false
---

Sau khi tạo database, tiếp tục tạo Glue Crawler để quét dữ liệu Parquet trong folder **curated/**.

- Trong **AWS Glue**, chọn **Data Catalog** → **Crawlers**.

- Sau đó nhấn **Create crawler**.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-001.png)

#### Cấu hình thông tin crawler

Tại màn hình **Set crawler properties**, nhập:

- Name: **crawler_ecommerce_curated**

Sau đó nhấn **Next**.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-002.png)

#### Thêm data source cho crawler

Tại bước chọn data source, nhấn **Add a data source**.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-003.png)

Trong giao diện **Add a data source**, cấu hình như sau:

- Data source: Chọn **S3**

- Điền S3 path: **s3://ecommerce-analytics-datalake-270642943130-ap-southeast-1-an/curated/**

Sau khi chọn đúng S3 path nhấn **Add an S3 data source**.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-004.png)

Data source đã được thêm vào crawler. Nhấn **Next** để tiếp tục.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-005.png)

#### Chọn IAM Role cho crawle

Tại màn hình **Configure security settings**, chọn IAM Role đã tạo cho AWS Glue **AWSGlueServiceRoleDefault**.

Sau đó nhấn **Next**.

IAM Role này cho phép Glue Crawler đọc dữ liệu trong S3 và ghi metadata vào Glue Data Catalog.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-006.png)

#### Cấu hình output cho crawler

- Tại màn hình **Set output and scheduling**, cấu hình như sau:

- Target database: **ecommerce_curated**

- Table name prefix: **curated_**

- Crawl schedule: **On demand**

Ở bước này, chọn On demand vì crawler sẽ được chạy thủ công. Sau này có thể đưa crawler vào Glue Workflow hoặc schedule tự động bằng EventBridge.

Sau khi cấu hình xong, nhấn **Next**.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-007.png)

#### Review và tạo crawler

Tại màn hình **Review and create**, kiểm tra lại các thông tin sau:

- Name: **crawler_ecommerce_curated**

- Data source: folder **curated/** trong S3

- IAM Role: **AWSGlueServiceRoleDefault**

- Target database: **ecommerce_curated**

- Table name prefix: **curated_**

- Schedule: **On demand**

Nếu thông tin đã chính xác, nhấn **Create crawler**.

![](/images/5-Workshop/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/image-008.png)

Crawler **crawler_ecommerce_curated** đã được tạo thành công.
