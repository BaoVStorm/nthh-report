---
title: "5.6. Configure the Athena Query Result Location"
linkTitle: "5.6. Configure the Athena Query Result Location"
menuTitle: "5.6. Configure the Athena Query Result Location"
date: 2026-05-29
weight: 560
chapter: false
---

**Amazon Athena** requires a location in Amazon S3 to store query results. Therefore, before running queries, it is necessary to configure the **Query result location for Athena**.

In this project, Athena query results will be stored in the folder:

**s3:// ecommerce-analytics-datalake-270642943130-ap-southeast-1-an/athena-results/**

### Access Amazon Athena

Search for and select the **Amazon Athena** service in the search bar:

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-001.png)

### Configure the Query result location

In the **Athena Query editor** interface, select **Edit settings**.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-002.png)

Next, select **Manage** to configure the query result storage location.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-003.png)

In the **Query result location** section, click **Browse S3**.

Select the S3 bucket that was created, then select the **athena-results/** folder. Click **Choose** to confirm the result storage location.

Then click **Save** to save the configuration.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-004.png)

After saving successfully, Athena has been configured with the query result location in S3.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-005.png)

### Query raw data with Athena

After configuring the query result location, proceed to validate the raw data whose metadata was created by the Glue Crawler in the Glue Data Catalog.

In the **Query editor** interface, configure as follows:

- Data source: **AwsDataCatalog**

- Database: **ecommerce_raw**

- Select **raw_events**

Then select **Preview Table** so Athena automatically generates a sample query statement.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-006.png)

### Query 10 rows of data from the raw_events table

Athena will automatically generate a query statement similar to the following:

```sql
SELECT *
FROM "ecommerce_raw"."raw_events"
LIMIT 10;
```

The query runs successfully, and the result will display the first 10 rows of data from the raw_events table.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-007.png)

After the query succeeds, check the following:

- Whether the data is displayed correctly

- Whether the column names match the original CSV file

- Whether the data types are reasonable

- Whether there are header errors, nulls, or column misalignment

The data is displayed correctly, meaning the raw_events table has had its metadata successfully created by the Glue Crawler and Athena can read the data from S3.

Repeat the same process for the two tables **raw_products** and **raw_transactions**.

#### Check the raw_products table

```sql
SELECT *
FROM "ecommerce_raw"."raw_products"
LIMIT 10;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-008.png)

#### Check the raw_transactions table

```sql
SELECT *
FROM "ecommerce_raw"."raw_transactions"
LIMIT 10;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-009.png)

All three tables were queried successfully. The raw data in S3 is now ready for the ETL processing step with AWS Glue.

### Validate data with aggregation queries

After checking the data preview, continue running several aggregation queries to validate the data logic in each table.

#### Check the number of events by type

The following query counts the number of records by each event_type in the raw_events table.

```sql
SELECT
event_type,
COUNT(*) AS event_count
FROM "ecommerce_raw"."raw_events"
GROUP BY event_type
ORDER BY event_count DESC;
```

The query result shows how many times each event type appears in the raw data.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-010.png)

#### Check the number of products by category

The following query counts the number of products by each category in the raw_products table.

```sql
SELECT
category,
COUNT(*) AS category_count
FROM "ecommerce_raw"."raw_products"
GROUP BY category
ORDER BY category_count DESC;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-011.png)

The query result helps verify which category groups the product data is classified into.

#### Check the number of transactions by quantity

The following query counts the number of transactions by each quantity value in the raw_transactions table.

```sql
SELECT
quantity,
COUNT(*) AS quantity_count
FROM "ecommerce_raw"."raw_transactions"
GROUP BY quantity
ORDER BY quantity_count DESC;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-012.png)

The query result helps verify the distribution of product quantities in transactions.

#### Conclusion

After successfully running the above queries, we can confirm that:

- Athena has been correctly configured with the query result location

- The Glue Data Catalog has recognized the metadata of the raw data

- The tables **raw_events**, **raw_products**, and **raw_transactions** can be queried successfully

- The raw data in S3 is ready for the ETL processing step with AWS Glue

In the next step, the project will proceed to create a Glue ETL Job to transform data from the raw tier to the curated tier.
