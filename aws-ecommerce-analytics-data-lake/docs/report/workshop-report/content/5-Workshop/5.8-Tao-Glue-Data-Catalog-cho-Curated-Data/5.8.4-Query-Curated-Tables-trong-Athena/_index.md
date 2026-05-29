---
title: "5.8.4. Query Curated Tables in Athena"
linkTitle: "5.8.4. Query Curated Tables in Athena"
menuTitle: "5.8.4. Query Curated Tables in Athena"
date: 2026-05-29
weight: 584
chapter: false
---

# 5.8.4. Query Curated Tables in Athena

This page uses Athena to query the curated tables and confirm that the transformed data is available for analytics.

## What This Page Covers
- Select the ecommerce_curated database in Athena.
- Run sample queries against curated_fact_events.
- Run sample queries against curated_fact_transactions.
- Run sample queries against curated_dim_products.
- Check that important columns and partitions are visible.

## Reference Commands and Queries

The SQL, JSON, or command snippets used in the Vietnamese walkthrough are kept below for the English version.

```sql
SELECT COUNT(*) AS total_events
FROM ecommerce_curated.curated_fact_events;
```

```sql
SELECT year, month, day, COUNT(*) AS total_events
FROM ecommerce_curated.curated_fact_events
GROUP BY year, month, day
ORDER BY year, month, day
LIMIT 20;
```

```sql
SELECT COUNT(*) AS total_transactions
FROM ecommerce_curated.curated_fact_transactions;
```

```sql
SELECT year, month, day, COUNT(*) AS total_transactions
FROM ecommerce_curated.curated_fact_transactions
GROUP BY year, month, day
ORDER BY year, month, day
LIMIT 20;
```

```sql
SELECT COUNT(*) AS total_products
FROM ecommerce_curated.curated_dim_products;
```

```sql
SELECT
category,
COUNT(*) AS product_count
FROM ecommerce_curated.curated_dim_products
GROUP BY category
ORDER BY product_count DESC;
```

## Screenshots

The following screenshots match the implementation steps in this page.

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-001.png)

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-002.png)

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-003.png)

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-004.png)

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-005.png)

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-006.png)
