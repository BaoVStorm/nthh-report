---
title: "Worklog Tuần 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

## Tuần 4: Xây dựng S3 Data Lake và chuẩn bị dữ liệu raw

**Thời gian:** 23/03/2026 - 27/03/2026

### Mục tiêu tuần 4:

* Thiết kế cấu trúc S3 Data Lake cho project.
* Tạo S3 bucket và tổ chức các thư mục dữ liệu theo từng zone.
* Thực hiện preprocessing dữ liệu ở local.
* Upload dữ liệu raw lên Amazon S3.
* Tạo IAM Role cần thiết để AWS Glue có thể truy cập dữ liệu trong S3.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Tìm hiểu thiết kế S3 Data Lake.<br>- Lên cấu trúc thư mục raw, curated, error và athena-results.<br>- Xác định quy ước đặt tên bucket và prefix.<br>- Ghi chú vai trò của từng zone trong data lake. | 23/03/2026 | 23/03/2026 |  |
| Thứ 3 | - Tạo S3 bucket cho project.<br>- Tạo folder raw/events, raw/products, raw/transactions.<br>- Tạo folder curated, error và athena-results.<br>- Chụp màn hình cấu trúc bucket để đưa vào report. | 24/03/2026 | 24/03/2026 |  |
| Thứ 4 | - Thực hiện preprocessing local cho dataset.<br>- Đổi tên timestamp thành event_timestamp và transaction_timestamp.<br>- Kiểm tra header, encoding, số dòng và định dạng dữ liệu.<br>- Ghi chú các bước preprocessing local trong report. | 25/03/2026 | 25/03/2026 |  |
| Thứ 5 | - Upload events.csv, products.csv và transactions.csv lên đúng S3 prefix.<br>- Kiểm tra file sau upload trong từng folder.<br>- Kiểm tra đường dẫn S3 URI của từng dataset.<br>- Chụp màn hình minh họa quá trình upload dữ liệu. | 26/03/2026 | 26/03/2026 |  |
| Thứ 6 | - Tạo IAM Role cho AWS Glue.<br>- Tìm hiểu quyền cần thiết để Glue truy cập S3 và Data Catalog.<br>- Attach policy phù hợp cho môi trường workshop.<br>- Ghi chú lưu ý về least privilege cho môi trường production. | 27/03/2026 | 27/03/2026 | [Setting up IAM permissions for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/set-up-iam.html)<br>[Step 2: Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html)<br>[How AWS Glue works with IAM](https://docs.aws.amazon.com/glue/latest/dg/security_iam_service-with-iam.html) |

### Kết quả đạt được tuần 4:

* Tạo thành công S3 bucket phục vụ project workshop.
* Thiết kế được cấu trúc data lake gồm:
  + raw/
  + curated/
  + error/
  + athena-results/
* Tổ chức dữ liệu raw theo từng domain:
  + raw/events/
  + raw/products/
  + raw/transactions/
* Thực hiện preprocessing local cho dữ liệu, bao gồm đổi tên cột timestamp để dễ xử lý trong ETL.
* Upload thành công các file CSV lên đúng thư mục trong S3 Raw Zone.
* Tạo được IAM Role cho AWS Glue với quyền truy cập S3 và Glue Data Catalog.
* Hiểu được vai trò của S3 trong việc đóng vai trò là data lake trung tâm của toàn bộ pipeline.
