---
title: "5.8. Create the Glue Data Catalog for Curated Data"
linkTitle: "5.8. Create the Glue Data Catalog for Curated Data"
menuTitle: "5.8. Create the Glue Data Catalog for Curated Data"
date: 2026-05-29
weight: 580
chapter: false
---

After the Glue ETL Job runs successfully, the data has been written to the **curated/** tier in Parquet format. In this step, we will create a new Glue Database and Glue Crawler to crawl the Parquet data in the curated tier. After the crawler finishes, Athena can query the curated tables directly.

The curated data currently available in S3 includes:
```
curated/
├── fact_events/
├── dim_products/
└── fact_transactions/
```

After the crawler runs successfully, the Glue Data Catalog will create **3 tables**:

- curated_fact_events

- curated_dim_products

- curated_fact_transactions
