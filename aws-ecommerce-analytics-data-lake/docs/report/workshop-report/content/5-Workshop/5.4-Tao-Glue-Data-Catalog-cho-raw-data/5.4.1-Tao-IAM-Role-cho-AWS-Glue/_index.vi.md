---
title: "5.4.1. Tạo IAM Role cho AWS Glue"
linkTitle: "5.4.1. Tạo IAM Role cho AWS Glue"
menuTitle: "5.4.1. Tạo IAM Role cho AWS Glue"
date: 2026-05-29
weight: 541
chapter: false
---


AWS Glue cần một IAM Role để có quyền truy cập vào Amazon S3 và ghi metadata vào Glue Data Catalog.

#### Truy cập IAM Role

Truy cập **AWS Management Console**, tìm kiếm và chọn dịch vụ **IAM**.

![](/images/5-Workshop/5.4.1-Tao-IAM-Role-cho-AWS-Glue/image-001.png)

Trong menu bên trái, chọn **Roles** -> **Create role**.

![](/images/5-Workshop/5.4.1-Tao-IAM-Role-cho-AWS-Glue/image-002.png)

#### Chọn trusted entity cho role

Tại bước Select trusted entity, cấu hình như sau:

- Trusted entity type: Chọn **AWS service**

- Use case: Chọn **Glue**

Sau đó nhấn **Next**.

![](/images/5-Workshop/5.4.1-Tao-IAM-Role-cho-AWS-Glue/image-003.png)

#### Thêm quyền cho role

Tại bước **Add permissions**, phần **Permissions policies** tìm và chọn policy **AWSGlueServiceRole** và **AmazonS3FullAccess**.

- **AWSGlueServiceRole**: Policy này cho phép AWS Glue thực hiện các tác vụ cơ bản như chạy crawler, ETL job và ghi metadata vào Glue Data Catalog.

- **AmazonS3FullAccess**: cho phép Glue đọc dữ liệu từ S3 Raw Zone và ghi dữ liệu sau xử lý vào S3 Curated Zone, Error Zone và các thư mục liên quan.

![](/images/5-Workshop/5.4.1-Tao-IAM-Role-cho-AWS-Glue/image-004.png)

Trong phạm vi workshop, AmazonS3FullAccess được sử dụng để đơn giản hóa cấu hình quyền. Trong môi trường production, nên thay AmazonS3FullAccess bằng custom least-privilege policy chỉ giới hạn quyền truy cập trong bucket của project.

#### Đặt tên IAM Role

Tại bước **Name, review, and create**, nhập tên role:

  - Role name: **AWSGlueServiceRoleDefault**

![](/images/5-Workshop/5.4.1-Tao-IAM-Role-cho-AWS-Glue/image-005.png)

Kiểm tra lại các thông tin đã cấu hình, sau đó nhấn **Create role**.

![](/images/5-Workshop/5.4.1-Tao-IAM-Role-cho-AWS-Glue/image-006.png)

IAM Role cho AWS Glue đã được tạo thành công.

![](/images/5-Workshop/5.4.1-Tao-IAM-Role-cho-AWS-Glue/image-007.png)
