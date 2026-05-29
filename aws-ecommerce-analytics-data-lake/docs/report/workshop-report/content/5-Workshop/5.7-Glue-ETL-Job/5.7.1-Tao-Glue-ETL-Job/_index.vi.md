---
title: "5.7.1. Tạo Glue ETL Job"
linkTitle: "5.7.1. Tạo Glue ETL Job"
menuTitle: "5.7.1. Tạo Glue ETL Job"
date: 2026-05-29
weight: 571
chapter: false
---

Truy cập **AWS Management Console**, tìm kiếm và chọn dịch vụ **AWS Glue**.

Trong menu bên trái, chọn **ETL jobs**. Sau đó chọn **Script editor**

![](/images/5-Workshop/5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/image-001.png)

#### Tạo Spark script

Trong giao diện tạo job, chọn cấu hình như sau:

- Engine: Chọn **Spark**

- Options: Chọn **Upload script**

Sau đó nhấn **Create script** để tạo Glue Job script.

![](/images/5-Workshop/5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/image-002.png)

Khi script được tạo thành công, chuyển sang tab **Job details** để cấu hình thông tin job.

Tại phần **Basic properties**, cấu hình như sau:

- Name:  **etl_ecommerce_raw_to_curated**

- IAM Role: chọn **AWSGlueServiceRoleDefault**

Role này là IAM Role đã tạo ở bước trước, dùng để cấp quyền cho Glue đọc dữ liệu từ S3 và ghi dữ liệu đầu ra vào S3.

![](/images/5-Workshop/5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/image-003.png)

#### Thêm Job Parameter

Trong phần **Advanced properties** của tab **Job details**, tìm mục **Job parameters**, nhấn **Add new parameter** và thêm tham số sau:

- Key: **--BUCKET_NAME**

- Value: **ecommerce-analytics-datalake-270642943130-ap-southeast-1-an**

![](/images/5-Workshop/5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/image-004.png)

Sau khi cấu hình xong, nhấn **Save** để lưu Glue Job.

Job đã được cập nhật thành công.

![](/images/5-Workshop/5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/image-005.png)

#### Run Glue ETL Job

Sau khi đã cấu hình đầy đủ, nhấn **Run** để bắt đầu chạy Glue ETL Job.

![](/images/5-Workshop/5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/image-006.png)

Glue sẽ thực hiện các bước sau:

- Đọc dữ liệu CSV từ các folder raw/events/, raw/products/, raw/transactions/

- Làm sạch và chuyển đổi kiểu dữ liệu

- Tạo các bảng curated ở định dạng Parquet

- Tách dữ liệu transaction lỗi sang vùng error/transactions/

- Ghi dữ liệu đầu ra vào S3

#### Kiểm tra trạng thái chạy job

Sau khi nhấn Run, chuyển sang tab **Runs** để theo dõi trạng thái chạy job.

Tại đây, kiểm tra các thông tin sau:

- Run status

- Started on

- Duration

- DPU hours

- Error logs, nếu job bị lỗi

Nếu job chạy thành công, trạng thái sẽ hiển thị **Succeeded**.

![](/images/5-Workshop/5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/image-007.png)

Nếu job bị lỗi, chọn vào job run đó để xem chi tiết log và kiểm tra nguyên nhân trong **CloudWatch Logs**.
