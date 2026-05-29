---
title: "BUILDING AN E-COMMERCE ANALYTICS DATA LAKE ON AWS USING A SERVERLESS APPROACH"
linkTitle: "5.1. Introduction"
menuTitle: "5.1. Introduction"
date: 2026-05-29
weight: 510
chapter: false
---

## INTRODUCTION

In e-commerce, data is generated from many different activities such as users viewing products, clicking on content, adding products to the cart, completing purchases, requesting refunds, or participating in marketing campaigns. If this data is only stored as raw files, it becomes very difficult for businesses to extract insights to answer important questions such as: is revenue growing or declining, where in the funnel are customers dropping off, which traffic source performs best, which products sell the most, or which A/B testing group has a higher conversion rate.

The **E-commerce Analytics Data Lake on AWS** workshop is designed to simulate a complete Data Engineering workflow on AWS. The input data is the **Marketing & E-commerce Analytics Dataset** from Kaggle, which includes three main data groups:

- **events.csv**: contains user behavior data such as view, click, add to cart, bounce, and purchase.
- **products.csv**: contains product information such as category, brand, base price, launch date, and premium flag.
- **transactions.csv**: contains purchase transaction data, product quantities, discounts, gross revenue, and refund flags.

In this workshop, AWS services are combined to build a serverless data analytics pipeline.

- **Amazon S3** is used as the main Data Lake of the workshop. Data is organized into multiple tiers: *Raw Zone*, *Curated Zone*, *Error Zone*, and *Athena Results*. The Raw Zone stores the initial CSV data, the Curated Zone stores processed data in Parquet format, the Error Zone stores error records, and Athena Results is used to store query results from Athena.

- **AWS Glue Data Catalog** is used to store metadata of data in S3. When data resides in S3, the Glue Data Catalog helps services like Athena understand the schema, column names, data types, and storage location of each table.

- **AWS Glue Crawler** is used to automatically scan data in S3 and create metadata tables in the Glue Data Catalog. The project uses two main crawlers: one crawler for the Raw Zone and one for the Curated Zone. The Raw Crawler allows Athena to query the original CSV data, while the Curated Crawler allows Athena to query the Parquet data after ETL.

- **AWS Glue ETL Job** is the main data processing component. The Glue Job reads CSV data from the S3 Raw Zone, performs timestamp parsing, data type casting, text normalization, missing value handling, transaction error validation, and writes the processed data to the S3 Curated Zone in Parquet format. For the events and transactions tables, data is partitioned by year/month/day to optimize query performance. Invalid transactions are separated into the Error Zone for inspection and debugging.

- **Amazon Athena** is used to query data directly on Amazon S3 using SQL. In this project, Athena has two main roles: validating raw/curated data after each processing step, and creating business views for dashboards. The Athena Views serve as a semantic layer, pre-aggregating business logic such as revenue, orders, funnel conversion, marketing performance, product performance, and A/B testing.

- **Amazon QuickSight** is used to visualize data from Athena. The workshop uses QuickSight Direct Query to connect directly to Athena Views in the ecommerce_curated database. The dashboards are built to support business analytics, including Executive Overview, Funnel Analytics, Marketing Performance, Product Analytics, and A/B Testing.

- **AWS Glue Workflow** is used to orchestrate the execution sequence of the pipeline. The Workflow groups the Raw Crawler, Glue ETL Job, and Curated Crawler into an ordered processing flow. When the Raw Crawler runs successfully, the Glue ETL Job is triggered. After the Glue ETL Job completes, the Curated Crawler runs to update metadata for the curated data.

- **Amazon EventBridge Scheduler** is used to automatically trigger the Glue Workflow on a schedule. Instead of running each step manually, the EventBridge Scheduler calls the API StartWorkflowRun to start the workflow according to a cron schedule. This allows the pipeline to run automatically on a daily basis.

- **Amazon EventBridge Rules** are used to catch errors during pipeline operation. Rules are configured to detect error states such as Raw Crawler Failed, Curated Crawler Failed, Glue ETL Job Failed, Timeout, or Stopped.

- **Amazon Simple Notification Service** is used to send email notifications when the pipeline encounters an error. When an EventBridge Rule detects an error from a Glue Job or Glue Crawler, the event is sent to an SNS Topic and SNS sends an alert email to the operator.

- **Amazon CloudWatch Logs** is used to inspect logs of the Glue ETL Job. When a job fails or needs debugging, CloudWatch Logs helps check the details of the data reading, data processing, output writing, and any PySpark errors.

In terms of data processing, the pipeline starts from the local preprocessing step, where data is briefly inspected and some columns are renamed for easier processing. The CSV files are then uploaded to the Amazon S3 Raw Zone. From the raw tier, the Glue Crawler creates metadata so Athena can query the initial data. After the raw data is validated, the Glue ETL Job processes the data and writes the results to the Curated Zone in Parquet format. Next, the Curated Crawler updates metadata for the curated data. Finally, Athena Views are created to serve the QuickSight dashboards.

The main curated tables in the workshop include:

- **fact_events**: cleaned user behavior data.
- **dim_products**: product data serving as a dimension table.
- **fact_transactions**: valid transaction data after validation.

From these curated tables, the following main Athena Views are created:

- **vw_executive_overview**: analyzes revenue, order count, average order value, and refund rate.
- **vw_daily_event_funnel**: analyzes the funnel by day.
- **vw_funnel_summary**: prepares data for the funnel chart.
- **vw_daily_funnel_by_source_device**: analyzes the funnel by traffic source and device.
- **vw_traffic_source_performance**: evaluates the effectiveness of each traffic source.
- **vw_campaign_performance**: evaluates the effectiveness of marketing campaigns.
- **vw_product_revenue**: analyzes revenue by product, category, brand, and premium status.
- **vw_ab_testing_summary**: analyzes the effectiveness between experiment groups.
- **vw_discount_refund_analysis**: analyzes the relationship between discounts and refunds.

After the semantic layer is ready, **Amazon QuickSight** is used to build analytics dashboards.
- The Executive Overview dashboard helps monitor the overall business situation.
- The Funnel Analytics dashboard helps analyze the user journey from view to purchase.
- The Marketing Performance dashboard evaluates the effectiveness of traffic sources and campaigns.
- The Product Analytics dashboard focuses on revenue, sales volume, category effectiveness, brand, premium products, and refunds.
- The A/B Testing dashboard helps compare the effectiveness between experiment groups based on conversion rate, add-to-cart rate, bounce rate, and purchase trends.

### OVERALL ARCHITECTURE DIAGRAM

![Overall AWS E-commerce Analytics Data Pipeline](./images/overall-architecture.png)

The overall diagram of the project can be described with the following flow:

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

This workshop simulates a complete data pipeline following the Data Engineering approach. The pipeline includes all steps from storing raw data, cataloging metadata, validating data, ETL, error handling, optimizing storage formats, creating a semantic layer, building dashboards, automating scheduled runs, and error alerting. This is an important foundation in modern data analytics systems, particularly suitable for Data Engineer or AWS Data Engineer roles.
