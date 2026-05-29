---
title: "5.8.4. Query Curated Tables trong Athena"
linkTitle: "5.8.4. Query Curated Tables trong Athena"
menuTitle: "5.8.4. Query Curated Tables trong Athena"
date: 2026-05-29
weight: 584
chapter: false
---

Sau khi Glue Crawler đã tạo metadata cho dữ liệu curated, ta có thể kiểm tra dữ liệu bằng **Amazon Athena**.

Truy cập **Amazon Athena**, trong **Query editor**, chọn:

- Data source: **AwsDataCatalog**

- Database: **ecommerce_curated**

#### Query bảng curated_fact_events

- Kiểm tra tổng số dòng trong bảng curated_fact_events:

```sql
SELECT COUNT(*) AS total_events
FROM ecommerce_curated.curated_fact_events;
```

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-001.png)

- Kiểm tra số lượng event theo từng partition year, month, day:

```sql
SELECT year, month, day, COUNT(*) AS total_events
FROM ecommerce_curated.curated_fact_events
GROUP BY year, month, day
ORDER BY year, month, day
LIMIT 20;
```

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-002.png)

Câu query này giúp kiểm tra dữ liệu fact_events đã được partition đúng theo ngày hay chưa.

#### Query bảng curated_fact_transactions

- Kiểm tra tổng số dòng trong bảng curated_fact_transactions:

```sql
SELECT COUNT(*) AS total_transactions
FROM ecommerce_curated.curated_fact_transactions;
```

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-003.png)

- Kiểm tra số lượng transaction theo từng partition year, month, day:

```sql
SELECT year, month, day, COUNT(*) AS total_transactions
FROM ecommerce_curated.curated_fact_transactions
GROUP BY year, month, day
ORDER BY year, month, day
LIMIT 20;
```

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-004.png)

Câu query này giúp kiểm tra dữ liệu transaction hợp lệ đã được ghi đúng vào tầng curated và partition đúng theo ngày.

#### Query bảng curated_dim_products

- Kiểm tra tổng số sản phẩm trong bảng curated_dim_products:

```sql
SELECT COUNT(*) AS total_products
FROM ecommerce_curated.curated_dim_products;
```

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-005.png)

- Kiểm tra số lượng sản phẩm theo từng category:

```sql
SELECT
category,
COUNT(*) AS product_count
FROM ecommerce_curated.curated_dim_products
GROUP BY category
ORDER BY product_count DESC;
```

![](/images/5-Workshop/5.8.4-Query-Curated-Tables-trong-Athena/image-006.png)

Câu query này giúp kiểm tra dữ liệu sản phẩm đã được crawl và phân loại đúng theo category.
