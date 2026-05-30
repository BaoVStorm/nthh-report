---

title: "Week 8 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
----------------------

## Week 8: Athena Views and Semantic Layer

**Time:** 20/04/2026 - 24/04/2026

### Week 8 Objectives:

* Learn the role of the semantic layer in a data analytics system.
* Create Athena Views for dashboards.
* Write SQL queries to aggregate business-ready data.
* Prepare data for the Executive, Funnel, Marketing, Product, and A/B Testing dashboards.

### Tasks to be carried out this week:

| Day       | Task                                                                                                                                                                                                                                                                                    | Start Date | Completion Date | Reference Material                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monday    | - Learn about the semantic layer and the role of Athena Views.<br>- Identify the dashboards that need to be built.<br>- Create a list of views needed for Executive, Funnel, Marketing, Product, and A/B Testing dashboards.<br>- Prepare SQL templates for the views.                  | 20/04/2026 | 20/04/2026      | [Working with views - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/views.html)<br>[CREATE VIEW - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/create-view.html)<br>[What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)                                                    |
| Tuesday   | - Create the view vw_executive_overview.<br>- Calculate total_orders, total_units_sold, total_revenue, avg_order_value, and refund_rate.<br>- Query and verify the view results.<br>- Take notes on the business meaning of the view.                                                   | 21/04/2026 | 21/04/2026      | [CREATE VIEW - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/create-view.html)<br>[SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Aggregate functions - Trino](https://trino.io/docs/current/functions/aggregate.html)<br>[Conditional expressions - Trino](https://trino.io/docs/current/functions/conditional.html)<br>[Mathematical functions - Trino](https://trino.io/docs/current/functions/math.html)                   |
| Wednesday | - Create the views vw_daily_event_funnel and vw_funnel_summary.<br>- Calculate views, clicks, add_to_carts, purchases, and conversion rates.<br>- Check the funnel logic using Athena.<br>- Take notes on how these views support the Funnel Dashboard.                                 | 22/04/2026 | 22/04/2026      | [CREATE VIEW - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/create-view.html)<br>[SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Aggregate functions - Trino](https://trino.io/docs/current/functions/aggregate.html)<br>[Conditional expressions - Trino](https://trino.io/docs/current/functions/conditional.html)<br>[Conversion functions - Trino](https://trino.io/docs/current/functions/conversion.html)               |
| Thursday  | - Create the views vw_traffic_source_performance and vw_campaign_performance.<br>- Calculate conversion rate, bounce rate, and campaign performance.<br>- Check the results by traffic_source and campaign_id.<br>- Take notes on the Marketing Analytics section.                      | 23/04/2026 | 23/04/2026      | [CREATE VIEW - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/create-view.html)<br>[SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Aggregate functions - Trino](https://trino.io/docs/current/functions/aggregate.html)<br>[Conditional expressions - Trino](https://trino.io/docs/current/functions/conditional.html)<br>[Comparison functions and operators - Trino](https://trino.io/docs/current/functions/comparison.html) |
| Friday    | - Create the views vw_product_revenue and vw_ab_testing_summary.<br>- Join transactions with products to analyze category, brand, and premium product segments.<br>- Calculate A/B Testing metrics by experiment_group.<br>- Summarize the list of created views and update the report. | 24/04/2026 | 24/04/2026      | [CREATE VIEW - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/create-view.html)<br>[SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Join queries - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/joining-tables.html)<br>[Aggregate functions - Trino](https://trino.io/docs/current/functions/aggregate.html)<br>[Conditional expressions - Trino](https://trino.io/docs/current/functions/conditional.html)      |

### Week 8 Achievements:

* Understood why Athena Views are needed instead of letting QuickSight query the curated tables directly.
* Created views for analytics.
* Calculated important metrics such as total revenue, total orders, average order value, refund rate, conversion rate, bounce rate, and funnel rate.
* Checked the results of each view before using them in QuickSight.
* Completed the semantic layer for data visualization.
