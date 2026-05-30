---

title: "Week 9 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
----------------------

## Week 9: Connecting QuickSight and Building the First Dashboard

**Time:** 27/04/2026 - 01/05/2026

### Week 9 Objectives:

* Learn about Amazon QuickSight and its main components, such as data source, dataset, analysis, and dashboard.
* Connect QuickSight to Athena.
* Create datasets from Athena Views.
* Build the Executive Overview dashboard.
* Create calculated fields and time-based filter controls.

### Tasks to be carried out this week:

| Day       | Task                                                                                                                                                                                                                                                                     | Start Date | Completion Date | Reference Material                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monday    | - Learn about Amazon QuickSight, Data Source, Dataset, Analysis, and Dashboard.<br>- Learn about Direct Query and SPICE.<br>- Check the region of QuickSight, Athena, Glue, and S3.<br>- Prepare QuickSight access permissions to Athena/S3.                             | 27/04/2026 | 27/04/2026      | [What is Amazon QuickSight?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)<br>[Data sources in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html)<br>[Creating datasets in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sets.html)<br>[Working with analyses in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-analyses.html)<br>[Publishing dashboards in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/publishing-dashboards.html)<br>[Importing data into SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html) |
| Tuesday   | - Configure QuickSight permissions to access Athena and the S3 bucket.<br>- Create an Athena data source in QuickSight.<br>- Validate the connection.<br>- Create a dataset from the view vw_executive_overview.                                                         | 28/04/2026 | 28/04/2026      | [Authorizing connections to AWS services - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/aws-services-permissions.html)<br>[Creating a dataset using Amazon Athena data](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)<br>[Specify a query result location - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location.html)                                                                                                                                    |
| Wednesday | - Create calculated fields for transaction_year, transaction_quarter, and transaction_month.<br>- Create filter controls for Year, Quarter, and Month.<br>- Check the hierarchy filter and show relevant values.<br>- Take notes on how to create filters in the report. | 29/04/2026 | 29/04/2026      | [Adding calculated fields - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/adding-a-calculated-field-analysis.html)<br>[Calculated field function and operator reference - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/calculated-field-reference.html)<br>[extract function - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/extract-function.html)<br>[Adding filters in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/add-a-filter.html)<br>[Adding filter controls to analysis sheets - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html)                  |
| Thursday  | - Build the Executive Overview Dashboard.<br>- Create KPI cards: Total Revenue, Total Orders, Avg Order Value, and Refund Rate.<br>- Create Revenue Trend, Orders Trend, and Refund Rate Trend visuals.<br>- Format numbers, titles, currency, and percentages.          | 30/04/2026 | 30/04/2026      | [Visual types in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visual-types.html)<br>[Using KPI charts - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html)<br>[Using line charts - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/line-charts.html)<br>[Using bar charts - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/bar-charts.html)<br>[Formatting visual data labels and values - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/formatting-visuals.html)                                                                                                |
| Friday    | - Test the Executive Overview dashboard with time filters.<br>- Take notes on the insights of each visual.<br>- Take screenshots of the dashboard.<br>- Write the Dashboard 1 section in the report.                                                                     | 01/05/2026 | 01/05/2026      | [Working with dashboards in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-dashboards.html)<br>[Publishing dashboards in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/publishing-dashboards.html)<br>[Using filter controls - Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html)<br>[Working with visuals in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html)                                                                                                                                                                                      |

### Week 9 Achievements:

* Understood the role of QuickSight in data visualization and BI dashboard development.
* Distinguished between Direct Query and SPICE at a basic level.
* Granted permissions for QuickSight to access Athena and the S3 bucket.
* Successfully created an Athena data source in QuickSight.
* Created a dataset from the view vw_executive_overview.
* Created calculated fields: transaction_year, transaction_quarter, and transaction_month.
* Created filter controls by Year, Quarter, and Month.
* Built the Executive Overview Dashboard.
* Verified that the dashboard works correctly with time filters.
