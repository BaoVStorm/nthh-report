---
title: "BUILDING AN E-COMMERCE ANALYTICS DATA LAKE ON AWS USING A SERVERLESS APPROACH"
linkTitle: "Workshop"
menuTitle: "Workshop"
date: 2026-05-29
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Overview

- **Data Lake** is a centralized data storage architecture that allows storing data in various formats such as CSV, JSON, Parquet, or log files. In this workshop, **Amazon S3** is used as the Data Lake to store e-commerce data across multiple tiers: **Raw Zone**, **Curated Zone**, **Error Zone**, and **Athena Results**.

- **Serverless Data Analytics** on AWS is a way to build data analysis pipelines without directly managing servers. Services such as Amazon S3, AWS Glue, Amazon Athena, Amazon QuickSight, EventBridge, and SNS help automate the processes of data storage, processing, querying, visualization, and monitoring.

- **AWS Glue** is a serverless ETL service by AWS, used to crawl metadata, create a Data Catalog, and process data using PySpark. In this project, AWS Glue is used for three main tasks:

  + **Glue Crawler**: automatically scans data in S3 and creates metadata tables in the Glue Data Catalog.
  + **Glue ETL Job**: cleans data, transforms data types, validates erroneous data, writes curated data in Parquet format, and partitions it by time.
  + **Glue Workflow**: orchestrates the execution sequence of the pipeline, including Raw Crawler, Glue ETL Job, and Curated Crawler.

- **Amazon Athena** is a serverless query service that allows querying data directly on Amazon S3 using SQL. In this project, Athena is used to validate raw/curated data and create business views for dashboards.

- **Amazon QuickSight** is a Business Intelligence service by AWS, used to visualize data from Athena. The dashboards in this project help analyze revenue, orders, funnel, marketing performance, product performance, and A/B testing.

- **EventBridge Scheduler**, **EventBridge Rules**, and **Simple Notification Service** (SNS) are used to automate and monitor the pipeline. EventBridge Scheduler automatically triggers the Glue Workflow on a schedule, EventBridge Rules catch Glue Job/Crawler errors, and SNS sends email notifications when the pipeline encounters errors.

The goal of the workshop is to build a complete e-commerce data analytics pipeline on AWS, starting from the initial raw data to business analytics dashboards, complete with basic automation and error alerting.
