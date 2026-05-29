---
title: "5.4. Create the Glue Data Catalog for Raw Data"
linkTitle: "5.4. Create the Glue Data Catalog for Raw Data"
menuTitle: "5.4. Create the Glue Data Catalog for Raw Data"
date: 2026-05-29
weight: 540
chapter: false
---


The objective of this step is to create the **AWS Glue Data Catalog** to store metadata for the CSV files in Amazon S3. Once the Data Catalog is in place, Amazon Athena can read and query the raw data from S3.

In this project, the raw data consists of 3 groups of files:

- raw/events/

- raw/products/

- raw/transactions/

After the crawler runs successfully, Glue will automatically create the corresponding schema and metadata tables for each data group.

**Next flow:**

S3 raw -> Glue IAM Role -> Glue Database -> Glue Crawler raw -> Run crawler -> Check tables in Glue Data Catalog -> Query with Athena
