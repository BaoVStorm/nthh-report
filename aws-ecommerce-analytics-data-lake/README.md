# Serverless Clickstream Data Lake for E-commerce Analytics on AWS

A serverless AWS data engineering project that collects, stores, transforms, and analyzes e-commerce clickstream data such as `view`, `add_to_cart`, and `purchase` events. The system is designed as a lightweight end-to-end pipeline for learning, internship reporting, and portfolio building.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Business Problem](#business-problem)
- [Solution Overview](#solution-overview)
- [Architecture](#architecture)
- [Processing Flow](#processing-flow)
- [AWS Services Used](#aws-services-used)
- [Data Lake Storage Structure](#data-lake-storage-structure)
- [Event Schema](#event-schema)
- [Suggested Repository Structure](#suggested-repository-structure)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Deployment Steps](#deployment-steps)
- [End-to-End Pipeline Flow](#end-to-end-pipeline-flow)
- [Core Analytics Queries](#core-analytics-queries)
- [Expected Dashboard Components](#expected-dashboard-components)
- [Monitoring and Logging](#monitoring-and-logging)
- [Security](#security)
- [Cost Optimization](#cost-optimization)
- [Expected Outcomes](#expected-outcomes)
- [Future Improvements](#future-improvements)
- [Learning Value](#learning-value)
- [Author](#author)
- [Notes](#notes)
- [License](#license)

---

## Project Overview

In e-commerce environments, user behavior data is an important source of insight for understanding customer journeys and improving business performance. However, many small systems and learning projects do not have a proper data pipeline for collecting, storing, transforming, and analyzing clickstream data.

This project builds a **serverless clickstream data lake on AWS** to simulate a real-world **AWS Data Engineer** use case. It is suitable for an **internship report**, **personal portfolio**, or **hands-on learning project** focused on cloud-native data pipelines.

The system captures clickstream events such as:

- `view`
- `add_to_cart`
- `purchase`

These events are ingested, stored in an Amazon S3 data lake, transformed using AWS Glue, queried with Amazon Athena, visualized through Amazon QuickSight, and monitored using Amazon CloudWatch.

---

## Objectives

The main objectives of this project are:

- Collect clickstream events from an event generator or lightweight web client
- Store raw and processed data in an S3-based data lake
- Transform raw JSON events into analytics-ready Parquet datasets
- Query processed data using SQL with Amazon Athena
- Build dashboards for clickstream analytics using Amazon QuickSight
- Monitor the pipeline with Amazon CloudWatch
- Apply basic AWS security and cost control practices

---

## Business Problem

This project addresses a common analytics problem in e-commerce:

- How many product views occur each day?
- Which products receive the most attention?
- What is the conversion flow from `view` to `add_to_cart` to `purchase`?
- Which categories are most popular?
- How does purchase activity change over time?

Without a centralized data pipeline, clickstream data is often scattered, difficult to query, and hard to use for dashboards or reporting. This project solves that by building a structured serverless analytics pipeline on AWS.

---

## Solution Overview

The proposed solution uses AWS serverless services to build a small but practical clickstream analytics platform.

User events are generated from a Python event generator or a simple web client. These events are sent to Amazon API Gateway, processed by AWS Lambda, and stored in Amazon S3 as raw data. AWS Glue Crawlers and Glue ETL Jobs are then used to discover schemas, clean data, transform JSON into Parquet, and organize it into partitions. Amazon Athena queries the processed data using SQL, Amazon QuickSight builds dashboards, and Amazon CloudWatch tracks logs, metrics, and errors.

This design is suitable for an AWS internship or student project because it demonstrates:

- cloud-native architecture
- serverless services
- end-to-end data pipeline design
- analytics and monitoring integration
- practical AWS service orchestration

---

## Architecture

### Proposed Architecture

```text
Event Generator / Web Client
        ↓
Amazon API Gateway
        ↓
AWS Lambda
        ↓
Amazon S3 (Raw Zone)
        ↓
AWS Glue Crawler / AWS Glue ETL
        ↓
Amazon S3 (Processed Zone)
        ↓
Amazon Athena
        ↓
Amazon QuickSight
        ↓
Amazon CloudWatch
```
## Processing Flow

The pipeline processes clickstream data through the following steps:

1. An **Event Generator** or **Web Client** produces clickstream events such as `view`, `add_to_cart`, and `purchase`.
2. **Amazon API Gateway** receives incoming requests from the client.
3. **AWS Lambda** validates the request payload and writes raw events to Amazon S3.
4. The **S3 Raw Zone** stores raw data in JSON format.
5. **AWS Glue Crawler** scans raw data and updates the Glue Data Catalog.
6. **AWS Glue ETL** cleans the data, standardizes fields, converts JSON to Parquet, and applies partitioning.
7. The **S3 Processed Zone** stores transformed datasets for analytics.
8. **Amazon Athena** queries processed data directly from S3 using SQL.
9. **Amazon QuickSight** visualizes the analytics through dashboards.
10. **Amazon CloudWatch** monitors logs, metrics, and pipeline health.

---

## AWS Services Used

| Service | Role in the Project |
|---|---|
| Amazon API Gateway | Receives requests from the event generator or web client |
| AWS Lambda | Processes incoming events and writes data to S3 |
| Amazon S3 | Stores raw and processed data in a data lake structure |
| AWS Glue Crawler | Discovers schema and creates the data catalog |
| AWS Glue ETL | Cleans, standardizes, and transforms data |
| Amazon Athena | Queries data using SQL |
| Amazon QuickSight | Creates analytics dashboards |
| Amazon CloudWatch | Provides logging, monitoring, and metrics |
| AWS IAM | Manages access control using least privilege |
| AWS CLI | Manages AWS resources from the command line |
| GitHub Actions / Deploy Scripts | Supports basic deployment automation |

---

## Data Lake Storage Structure

Data in Amazon S3 is organized using a simple data lake layout:

```text
s3://<your-bucket-name>/
├── raw/
│   └── year=2026/month=03/day=16/
│       └── events_001.json
├── processed/
│   └── event_type=view/year=2026/month=03/day=16/
│       └── part-000.parquet
├── analytics/
│   └── query-results/
└── logs/
```
### Zone Description

- **`raw/`**: stores raw incoming events from the ingestion layer
- **`processed/`**: stores transformed data in Parquet format with partitions
- **`analytics/`**: stores Athena query results or aggregated outputs
- **`logs/`**: stores optional logging or monitoring artifacts if needed

---

## Event Schema

A sample clickstream event looks like this:

```json
{
  "event_id": "evt_000001",
  "user_id": "user_123",
  "session_id": "sess_456",
  "event_type": "view",
  "product_id": "prod_789",
  "category": "electronics",
  "price": 299.99,
  "currency": "USD",
  "device_type": "mobile",
  "source": "homepage",
  "event_timestamp": "2026-03-16T10:30:00Z"
}
```
# AWS Clickstream Data Lake

## Main Fields

| Field | Description |
| :--- | :--- |
| `event_id` | Unique identifier of the event |
| `user_id` | User identifier |
| `session_id` | Session identifier |
| `event_type` | Event type: view, add_to_cart, purchase |
| `product_id` | Product identifier |
| `category` | Product category |
| `price` | Product price at event time |
| `currency` | Currency code |
| `device_type` | Access device type |
| `source` | Event source |
| `event_timestamp` | Event timestamp |

## Suggested Repository Structure

```text
aws-clickstream-data-lake/
├── README.md
├── docs/
│   ├── architecture/
│   ├── diagrams/
│   └── report/
├── data/
│   ├── sample/
│   └── mock/
├── event-generator/
│   ├── generate_events.py
│   └── requirements.txt
├── ingestion/
│   ├── lambda/
│   │   └── handler.py
│   └── api/
├── etl/
│   ├── glue_jobs/
│   └── sql/
├── dashboard/
│   └── screenshots/
├── infra/
│   ├── cli-scripts/
│   ├── cloudformation/
│   └── iam/
└── tests/
```
### Folder Description
* **`docs/`**: architecture, diagrams, and report materials
* **`data/`**: sample and mock datasets
* **`event-generator/`**: clickstream event simulation scripts
* **`ingestion/`**: API and Lambda source code
* **`etl/`**: Glue jobs and SQL queries
* **`dashboard/`**: dashboard screenshots or notes
* **`infra/`**: infrastructure scripts or templates
* **`tests/`**: component tests and end-to-end tests

## Prerequisites
Before running this project, make sure you have:
* An AWS account
* Access to S3, Lambda, Glue, Athena, QuickSight, and CloudWatch
* AWS CLI installed and configured
* Python 3.x
* Git
* An S3 bucket for the data lake
* A suitable AWS region
* A QuickSight account if dashboarding is required

## Environment Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)ngthhaiha/aws-clickstream-data-lake.git
cd aws-clickstream-data-lake
```
### 2. Configure AWS CLI
```bash
aws configure
```
You will need to provide:

* AWS Access Key ID
* AWS Secret Access Key
* Default region name
* Default output format

### 3. Verify AWS Identity

```bash
aws sts get-caller-identity
```

## Deployment Steps
### Step 1: Create an S3 Bucket
```bash
aws s3 mb s3://<your-bucket-name>
```
### Step 2: Prepare the Ingestion Layer
* Create an API Gateway endpoint
* Create a Lambda function to receive clickstream events
* Grant Lambda permission to write to S3
* Connect API Gateway to Lambda
### Step 3: Send Sample Data
Use the event generator to send events to API Gateway, or upload sample data directly to S3 for ETL testing.
### Step 4: Create a Glue Crawler
* Crawl the data in **`raw/`**
* Create a Glue Data Catalog table for raw data
### Step 5: Create a Glue Crawler
* Clean the data
* Standardize fields
* Convert JSON to Parquet
* Write outputs to **`processed/`**
### Step 6: Query with Athena
* Use the Glue Data Catalog table
* Run SQL queries on the processed clickstream dataset
### Step 7: Build Dashboards with QuickSight
* Connect QuickSight to Athena
* Create dashboards for key metrics
### Step 8: Monitor with CloudWatch
* Review Lambda logs
* Track request counts, errors, and durations
* Configure alarms if needed

## End-to-End Pipeline Flow
The full pipeline works as follows:
**1.** Generate clickstream events
**2.** Send events to API Gateway
**3.** Validate and store raw data in S3 through Lambda
**4.** Crawl raw data with Glue Crawler
**5.** Transform raw data into Parquet with Glue ETL
**6.** Query processed data using Athena
**7.** Visualize analytics in QuickSight
**8.** Monitor the pipeline with CloudWatch


## Core Analytics Queries
### Count Events by Type
```bash
SELECT event_type, COUNT(*) AS total_events
FROM processed_clickstream_events
GROUP BY event_type
ORDER BY total_events DESC;
```
### Top Viewed Products
``` bash
SELECT product_id, COUNT(*) AS total_views
FROM processed_clickstream_events
WHERE event_type = 'view'
GROUP BY product_id
ORDER BY total_views DESC
LIMIT 10;
```
### Conversion Funnel
``` bash
SELECT
    COUNT(CASE WHEN event_type = 'view' THEN 1 END) AS total_views,
    COUNT(CASE WHEN event_type = 'add_to_cart' THEN 1 END) AS total_add_to_cart,
    COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS total_purchases
FROM processed_clickstream_events;
```
### Daily Purchase Trend
``` bash
SELECT
    DATE(event_timestamp) AS event_date,
    COUNT(*) AS total_purchases
FROM processed_clickstream_events
WHERE event_type = 'purchase'
GROUP BY DATE(event_timestamp)
ORDER BY event_date;
```

## Expected Dashboard Components
The dashboard may include:
* Total events by day
* Event distribution by type
* Top viewed products
* Top purchased products
* Conversion funnel
* Purchase trend over time
* Event distribution by device type
* Event distribution by product category

## Monitoring and Logging
### Key Metrics
* Number of events received
* Number of successfully processed events
* Number of failed events
* Number of purchase events
* ETL job runtime
* Number of Athena queries
* Lambda duration and errors

### Monitoring Tools
* **CloudWatch Logs** for Lambda and Glue logs
* **CloudWatch Metrics** for requests, durations, and errors
* **CloudWatch Alarms** for failures or abnormal error rates

## Security
This project applies several basic AWS security practices:
* IAM least privilege
* Restricted S3 bucket access
* S3 encryption when needed
* Separate permissions for users, Lambda, and Glue
* No hard-coded access keys in source code
* Environment variables or proper secret handling where appropriate

## Cost Optimization
To keep costs low during learning and demonstration:

* Use small to medium-sized datasets
* Use batch processing instead of complex streaming
* Run Glue Crawlers and ETL jobs on demand or on schedule
* Store processed data in Parquet format
* Partition data to reduce Athena scan costs
* Track usage with AWS Budgets
* Limit QuickSight usage if account access is restricted

## Expected Outcomes
By the end of this project, the expected outcomes are:

* A working clickstream analytics pipeline on AWS
* Data organized in a data lake structure
* Basic automation for ingestion and ETL
* SQL-based analytics on processed data
* Dashboards for key business metrics
* Monitoring and logging for the pipeline
* A portfolio-ready project for Data Engineer Intern / Fresher roles

## Future Improvements
Possible future enhancements include:

* Near real-time streaming with Amazon Kinesis
* Advanced user and session analytics
* Recommendation analytics
* Anomaly detection for user behavior
* A/B testing analysis
* More dashboard KPIs
* Full CI/CD automation

## Learning Value
By completing this project, the developer can strengthen:

* End-to-end data pipeline design skills
* Hands-on experience with AWS serverless services
* Data lake design on Amazon S3
* ETL development with AWS Glue
* SQL analytics with Amazon Athena
* Dashboarding with Amazon QuickSight
* Monitoring, logging, and cost awareness on AWS

## Author
* **Author:** `Nguyen Thi Hai Ha`
* **Project Type:** Internship / Personal Project
* **Role:** AWS Data Engineer Intern

## Notes
* This is a learning and demo project built at small scale.
* Some components may be simplified to fit internship scope, time, and cost constraints.
* If QuickSight or API Gateway cannot be fully implemented, Athena query outputs or direct S3 uploads can be used as alternatives for demonstrating ETL and analytics.

## License
All rights reserved for internship reporting and personal portfolio only.


