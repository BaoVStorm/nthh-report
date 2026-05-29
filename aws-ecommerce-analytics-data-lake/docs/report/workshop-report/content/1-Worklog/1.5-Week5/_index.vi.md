---
title: "Worklog Tuần 5"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

## Worklog Tuần 5: Glue Data Catalog, Glue Crawler và Athena Raw Validation

**Thời gian:** 30/03/2026 - 03/04/2026

### Mục tiêu tuần 5:

* Tìm hiểu AWS Glue Data Catalog và vai trò của metadata.
* Tạo Glue Database cho dữ liệu raw.
* Tạo và chạy Glue Crawler để tự động nhận diện schema dữ liệu trong S3.
* Cấu hình Amazon Athena để query dữ liệu trên S3.
* Thực hiện kiểm tra dữ liệu raw bằng các câu SQL cơ bản.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Tìm hiểu AWS Glue Data Catalog, Glue Database và Glue Table.<br>- Tìm hiểu vai trò metadata trong việc query dữ liệu trên S3.<br>- Tạo Glue Database ecommerce_raw.<br>- Ghi chú khái niệm Data Catalog cho report. | 30/03/2026 | 30/03/2026 | AWS Glue Documentation |
| Thứ 3 | - Tìm hiểu Glue Crawler và cách crawler nhận diện schema.<br>- Tạo crawler_ecommerce_raw cho S3 Raw Zone.<br>- Cấu hình S3 data source, IAM Role, target database và table prefix.<br>- Chụp màn hình cấu hình crawler. | 31/03/2026 | 31/03/2026 | AWS Glue Console |
| Thứ 4 | - Chạy Raw Crawler.<br>- Kiểm tra trạng thái crawler sau khi chạy.<br>- Kiểm tra các bảng raw_events, raw_products, raw_transactions trong Glue Catalog.<br>- Kiểm tra schema từng bảng và ghi chú kết quả. | 01/04/2026 | 01/04/2026 | AWS Glue Console |
| Thứ 5 | - Cấu hình Athena query result location trong S3.<br>- Query thử các bảng raw bằng SELECT LIMIT.<br>- Kiểm tra dữ liệu hiển thị, tên cột, kiểu dữ liệu và lỗi header.<br>- Chụp màn hình kết quả query. | 02/04/2026 | 02/04/2026 | Amazon Athena |
| Thứ 6 | - Viết SQL validation cho raw data.<br>- Kiểm tra event_type, category, quantity, null value và abnormal value.<br>- Tổng hợp kết quả raw validation.<br>- Viết phần Glue Crawler và Athena Raw Validation vào report. | 03/04/2026 | 03/04/2026 | Amazon Athena |

### Kết quả đạt được tuần 5:

* Hiểu được Glue Data Catalog là nơi lưu metadata để Athena có thể truy vấn dữ liệu trong S3.
* Tạo thành công Glue Database cho raw data.
* Tạo và chạy thành công Glue Crawler cho S3 Raw Zone.
* Các bảng raw đã được tạo trong Glue Data Catalog, bao gồm:
* raw_events
* raw_products
* raw_transactions
* Cấu hình thành công Athena query result location trong S3.
* Query thử dữ liệu raw bằng Athena và xác nhận dữ liệu có thể được đọc từ S3 thông qua Glue Catalog.
* Viết được các câu SQL kiểm tra dữ liệu ban đầu như:
* Đếm số lượng event theo event_type.
* Đếm số lượng sản phẩm theo category.
* Kiểm tra phân bố quantity trong transactions.
* Kiểm tra null value và các giá trị bất thường.
* Hoàn thành phần nền tảng để chuyển sang bước xây dựng ETL pipeline.
