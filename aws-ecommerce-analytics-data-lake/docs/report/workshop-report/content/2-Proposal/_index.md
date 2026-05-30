---
title: "Proposal"
date: 2026-05-29
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

## BUILDING A SERVERLESS E-COMMERCE ANALYTICS DATA LAKE ON AWS

### 1. Executive Summary

**E-commerce Analytics Data Lake on AWS** is built to process and analyze e-commerce data using a serverless approach on the AWS platform. The solution uses the Marketing & E-commerce dataset from Kaggle, including user behavior data, product data, and transaction data.

The solution is designed based on a data lake model, in which Amazon S3 serves as the central data storage layer. The initial data is uploaded to the S3 Raw Zone in CSV format, then processed by an AWS Glue ETL Job to clean, standardize, validate errors, and convert it into Parquet format in the S3 Curated Zone. Amazon Athena is used to query the data and create semantic views for analytics. Amazon QuickSight is used to build dashboards that visualize important business metrics.

In addition to data processing and analytics, the workshop also implements an automation and monitoring layer for the pipeline. EventBridge Scheduler is used to automatically trigger the Glue Workflow on a schedule, while EventBridge Rules and SNS Email Notification are used to send alerts when a Glue Job or Glue Crawler fails.

The workshop aims to simulate a complete e-commerce data analytics pipeline, from raw data to business dashboards.

### 2. Problem Statement

***Current Problem***

In e-commerce, data is often generated from many different sources such as user events, marketing campaigns, product information, and purchase transactions. If these datasets are only stored as raw CSV files, analytics becomes difficult:

* Data is distributed across multiple files and multiple domains.
* Raw data may contain missing values, incorrect data types, or inconsistent formats.
* Values such as traffic source may have inconsistent uppercase/lowercase formatting.
* Transaction data may contain invalid records, such as missing product_id, missing gross_revenue, or negative revenue that is not marked as a refund.
* Querying raw CSV files directly with Athena can be more costly and less performant than querying Parquet data.
* Dashboards are difficult to build if all business logic must be written directly in QuickSight.
* A manual pipeline can easily cause errors if crawlers, ETL jobs, and curated crawlers must be run step by step by hand.

Therefore, a data pipeline is needed that can store, process, standardize, analyze, visualize, and automate data through a clear workflow.

***Solution***

The proposed solution is to build a serverless E-commerce Analytics Data Lake on AWS.

The pipeline uses Amazon S3 as the data lake and divides data into the following zones:

* Raw Zone: stores the initial CSV data.
* Curated Zone: stores processed data in Parquet format.
* Error Zone: stores invalid transaction records.
* Athena Results: stores Athena query results.

AWS Glue Crawler is used to automatically scan data in S3 and create metadata in the AWS Glue Data Catalog. AWS Glue ETL Job processes data using PySpark, including data type casting, timestamp parsing, text standardization, invalid transaction validation, writing valid data to the curated zone, and writing invalid data to the error zone.

Amazon Athena is used to validate raw/curated data and create business views. These views act as a semantic layer for Amazon QuickSight. Amazon QuickSight visualizes data through dashboards such as Executive Overview, Funnel Analytics, Marketing Performance, Product Analytics, and A/B Testing.

To automate the pipeline, EventBridge Scheduler is used to trigger the Glue Workflow on a schedule. The Glue Workflow orchestrates the execution order: Raw Crawler → Glue ETL Job → Curated Crawler. EventBridge Rules are used to capture Glue Job or Glue Crawler failures and send notifications through SNS Email Notification.

***Benefits and Return on Investment (ROI)***

The solution provides the following key benefits:

* Automates the data processing workflow from raw to curated.
* Reduces manual operations when running crawlers and ETL jobs.
* Optimizes queries by converting data from CSV to Parquet.
* Organizes data according to a clear data lake model.
* Separates invalid data into the Error Zone for easier inspection and debugging.
* Creates a semantic layer using Athena Views, making dashboards easier to use.
* Supports business decision-making through QuickSight dashboards.
* Provides a pipeline failure alert mechanism using EventBridge Rules and SNS.
* Suitable for learning environments, workshop demos, and AWS Data Engineering portfolios.

In terms of ROI, the solution helps reduce manual operation time, reduce data preparation time for dashboards, and create an extensible foundation for advanced analytics use cases such as customer segmentation, recommendation, or churn analysis in the future.

### 3. Solution Architecture

The solution uses an AWS Serverless Data Analytics architecture, in which the main components include Amazon S3, AWS Glue, Amazon Athena, Amazon QuickSight, EventBridge, CloudWatch Logs, SNS, and IAM.

Overall architecture flow:

```text
Kaggle Marketing & E-commerce Dataset
        |
        v
Local Preprocessing
Rename columns only
        |
        v
Amazon S3 Raw Zone
raw/events/
raw/products/
raw/transactions/
        |
        v
AWS Glue Crawler Raw
Raw metadata catalog
        |
        v
Amazon Athena Raw Validation
Schema checks, null checks, duplicates, abnormal values
        |
        v
AWS Glue Batch ETL Job
Clean, cast, validate, enrich, partition, convert to Parquet
        |
        v
Amazon S3 Curated Zone + Error Zone
curated/fact_events/
curated/dim_products/
curated/fact_transactions/
error/transactions/
        |
        v
AWS Glue Crawler Curated
Curated metadata catalog
        |
        v
Amazon Athena Semantic Views
Business-ready SQL views
        |
        v
Amazon QuickSight Dashboards
Executive, Funnel, Marketing, Product, A/B Testing
        |
        v
Automation & Monitoring
EventBridge Scheduler + Glue Workflow + EventBridge Rules + CloudWatch Logs + SNS Alert
```

#### AWS Services Used

* **Amazon S3:**
  Used as the main data lake to store raw data, curated data, error data, and Athena query results.

* **AWS Glue Data Catalog:**
  Stores metadata of raw tables and curated tables so that Athena can query data on S3.

* **AWS Glue Crawler:**
  Automatically scans data in S3 and creates metadata tables. The project uses a Raw Crawler and a Curated Crawler.

* **AWS Glue ETL Job:**
  Processes CSV data from the raw zone, cleans, standardizes, validates, and writes Parquet data to the curated zone.

* **AWS Glue Workflow:**
  Orchestrates the execution flow Raw Crawler → Glue ETL Job → Curated Crawler in order.

* **Amazon Athena:**
  Queries data directly on S3 using SQL, validates data, and creates business views for dashboards.

* **Amazon QuickSight:**
  Connects to Athena to build e-commerce data analytics dashboards.

* **Amazon EventBridge Scheduler:**
  Automatically triggers the Glue Workflow on a schedule through the StartWorkflowRun API.

* **Amazon EventBridge Rules:**
  Captures failure events from Glue Job and Glue Crawler.

* **Amazon SNS:**
  Sends email notifications when the pipeline encounters errors.

* **Amazon CloudWatch Logs:**
  Stores logs of the Glue ETL Job for inspection and debugging.

* **AWS IAM:**
  Manages access permissions for Glue, EventBridge Scheduler, and related services.

#### Component Design

* **Data Source:**
  The Marketing & E-commerce dataset from Kaggle, including events.csv, products.csv, and transactions.csv.

* **Local Preprocessing:**
  Checks the initial data and renames some columns for easier processing, such as timestamp to event_timestamp or transaction_timestamp.

* **S3 Raw Zone:**
  Stores the initial CSV data by domain: events, products, and transactions.

* **Raw Glue Crawler:**
  Scans raw data and creates metadata tables in the ecommerce_raw database.

* **Athena Raw Validation:**
  Checks schema, row counts, event types, categories, quantity, null values, and abnormal values.

* **Glue ETL Job:**
  Cleans data, standardizes data types, validates invalid transactions, creates time columns, writes Parquet data, and partitions by year/month/day.

* **S3 Curated Zone:**
  Stores processed data including fact_events, dim_products, and fact_transactions.

* **Error Zone:**
  Stores invalid transactions for later inspection.

* **Curated Glue Crawler:**
  Scans curated data and creates metadata tables in the ecommerce_curated database.

* **Athena Semantic Views:**
  Creates views for dashboards such as executive overview, funnel, marketing, product, and A/B testing.

* **QuickSight Dashboards:**
  Visualizes data from multiple business perspectives.

* **Automation & Monitoring:**
  EventBridge Scheduler runs the workflow on a schedule, EventBridge Rules capture errors, SNS sends emails, and CloudWatch Logs supports debugging.

### 4. Technical Implementation

#### Implementation Phases

The project is implemented through the following main phases:

**Phase 1: Data Exploration and Architecture Design**
Study the dataset from Kaggle, identify the main data files, analyze schemas, define fact/dimension tables, and design the AWS data lake architecture.

**Phase 2: Building the S3 Data Lake**
Create an S3 bucket and organize folders by zones: raw, curated, error, and athena-results. Upload CSV data after local preprocessing to the correct folders in the Raw Zone.

**Phase 3: Creating Glue Data Catalog for Raw Data**
Create an IAM Role for AWS Glue, create the Glue Database ecommerce_raw, and create a Raw Crawler to crawl CSV data in the Raw Zone.

**Phase 4: Validating Raw Data with Athena**
Configure the Athena query result location, query raw data, and run validation queries such as row counts, event types, product categories, and quantity distribution.

**Phase 5: Developing Glue ETL Job**
Write the Glue ETL script using PySpark to process events, products, and transactions data. The ETL Job performs cleaning, casting, validation, partitioning, and conversion to Parquet.

**Phase 6: Creating Glue Data Catalog for Curated Data**
Create the Glue Database ecommerce_curated, create the Curated Crawler, and crawl Parquet data in the Curated Zone.

**Phase 7: Validating Curated Data**
Use Athena to validate data after ETL, including total row counts, refund data, invalid transactions, null values, and curated schema.

**Phase 8: Creating Athena Views**
Create business views for dashboards such as vw_executive_overview, vw_daily_event_funnel, vw_traffic_source_performance, vw_product_revenue, and vw_ab_testing_summary.

**Phase 9: Building QuickSight Dashboards**
Connect QuickSight to Athena using Direct Query and build business analytics dashboards.

**Phase 10: Automation & Monitoring**
Create Glue Workflow, EventBridge Scheduler, EventBridge Rules, SNS Email Notification, and check CloudWatch Logs for the Glue ETL Job.

#### Technical Requirements

**Input Data:**

* events.csv
* products.csv
* transactions.csv

**AWS Infrastructure:**

* Amazon S3 bucket for the data lake.
* AWS Glue Data Catalog for raw and curated databases.
* AWS Glue Crawlers for raw zone and curated zone.
* AWS Glue ETL Job using PySpark.
* Amazon Athena for data querying.
* Amazon QuickSight for visualization.
* EventBridge Scheduler for scheduled workflow execution.
* EventBridge Rules and SNS for failure alerts.
* CloudWatch Logs for monitoring ETL logs.

**Access Permissions:**

* IAM Role for AWS Glue with AWSGlueServiceRole permissions and S3 access.
* IAM Role for EventBridge Scheduler with glue:StartWorkflowRun permission.
* SNS email subscription confirmed.

**Data Processing Requirements:**

* Parse timestamp.
* Cast data types.
* Standardize traffic_source.
* Handle null device_type.
* Cast is_premium and is_refunded to boolean.
* Validate invalid transactions.
* Write Parquet.
* Partition fact_events and fact_transactions by year/month/day.
* Create Athena Views for QuickSight.

### 5. Roadmap & Implementation Milestones

#### Preparation

* Define the project topic and scope.
* Select a suitable dataset from Kaggle.
* Explore schema and data quality issues.
* Design the overall pipeline architecture.
* Prepare an AWS account, S3 bucket, and required access permissions.

#### Phase 1: Data Lake Foundation

* Create an S3 bucket.
* Create the folder structure: raw, curated, error, and athena-results.
* Upload CSV data to the S3 Raw Zone.
* Create a Glue IAM Role.
* Create a Glue Database for raw data.
* Create and run the Raw Crawler.

#### Phase 2: Data Validation & ETL

* Configure Athena query result location.
* Query and validate raw tables.
* Develop Glue ETL Job.
* Run Glue ETL Job.
* Check output in the S3 Curated Zone and Error Zone.
* Create Glue Database and Crawler for curated data.
* Validate curated data using Athena.

#### Phase 3: Analytics Layer & Dashboard

* Create Athena Views for analytics.
* Connect QuickSight to Athena.
* Create calculated fields and filters.
* Build the Executive Overview dashboard.
* Build the Funnel Analytics dashboard.
* Build the Marketing Performance dashboard.
* Build the Product Analytics dashboard.
* Build the A/B Testing dashboard.

#### Phase 4: Automation & Monitoring

* Create an SNS Topic and email subscription.
* Create a Glue Workflow.
* Create EventBridge Scheduler to start the Glue Workflow.
* Create EventBridge Rules to capture crawler/job failures.
* Check CloudWatch Logs.
* Test schedule and alert.
* Complete documentation and host the report using Hugo/GitHub Pages.

### 6. Budget Estimate

The actual cost depends on data volume, the number of Glue Job runs, the number of Athena queries, the number of QuickSight dashboards, and usage duration. Within the scope of the workshop, the project is implemented at a small scale, mainly for learning and demo purposes.

**AWS Pricing Calculator** can be used to estimate costs more accurately before deployment.

#### Estimated Infrastructure Costs

* **Amazon S3:**
  Used to store raw CSV, curated Parquet, error data, and Athena query results. With the small data volume used in the workshop, storage cost is low.

* **AWS Glue Crawler:**
  Costs are incurred when crawlers run to crawl the Raw Zone and Curated Zone.

* **AWS Glue ETL Job:**
  Costs are incurred based on runtime and the number of DPUs used. The project only runs ETL on a schedule or when testing is needed, so costs can be controlled.

* **Amazon Athena:**
  Costs are based on the amount of data scanned per query. Converting data to Parquet and partitioning by year/month/day helps reduce the amount of scanned data.

* **Amazon QuickSight:**
  Costs depend on the account type, number of authors/readers, and usage mode. The project uses Direct Query to avoid managing SPICE refresh.

* **Amazon EventBridge Scheduler** and **EventBridge Rules:**
  Costs are low within the workshop scope because the number of schedules and rules is small.

* **Amazon SNS:**
  Costs are low because email notifications are only sent when the pipeline encounters errors.

* **Amazon CloudWatch Logs:**
  Costs depend on the amount of logs generated by the Glue ETL Job.

#### Overall Estimate

At workshop scale, costs can be controlled by:

* Running Glue Jobs on a reasonable schedule.
* Avoiding running crawlers too frequently.
* Using Parquet to reduce Athena scans.
* Deleting unnecessary test data.
* Monitoring billing in the AWS Billing Dashboard.
* Creating AWS Budget if cost alerts are needed.

### 7. Risk Assessment

#### Risk Matrix

**Risk 1: Glue ETL Job failed**

* Impact: High
* Probability: Medium
* Cause: May be caused by incorrect schema, incorrect data types, missing S3 permissions, or PySpark errors.

**Risk 2: Glue Crawler does not detect the schema correctly**

* Impact: Medium
* Probability: Medium
* Cause: May be caused by inconsistent CSV data, incorrect headers, or incorrect S3 folder paths.

**Risk 3: Athena query errors or scans too much data**

* Impact: Medium
* Probability: Medium
* Cause: May be caused by outdated table metadata, incorrect partitions, or unoptimized queries.

**Risk 4: QuickSight cannot connect to Athena/S3**

* Impact: Medium
* Probability: Medium
* Cause: May be caused by incorrect region, missing S3 access permissions, or QuickSight not being granted access to Athena.

**Risk 5: AWS costs increase unexpectedly**

* Impact: Medium
* Probability: Low to Medium
* Cause: May be caused by running Glue/Athena/QuickSight too many times or querying raw CSV data too frequently.

**Risk 6: EventBridge Scheduler or alerts are configured incorrectly**

* Impact: Medium
* Probability: Medium
* Cause: May be caused by an incorrect IAM Role, incorrect API target, incorrect input JSON, or unconfirmed SNS email subscription.

#### Mitigation Strategies

**For Glue ETL Job failures:**

* Check CloudWatch Logs.
* Test the script with a small dataset first.
* Validate raw schema before running ETL.
* Separate invalid data into the Error Zone.

**For Glue Crawler:**

* Check the correct S3 path.
* Use clear table prefixes.
* Rerun the crawler after ETL writes new data.

**For Athena:**

* Use Parquet instead of querying raw CSV directly.
* Partition fact_events and fact_transactions by year/month/day.
* Create Athena Views to reduce errors when used in QuickSight.

**For QuickSight:**

* Ensure QuickSight, Athena, Glue, and S3 are in the same region.
* Grant QuickSight access to Athena and the S3 bucket.
* Use Direct Query so data is updated according to Athena views.

**For costs:**

* Monitor the AWS Billing Dashboard.
* Limit continuous Glue Job and Crawler runs.
* Delete unnecessary resources after the workshop.
* Use AWS Budget if needed.

**For automation and alerts:**

* Test the Glue Workflow manually first.
* Test EventBridge Scheduler using a cron expression close to the current time.
* Check Workflow History and Job run monitoring.
* Confirm the SNS email subscription before creating alert rules.

#### Contingency Plan

* If EventBridge Scheduler fails, the Glue Workflow can be run manually.
* If the Glue Workflow fails, each step can be run separately: Raw Crawler → Glue ETL Job → Curated Crawler.
* If QuickSight encounters errors, Athena query results can be used to demonstrate analytics.
* If costs exceed expectations, pause the schedule and only run the pipeline when needed for demo.
* If alerts are not working, manually check CloudWatch Logs and Glue Job Run History.

### 8. Expected Outcomes

After completing the workshop, the project is expected to achieve the following outcomes:

#### Technical Outcomes

* Build an AWS Data Lake with a clear structure including Raw Zone, Curated Zone, Error Zone, and Athena Results.
* Create Glue Data Catalog for raw data and curated data.
* Build a Glue ETL Job to process CSV data into Parquet.
* Validate invalid data and separate invalid transactions into the Error Zone.
* Create Athena Views that act as a semantic layer for dashboards.
* Connect QuickSight to Athena using Direct Query.
* Build business analytics dashboards.
* Create a Glue Workflow to orchestrate the pipeline.
* Create EventBridge Scheduler to automatically run the workflow on a schedule.
* Create EventBridge Rules and SNS Email Notification for failure alerts.

#### Business Analytics Outcomes

The project helps answer important analytics questions:

* How does revenue change over time?
* Are the number of orders and average order value stable?
* Is the refund rate increasing abnormally?
* At which step in the funnel do users drop off the most?
* Which traffic source generates the most purchases?
* Which campaign has a good conversion rate?
* Which product, category, or brand generates the highest revenue?
* Are premium products more effective than non-premium products?
* Which product or category has a high refund rate?
* Which experiment group in A/B testing has better conversion?

#### Long-Term Value

The project can be extended to support advanced use cases such as:

* Customer segmentation.
* Churn analysis.
* Recommendation system.
* Marketing attribution.
* Data quality monitoring.
* CI/CD for Glue scripts and Athena views.
* Cost monitoring using AWS Budgets.
* Dashboard sharing or embedding.

Overall, the project is not only a data analytics dashboard, but also simulates a complete Data Engineering workflow on AWS. This is a suitable foundation for developing practical skills in data lake, ETL, SQL analytics, BI dashboard, automation, and monitoring in a cloud environment.
