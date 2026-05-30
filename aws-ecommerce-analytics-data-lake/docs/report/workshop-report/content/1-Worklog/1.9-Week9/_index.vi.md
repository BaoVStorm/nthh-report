---
title: "Worklog Tuần 9"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---

## Tuần 9: Kết nối QuickSight và xây dựng dashboard đầu tiên

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
| Thứ 2 | - Tìm hiểu Amazon QuickSight, Data Source, Dataset, Analysis và Dashboard.<br>- Tìm hiểu Direct Query và SPICE.<br>- Kiểm tra region của QuickSight, Athena, Glue và S3.<br>- Chuẩn bị quyền truy cập QuickSight đến Athena/S3. | 27/04/2026 | 27/04/2026 | [What is Amazon QuickSight?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)<br>[Data sources in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html)<br>[Creating datasets in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sets.html)<br>[Working with analyses in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-analyses.html)<br>[Publishing dashboards in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/publishing-dashboards.html)<br>[Importing data into SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html) |
| Thứ 3 | - Cấu hình quyền QuickSight truy cập Athena và S3 bucket.<br>- Tạo Athena data source trong QuickSight.<br>- Validate connection.<br>- Tạo dataset từ view vw_executive_overview. | 28/04/2026 | 28/04/2026 | [Authorizing connections to AWS services - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/aws-services-permissions.html)<br>[Creating a dataset using Amazon Athena data](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)<br>[Specify a query result location - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location.html) |
| Thứ 4 | - Tạo calculated fields cho transaction_year, transaction_quarter và transaction_month.<br>- Tạo filter controls cho Year, Quarter, Month.<br>- Kiểm tra hierarchy filter và show relevant values.<br>- Ghi chú cách tạo filter trong report. | 29/04/2026 | 29/04/2026 | [Adding calculated fields - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-calculated-field-analysis.html)<br>[Calculated field function and operator reference - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/calculated-field-reference.html)<br>[extract function - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/extract-function.html)<br>[Adding filters in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/add-a-filter.html)<br>[Adding filter controls to analysis sheets - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html) |
| Thứ 5 | - Xây dựng Dashboard Executive Overview.<br>- Tạo KPI cards: Total Revenue, Total Orders, Avg Order Value, Refund Rate.<br>- Tạo Revenue Trend, Orders Trend và Refund Rate Trend.<br>- Format số liệu, title, currency và percent. | 30/04/2026 | 30/04/2026 | [Visual types in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visual-types.html)<br>[Using KPI charts - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html)<br>[Using line charts - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/line-charts.html)<br>[Using bar charts - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/bar-charts.html)<br>[Formatting visual data labels and values - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/formatting-visuals.html) |
| Thứ 6 | - Kiểm tra dashboard Executive Overview với các filter thời gian.<br>- Ghi chú insight của từng visual.<br>- Chụp màn hình dashboard.<br>- Viết phần Dashboard 1 trong report. | 01/05/2026 | 01/05/2026 | [Working with dashboards in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-dashboards.html)<br>[Publishing dashboards in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/publishing-dashboards.html)<br>[Using filter controls - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html)<br>[Working with visuals in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html) |

### Kết quả đạt được tuần 9:

* Hiểu được vai trò của QuickSight trong việc trực quan hóa dữ liệu và xây dựng dashboard BI.
* Phân biệt được Direct Query và SPICE ở mức cơ bản.
* Cấp quyền để QuickSight truy cập Athena và S3 bucket.
* Tạo thành công data source Athena trong QuickSight.
* Tạo dataset từ view vw_executive_overview.
* Tạo được các calculated fields: transaction_year, transaction_quarter, transaction_month.
* Tạo được filter controls theo Year, Quarter và Month.
* Xây dựng được Dashboard Executive Overview.
* Kiểm tra dashboard hoạt động đúng với các bộ lọc thời gian.
