---
title: "Worklog Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

## Worklog Tuần 2: IAM, S3, EC2, VPC và CloudWatch cơ bản

**Thời gian:** 09/03/2026 - 13/03/2026

### Mục tiêu tuần 2:

* Tìm hiểu các service nền tảng quan trọng của AWS.
* Nắm được IAM để hiểu cách AWS quản lý quyền truy cập.
* Tìm hiểu Amazon S3 để chuẩn bị cho việc xây dựng data lake.
* Học các kiến thức cơ bản về EC2, VPC và CloudWatch.
* Làm quen với AWS CLI và cách quản lý tài nguyên AWS ngoài giao diện Console.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Tìm hiểu AWS IAM: User, Group, Role, Policy, Permission.<br>- Phân biệt permission policy và trust policy.<br>- Thực hành xem cấu trúc policy JSON cơ bản.<br>- Ghi chú vai trò của IAM trong các service như Glue, EventBridge và QuickSight. | 09/03/2026 | 09/03/2026 | AWS IAM Documentation |
| Thứ 3 | - Tìm hiểu Amazon S3: bucket, object, prefix/folder, S3 URI.<br>- Thực hành tạo bucket thử nghiệm, upload file và tạo folder.<br>- Tìm hiểu bucket policy, public access block và storage class.<br>- Ghi chú cách S3 được dùng làm data lake trong workshop. | 10/03/2026 | 10/03/2026 | AWS S3 Documentation |
| Thứ 4 | - Tìm hiểu Amazon EC2: instance, AMI, instance type, key pair, EBS.<br>- Tìm hiểu security group và cách SSH vào EC2.<br>- Thực hành tạo EC2 instance ở mức cơ bản nếu cần.<br>- Ghi chú vai trò của compute service trong AWS. | 11/03/2026 | 11/03/2026 | AWS EC2 Documentation |
| Thứ 5 | - Tìm hiểu Amazon VPC: VPC, subnet, route table, Internet Gateway, NAT Gateway.<br>- Tìm hiểu security group và network ACL ở mức cơ bản.<br>- Xem mô hình network cơ bản trên AWS.<br>- Ghi chú các khái niệm network cần biết cho người mới học AWS. | 12/03/2026 | 12/03/2026 | AWS VPC Documentation |
| Thứ 6 | - Tìm hiểu Amazon CloudWatch Logs, metric, log group và log stream.<br>- Tìm hiểu CloudTrail ở mức cơ bản để theo dõi lịch sử thao tác tài khoản.<br>- Tổng hợp kiến thức nền tảng AWS tuần 2.<br>- Viết phần kết quả đạt được và chuẩn bị chuyển sang nhóm Data Analytics. | 13/03/2026 | 13/03/2026 | CloudWatch Documentation |

### Kết quả đạt được tuần 2:

* Hiểu được vai trò của IAM trong việc quản lý người dùng, role, policy và permission.
* Phân biệt được IAM User, IAM Role, IAM Policy, Permission Policy và Trust Policy.
* Nắm được cách Amazon S3 lưu trữ dữ liệu bằng bucket, object và prefix/folder.
* Hiểu cơ bản về EC2, AMI, instance type, key pair, EBS và security group.
* Hiểu được các thành phần mạng cơ bản trong VPC như subnet, route table, Internet Gateway và security group.
* Biết vai trò của CloudWatch trong việc theo dõi log, metric và hỗ trợ debug lỗi.
* Có kiến thức nền tảng để tiếp tục học các service phục vụ Data Engineering như Glue, Athena và QuickSight.
