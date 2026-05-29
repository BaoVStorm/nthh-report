---
title: "5.7. Glue ETL Job"
linkTitle: "5.7. Glue ETL Job"
menuTitle: "5.7. Glue ETL Job"
date: 2026-05-29
weight: 570
chapter: false
---

In this step, we will create the **AWS Glue ETL Job** to process data from the raw tier to the curated tier.

The goal of the Glue ETL Job is: raw CSV → clean / cast / validate → curated Parquet

After the ETL runs successfully, data will be written to the following directories in S3:

- **curated/fact_events/**: stores cleaned event data

- **curated/dim_products/**: stores normalized product data

- **curated/fact_transactions/**: stores valid transaction data

- **error/transactions/**: stores invalid transaction records

### ETL Processing Logic

The Glue ETL Job reads CSV data from the S3 Raw Zone, then performs data cleaning, data type conversion, error data validation, and writes the results to the S3 Curated Zone in Parquet format.

The Glue Job reads data from the following paths:

- raw/events/

- raw/products/

- raw/transactions/

Output data is written to:

- curated/fact_events/

- curated/dim_products/

- curated/fact_transactions/

- error/transactions/

When reading CSV, using header=true, inferSchema=false, and recursiveFileLookup=true helps Glue read all CSV files in the corresponding raw folders and actively cast data types in the transform step.

#### Processing the raw_events table

- Input data source: **raw/events/**

- Processed data is written to: **curated/fact_events/**

**Main processing steps:**

- Parse the event_timestamp column to timestamp type with format yyyy-MM-dd HH:mm:ss.

- Cast event_id, customer_id, session_id, campaign_id columns to Long type.

- Trim the event_type column.

- Cast product_id from a float/string format such as "1004.0" to Long.

- Normalize null or empty values of device_type to "unknown".

- Normalize traffic_source to handle inconsistent upper/lowercase values, e.g.:

  + ORGANIC → Organic

  + PAID SEARCH → Paid Search

  + SOCIAL → Social

  + EMAIL → Email

  + DIRECT → Direct

- Trim the page_category and experiment_group columns.

- Cast session_duration_sec to Double.

- Add derived time columns:

  + event_date

  + event_hour

  + year

  + month

  + day

- Add an ingestion_timestamp column to record the data processing time.

- Select the necessary columns according to the curated schema.

- Write data in Parquet format to curated/fact_events/

- Partition data by year/month/day.

The processed **fact_events** table is used to analyze user behavior, funnel, traffic source, device type, campaign, and A/B testing.

#### Processing the raw_products table

- Input data source: **raw/products/**

- Processed data is written to: **curated/dim_products/**

**Main processing steps:**

- Cast product_id to Long type.

- Trim the category and brand columns.

- Cast base_price to Double type.

- Parse launch_date to date type with format yyyy-MM-dd.

- Cast is_premium to boolean:

- is_premium = 1 → true

- other values → false

- Add an ingestion_timestamp column to record the data processing time.

- Select the necessary columns according to the curated schema.

- Write data in Parquet format to curated/dim_products/.

This table is not partitioned by time because it is a product dimension table. The **dim_products** table is used to join with fact_transactions and fact_events via product_id.

#### Processing the raw_transactions table

- Input data source: **raw/transactions/**

- Valid processed data is written to: **curated/fact_transactions/**

- Error data is written to: **error/transactions/**

**Main processing steps:**

- Parse transaction_timestamp to timestamp type with format yyyy-MM-dd HH:mm:ss.

- Cast transaction_id, customer_id, product_id, campaign_id columns to Long type.

- Cast product_id from a float/string format such as "1004.0" to Long.

- Cast quantity to Integer.

- Cast discount_applied and gross_revenue to Double.

- Cast is_refunded to boolean:

  + is_refunded = 1 → true

  + Other values → false

- Add derived time columns:

  + transaction_date

  + transaction_hour

  + year

  + month

  + day

- Add an ingestion_timestamp column to record the data processing time.

- Split data into 2 groups:

  + **valid_transactions**: valid data written to curated/fact_transactions/

  + **invalid_transactions**: error data written to error/transactions/

A transaction is considered **invalid** if it meets any of the following conditions:

- transaction_timestamp parsing fails or is null.

- product_id is null.

- gross_revenue is null.

- gross_revenue < 0 but is_refunded = false.

For error data, add an **error_reason** column to describe the cause of the error:

- INVALID_TRANSACTION_TIMESTAMP

- MISSING_PRODUCT_ID

- MISSING_GROSS_REVENUE

- NEGATIVE_REVENUE_WITHOUT_REFUND_FLAG

Valid data is selected according to the curated schema, written in Parquet format to curated/fact_transactions/, and partitioned by year/month/day.
Error data is written in Parquet format to error/transactions/.
