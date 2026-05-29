---
title: "Worklog Tuần 9"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---

## Worklog Tuần 9: Kết nối QuickSight và xây dựng dashboard đầu tiên

**Thời gian:** 27/04/2026 - 01/05/2026

### Mục tiêu tuần 9:

* Tìm hiểu Amazon QuickSight và các thành phần chính như data source, dataset, analysis và dashboard.
* Kết nối QuickSight với Athena.
* Tạo dataset từ Athena Views.
* Xây dựng dashboard Executive Overview.
* Tạo calculated fields và filter controls theo thời gian.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Tìm hiểu Amazon QuickSight, Data Source, Dataset, Analysis và Dashboard.<br>- Tìm hiểu Direct Query và SPICE.<br>- Kiểm tra region của QuickSight, Athena, Glue và S3.<br>- Chuẩn bị quyền truy cập QuickSight đến Athena/S3. | 27/04/2026 | 27/04/2026 | QuickSight Documentation |
| Thứ 3 | - Cấu hình quyền QuickSight truy cập Athena và S3 bucket.<br>- Tạo Athena data source trong QuickSight.<br>- Validate connection.<br>- Tạo dataset từ view vw_executive_overview. | 28/04/2026 | 28/04/2026 | QuickSight Console |
| Thứ 4 | - Tạo calculated fields cho transaction_year, transaction_quarter và transaction_month.<br>- Tạo filter controls cho Year, Quarter, Month.<br>- Kiểm tra hierarchy filter và show relevant values.<br>- Ghi chú cách tạo filter trong report. | 29/04/2026 | 29/04/2026 | QuickSight |
| Thứ 5 | - Xây dựng Dashboard Executive Overview.<br>- Tạo KPI cards: Total Revenue, Total Orders, Avg Order Value, Refund Rate.<br>- Tạo Revenue Trend, Orders Trend và Refund Rate Trend.<br>- Format số liệu, title, currency và percent. | 30/04/2026 | 30/04/2026 | QuickSight |
| Thứ 6 | - Kiểm tra dashboard Executive Overview với các filter thời gian.<br>- Ghi chú insight của từng visual.<br>- Chụp màn hình dashboard.<br>- Viết phần Dashboard 1 trong report. | 01/05/2026 | 01/05/2026 | QuickSight, Report Draft |

### Kết quả đạt được tuần 9:

* Hiểu được vai trò của QuickSight trong việc trực quan hóa dữ liệu và xây dựng dashboard BI.
* Phân biệt được Direct Query và SPICE ở mức cơ bản.
* Cấp quyền để QuickSight truy cập Athena và S3 bucket.
* Tạo thành công data source Athena trong QuickSight.
* Tạo dataset từ view vw_executive_overview.
* Tạo được các calculated fields:
* transaction_year
* transaction_quarter
* transaction_month
* Tạo được filter controls theo Year, Quarter và Month.
* Xây dựng được Dashboard Executive Overview gồm:
* Total Revenue
* Total Orders
* Average Order Value
* Refund Rate
* Revenue Trend
* Orders Trend
* Refund Rate Trend
* Kiểm tra dashboard hoạt động đúng với các bộ lọc thời gian.
