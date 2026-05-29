---
title: "Worklog Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

## Tuần 2: IAM, S3, EC2, VPC và CloudWatch cơ bản

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
| Thứ 2 | - Tìm hiểu AWS IAM: User, Group, Role, Policy, Permission.<br>- Phân biệt permission policy và trust policy.<br>- Thực hành xem cấu trúc policy JSON cơ bản.<br>- Ghi chú vai trò của IAM trong các service như Glue, EventBridge và QuickSight. | 09/03/2026 | 09/03/2026 | [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)<br>[What is AWS Identity and Access Management?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)<br>[IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)<br>[IAM Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)<br>[IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)<br>[IAM Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)<br>[IAM Policy JSON Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) |
| Thứ 3 | - Tìm hiểu Amazon S3: bucket, object, prefix/folder, S3 URI.<br>- Thực hành tạo bucket thử nghiệm, upload file và tạo folder.<br>- Tìm hiểu bucket policy, public access block và storage class.<br>- Ghi chú cách S3 được dùng làm data lake trong workshop. | 10/03/2026 | 10/03/2026 | [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)<br>[What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)<br>[Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)<br>[Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html)<br>[Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html)<br>[Bucket policies for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)<br>[Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)<br>[Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) |
| Thứ 4 | - Tìm hiểu Amazon EC2: instance, AMI, instance type, key pair, EBS.<br>- Tìm hiểu security group và cách SSH vào EC2.<br>- Thực hành tạo EC2 instance ở mức cơ bản nếu cần.<br>- Ghi chú vai trò của compute service trong AWS. | 11/03/2026 | 11/03/2026 | [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/)<br>[What is Amazon EC2?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>[Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)<br>[Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)<br>[Amazon EBS volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)<br>[Amazon EC2 key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)<br>[Amazon EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>[Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) |
| Thứ 5 | - Tìm hiểu Amazon VPC: VPC, subnet, route table, Internet Gateway, NAT Gateway.<br>- Tìm hiểu security group và network ACL ở mức cơ bản.<br>- Xem mô hình network cơ bản trên AWS.<br>- Ghi chú các khái niệm network cần biết cho người mới học AWS. | 12/03/2026 | 12/03/2026 | [Amazon VPC Documentation](https://docs.aws.amazon.com/vpc/)<br>[What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)<br>[VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html)<br>[Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)<br>[Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)<br>[NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)<br>[Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)<br>[Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| Thứ 6 | - Tìm hiểu Amazon CloudWatch Logs, metric, log group và log stream.<br>- Tìm hiểu CloudTrail ở mức cơ bản để theo dõi lịch sử thao tác tài khoản.<br>- Tổng hợp kiến thức nền tảng AWS tuần 2.<br>- Viết phần kết quả đạt được và chuẩn bị chuyển sang nhóm Data Analytics. | 13/03/2026 | 13/03/2026 | [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)<br>[What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br>[What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br>[Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)<br>[Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)<br>[AWS CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)<br>[What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)<br>[Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) |

### Kết quả đạt được tuần 2:

* Hiểu được vai trò của IAM trong việc quản lý người dùng, role, policy và permission.
* Phân biệt được IAM User, IAM Role, IAM Policy, Permission Policy và Trust Policy.
* Nắm được cách Amazon S3 lưu trữ dữ liệu bằng bucket, object và prefix/folder.
* Hiểu cơ bản về EC2, AMI, instance type, key pair, EBS và security group.
* Hiểu được các thành phần mạng cơ bản trong VPC như subnet, route table, Internet Gateway và security group.
* Biết vai trò của CloudWatch trong việc theo dõi log, metric và hỗ trợ debug lỗi.
* Có kiến thức nền tảng để tiếp tục học các service phục vụ Data Engineering như Glue, Athena và QuickSight.
