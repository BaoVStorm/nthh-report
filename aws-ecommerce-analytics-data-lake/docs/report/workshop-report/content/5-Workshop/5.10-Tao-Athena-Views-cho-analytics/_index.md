---
title: "5.10. Create Athena Views for Analytics"
linkTitle: "5.10. Create Athena Views for Analytics"
menuTitle: "5.10. Create Athena Views for Analytics"
date: 2026-05-29
weight: 600
chapter: false
---

After the curated data has been created and crawled into the Glue Data Catalog, the next step is to create **Athena Views** for analytics.

Instead of having QuickSight query directly against the curated tables, we will create business views in Athena. This makes the project more realistic because:

- It separates business logic processing from the dashboard

- It makes QuickSight easier to use

- It reduces the need to rewrite formulas multiple times in the dashboard

- Data fed into the dashboard is already aggregated according to the correct analysis objectives

**The main views to be created include:**

- vw_daily_event_funnel

- vw_traffic_source_performance

- vw_discount_refund_analysis

- vw_ab_testing_summary

- vw_executive_overview

- vw_product_revenue

- vw_campaign_performance

- vw_daily_funnel_by_source_device

- vw_funnel_summary

### 1. View: Daily event funnel

This view is used to analyze the user behavior funnel by day, including the steps: **view → click → add_to_cart → purchase**.

This view helps answer:

- How many views, clicks, add to carts, and purchases are there each day?

- What is the conversion rate between funnel steps?

- Is the daily bounce rate high?

Run the following SQL in Athena:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_daily_event_funnel AS
SELECT
event_date,
COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_click_rate,

ROUND(
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END), 0),
4
) AS click_to_cart_rate,

ROUND(
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_cart_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END), 0),
4
) AS cart_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY event_date;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-001.png)

After creating the view, verify it with the query:

```sql
SELECT * FROM "ecommerce_curated"."vw_daily_event_funnel";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-002.png)

### 2. View: Discount and refund analysis

This view is used to analyze the relationship between discounts and refunds.

This view helps answer:

- Do different discount levels affect the refund rate?

- Which days have high refunds?

- How does total revenue and average revenue change with discount levels?

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_discount_refund_analysis AS
SELECT
transaction_date,
discount_applied,
COUNT(*) AS total_transactions,
SUM(gross_revenue) AS total_revenue,
AVG(gross_revenue) AS avg_revenue,
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) AS refunded_transactions,
ROUND(
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS refund_rate
FROM ecommerce_curated.curated_fact_transactions
GROUP BY
transaction_date,
discount_applied;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-003.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_discount_refund_analysis";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-004.png)

### 3. View: Traffic Source Performance

This view is used to evaluate the effectiveness of each traffic source by day.

This view helps answer:

- Which traffic source generates the most views, clicks, and purchases?

- Do Organic, Paid Search, Social, Email, or Direct have a better conversion rate?

- Which traffic source has a high bounce rate?

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_traffic_source_performance AS
SELECT
event_date,
traffic_source,

COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
traffic_source;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-005.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_traffic_source_performance";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-006.png)

### 4. View: A/B Testing Summary

This view is used to analyze the effectiveness between A/B testing experiment groups.

This view helps answer:

- Which experiment group has a higher conversion rate?

- Which group has a better add-to-cart rate?

- Which group has a lower bounce rate?

- What is the average session duration for each group?

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_ab_testing_summary AS
SELECT
event_date,
experiment_group,
COUNT(*) AS total_events,
SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,
AVG(session_duration_sec) AS avg_session_duration,
ROUND(SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 / NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0), 4) AS conversion_rate,
ROUND(SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 / NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0), 4) AS add_to_cart_rate,
ROUND(SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(*), 0), 4) AS bounce_rate
FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
experiment_group;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-007.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_ab_testing_summary";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-008.png)

### 5. View: Executive Overview

This view is used for the management-level overview dashboard. This is the main view for Dashboard 1 — Executive Overview.

This view helps answer:

- Is revenue increasing or decreasing?

- How is the number of orders changing?

- What is the average order value?

- Is the refund rate increasing abnormally?

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_executive_overview AS
SELECT
transaction_date,
COUNT(*) AS total_orders,
SUM(quantity) AS total_units_sold,
SUM(gross_revenue) AS total_revenue,
AVG(gross_revenue) AS avg_order_value,
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) AS refunded_orders,
ROUND(
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS refund_rate
FROM ecommerce_curated.curated_fact_transactions
GROUP BY transaction_date;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-009.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_executive_overview";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-010.png)

### 6. View: vw_product_revenue

This view is used to analyze revenue by product, category, brand, and premium group.

This view helps answer:

- Which product generates the most revenue?

- Which category sells the best?

- Which brand is the strongest?

- Are premium products effective?

- Which product or category has a high refund rate?

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_product_revenue AS
SELECT
t.transaction_date,
p.product_id,
p.category,
p.brand,
p.is_premium,
COUNT(t.transaction_id) AS total_transactions,
SUM(t.quantity) AS total_units_sold,
SUM(t.gross_revenue) AS total_revenue,
AVG(t.gross_revenue) AS avg_transaction_value,
SUM(CASE WHEN t.is_refunded = true THEN 1 ELSE 0 END) AS refunded_transactions,
ROUND(
SUM(CASE WHEN t.is_refunded = true THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(t.transaction_id), 0), 4) AS refund_rate
FROM ecommerce_curated.curated_fact_transactions t
LEFT JOIN ecommerce_curated.curated_dim_products p
ON t.product_id = p.product_id
GROUP BY
t.transaction_date,
p.product_id,
p.category,
p.brand,
p.is_premium;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-011.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_product_revenue";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-012.png)

### 7. View: Campaign Performance

This view is used to analyze the effectiveness of each campaign by day and traffic source.

This view helps answer:

- Which campaign has the most views, clicks, and purchases?

- Which campaign has a high conversion rate?

- Which campaign has a high bounce rate?

- Which traffic source most effectively supports a campaign?

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_campaign_performance AS
SELECT
event_date,
campaign_id,
traffic_source,

COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS conversion_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
campaign_id,
traffic_source;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-013.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_campaign_performance";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-014.png)

### 8. View: Daily Funnel by Source and Device

This view is used to analyze the funnel by both traffic source and device type.

This view helps answer:

- Does the funnel differ between traffic sources?

- Do mobile, desktop, or tablet have different conversion rates?

- Which traffic source on which device is showing a high bounce rate?

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_daily_funnel_by_source_device AS
SELECT
event_date,
traffic_source,
device_type,

COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_click_rate,

ROUND(
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END), 0),
4
) AS click_to_cart_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END), 0),
4
) AS cart_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS conversion_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
traffic_source,
device_type;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-015.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_daily_funnel_by_source_device";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-016.png)

### 9. View: Funnel Summary

This view is used to create a funnel chart in QuickSight. Data is converted from a multi-column format to a per-stage format for easier visualization.

This view helps display the funnel across the steps **Views → Clicks → Add to Cart → Purchases**.

Run the following SQL:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_funnel_summary AS
SELECT
event_date,
'01 Views' AS funnel_stage,
SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date
UNION ALL
SELECT
event_date,
'02 Clicks' AS funnel_stage,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date
UNION ALL
SELECT
event_date,
'03 Add to Cart' AS funnel_stage,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date
UNION ALL
SELECT
event_date,
'04 Purchases' AS funnel_stage,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-017.png)

Verify the view:

```sql
SELECT * FROM "ecommerce_curated"."vw_funnel_summary";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-018.png)

### Check the list of created views:

After creating all the views, check in Athena or the Glue Data Catalog to ensure the views have appeared in the **ecommerce_curated** database.

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-019.png)

All the necessary views for visualization are now in place.
