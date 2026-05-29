---
title: "5.11. Kết nối QuickSight với Athena"
linkTitle: "5.11. Kết nối QuickSight với Athena"
menuTitle: "5.11. Kết nối QuickSight với Athena"
date: 2026-05-29
weight: 610
chapter: false
---

Sau khi tạo xong các Athena Views, tiếp theo ta sẽ kết nối **Amazon QuickSight** với **Athena** để tạo dataset và xây dựng dashboard.

QuickSight sẽ lấy dữ liệu từ database **ecommerce_curated** và sử dụng các view đã tạo ở bước trước làm dataset chính.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-001.png)

Tiếp theo ta chọn **Sign up for Amazon Quick**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-002.png)

### Kiểm tra Region của QuickSight

Trước khi kết nối QuickSight với Athena, cần kiểm tra **Region** đang sử dụng.

{{% notice note %}}
QuickSight, Athena, Glue Data Catalog và S3 bucket nên được cấu hình trong cùng một Region để tránh lỗi truy cập dữ liệu.
{{% /notice %}}

Trong workshop này, S3 bucket và Athena đang ở Region **ap-southeast-1** nên QuickSight cũng phải được chuyển sang cùng Region này.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-003.png)

### Cấu hình quyền truy cập trong QuickSight

Trong QuickSight, vào phần **Manage Account**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-004.png)

Sau đó nhấn vào **AWS resouces** kiểm tra phần quyền truy cập đến các dịch vụ AWS.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-005.png)

Chọn service **S3 bucket** để thêm bucket của project vào danh sách bucket được QuickSight phép truy cập.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-006.png)

Trong phần chọn S3 bucket, chọn bucket của project, tick **Write permission for Athena Workgroup**.

Sau đó nhấn **Finish**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-007.png)

Cần đảm bảo QuickSight có quyền truy cập:

- Amazon Athena

- Amazon S3 bucket chứa dữ liệu project

- Glue Data Catalog thông qua Athena

Sau đó nhấn **Next**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-008.png)

### Tạo dataset từ Athena

Trong giao diện QuickSight, chọn **Datasets** → **Create dataset**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-009.png)

Trong màn hình Create dataset, nhấn **Create data source**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-010.png)

Chọn data source **Amazon Athena**.

Sau đó nhấn **Next**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-011.png)

Tại màn hình tạo **Athena data source**, nhập:

- Data source name: **ecommerce_curated**

Nhấn **Validate connection** để kiểm tra kết nối.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-012.png)

Nếu kết nối thành công, QuickSight sẽ hiển thị thông báo SSL đã được bật hoặc kết nối hợp lệ.

Sau đó nhấn **Create data source**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-013.png)

### Chọn database và view

Sau khi tạo data source, QuickSight sẽ hiển thị danh sách database và table/view từ Athena.

Cấu hình như sau:

- Database: **ecommerce_curated**

- Table/View: **vw_executive_overview**

Sau khi chọn view, nhấn **Select**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-014.png)

### Hoàn tất tạo dataset

Tại bước **Finish dataset creation** chọn **Directly query your data**, sau đó nhấn **Visualize**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-015.png)

Lý do chọn **Directly query your data**:

- Dữ liệu trong Athena đã được xử lý ở curated layer

- Dataset dễ cập nhật khi dữ liệu thay đổi

Sau khi nhấn Visualize, QuickSight sẽ mở giao diện tạo analysis/dashboard.

Nhấn **Create** để tạo dashboard.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-016.png)
