---
title: "5.9. Validate curated data"
linkTitle: "5.9. Validate curated data"
menuTitle: "5.9. Validate curated data"
date: 2026-05-29
weight: 590
chapter: false
---

Before building dashboards on QuickSight, it is necessary to validate the data in the curated tier to ensure it has been processed correctly.

**The goal of the validation step is:**

- Check the row count of each table

- Check categorical data such as event_type, category

- Check revenue and refund data

- Ensure the curated data can be used for analysis and dashboards

### Check row counts per table

Row counts:

- events = 2,000,000

- products = 2,000

- transactions <= 103,127 (transactions is less than 103,127 because the Glue ETL has moved error records to error/transactions/).

### Check event type

Run the following query to check the number of records by each event type:

```sql
SELECT
event_type,
COUNT(*) AS event_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_type
ORDER BY event_count DESC;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-001.png)

The query result helps verify:

- What event types are present in the data

- Whether the count for each event type is reasonable

- Whether there are abnormal values such as null, empty, or incorrect format

### Check product category

Run the following query to check the number of products by each category:

```sql
SELECT
category,
COUNT(*) AS product_count
FROM ecommerce_curated.curated_dim_products
GROUP BY category
ORDER BY product_count DESC;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-002.png)

The query result helps verify:

- The product category groups

- The number of products in each category

### Check negative revenue and refunds

Run the following query to check total revenue by refund status:
```sql
SELECT
is_refunded,
COUNT(*) AS transaction_count,
SUM(gross_revenue) AS total_revenue
FROM ecommerce_curated.curated_fact_transactions
GROUP BY is_refunded;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-003.png)

This query helps verify the transaction processing logic after ETL.

**Results:**

- Transactions with is_refunded = true may have negative gross_revenue

- Transactions with is_refunded = false do not have negative gross_revenue

- Records with gross_revenue < 0 but is_refunded = false have been moved to error/transactions/

### Check invalid negative transactions

To ensure that transactions with negative revenue that are not refunds have been excluded from the curated layer, run the query:

```sql
SELECT
    COUNT(*) AS invalid_negative_revenue_count
FROM ecommerce_curated.curated_fact_transactions
WHERE gross_revenue < 0
  AND is_refunded = false;
  ```

Result:

![](/images/5-Workshop/5.9-Validate-curated-data/image-004.png)

The validation logic in the Glue ETL Job has successfully removed all invalid transactions.

### Check important null fields in fact_transactions

Run the following query to check key columns in the transaction table:

```sql
SELECT
SUM(CASE WHEN transaction_id IS NULL THEN 1 ELSE 0 END) AS null_transaction_id,
SUM(CASE WHEN transaction_timestamp IS NULL THEN 1 ELSE 0 END) AS null_transaction_timestamp,
SUM(CASE WHEN product_id IS NULL THEN 1 ELSE 0 END) AS null_product_id,
SUM(CASE WHEN gross_revenue IS NULL THEN 1 ELSE 0 END) AS null_gross_revenue
FROM ecommerce_curated.curated_fact_transactions;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-005.png)

The results show:

- null_transactions_id = 0

- null_transaction_timestamp = 0

- null_product_id = 0

- null_gross_revenue = 0

These columns were used in the validation logic of the Glue ETL Job, so valid data in the curated layer should have no errors in these fields.

#### Conclusion

After completing the validation step, we can confirm that:

- The curated data has been successfully crawled into the Glue Data Catalog

- Athena can query the Parquet tables in the curated tier

- The fact_events, dim_products, and fact_transactions tables have the correct schema

- Data has been cleaned and converted to appropriate data types

- Invalid transaction data has been removed from the curated_fact_transactions table

- The curated tier is ready to connect to Amazon QuickSight and build analytics dashboards

After this step, the project can move on to connecting Athena with QuickSight for data visualization.
