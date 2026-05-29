---
title: "5.5. Create a Glue Crawler for Raw Data"
linkTitle: "5.5. Create a Glue Crawler for Raw Data"
menuTitle: "5.5. Create a Glue Crawler for Raw Data"
date: 2026-05-29
weight: 550
chapter: false
---


**AWS Glue Crawler** is used to scan data in S3, automatically detect the schema, and create metadata tables in the Glue Data Catalog.

In this step, the crawler will scan the folder: **s3:// ecommerce-analytics-datalake-270642943130-ap-southeast-1-an/raw/**

After the crawler runs successfully, the system will create 3 tables corresponding to the raw data:

- raw_events

- raw_products

- raw_transactions

### Create a Glue Crawler

Access **AWS Glue**, in the left menu select: **Data Catalog** → **Crawlers**

Then click **Create crawler**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-001.png)

### Configure crawler properties

On the **Set crawler properties** screen, enter:

- Name: **crawler_ecommerce_raw**

Then click **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-002.png)

### Add a data source for the crawler

At the **Data sources** step, click **Add a data source**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-003.png)

In the **Add a data source** screen, configure as follows:

- Data source: Select **S3**

- S3 path: Click **Browse S3**

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-004.png)

Select the bucket created in the previous step, then select the **raw/** folder, click **Choose** to confirm the path.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-005.png)

After selecting the S3 path, click **Add an S3 data source**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-006.png)

Then click **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-007.png)

### Select an IAM Role for the crawler

On the **Configure security settings** screen, in the IAM Role section, select the role **AWSGlueServiceRoleDefault** created in the previous step, then click **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-008.png)

This role allows the Glue Crawler to access data in S3 and write metadata to the Glue Data Catalog.

### Configure output and crawler schedule

On the **Set output and scheduling** screen, configure as follows:

- Target database: select **ecommerce_raw**

- Table name prefix: **raw_**

- Crawler schedule: **On demand** because the crawler will be run manually. Automatic scheduling via EventBridge/Glue Workflow will be configured in later steps.

Once configured, click **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-009.png)

### Review and create the crawler

On the **Review and create** screen, review the configured information:

- Crawler name

- S3 data source

- IAM Role

- Target database

- Table name prefix

- Crawler schedule

If the information is correct, click **Create crawler**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-010.png)

The crawler **crawler_ecommerce_raw** has been successfully created.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-011.png)

### Run the Crawler

After creating the crawler, select crawler **crawler_ecommerce_raw**

Click **Run crawler** to start scanning data in S3.

The crawler will read data in the **raw/** folder, automatically detect the schema, and create metadata tables in the Glue Data Catalog. After the crawler runs successfully, its status will display as completed and show information about the number of tables created or updated.

The crawler will create **3 tables** corresponding to the 3 raw data groups.

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-001.png)

### Check the schema in the Glue Catalog

After the crawler finishes, go to **AWS Glue** → **Data Catalog** → **Tables**.

Here, check the tables that have been created in the **ecommerce_raw** database.

The tables include:

- raw_events

- raw_products

- raw_transactions

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-002.png)

Click on each table to view the detailed table information.

- **raw_events:**

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-003.png)

- **raw_products:**

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-004.png)

- **raw_transactions:**

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-005.png)

All 3 tables raw_events, raw_products, and raw_transactions have appeared in the Glue Data Catalog. The process of creating the crawler for raw data is complete.
After this step, the raw data in Amazon S3 has had its metadata registered into the AWS Glue Data Catalog. The data can be queried using Amazon Athena before performing the ETL step to the curated tier.
