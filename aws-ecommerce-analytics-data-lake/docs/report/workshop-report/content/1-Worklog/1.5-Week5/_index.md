---

title: "Week 5 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
----------------------

## Week 5: Glue Data Catalog, Glue Crawler, and Athena Raw Validation

**Time:** 30/03/2026 - 03/04/2026

### Week 5 Objectives:

* Learn about AWS Glue Data Catalog and the role of metadata.
* Create a Glue Database for raw data.
* Create and run a Glue Crawler to automatically detect the schema of data in S3.
* Configure Amazon Athena to query data on S3.
* Validate raw data using basic SQL queries.

### Tasks to be carried out this week:

| Day       | Task                                                                                                                                                                                                                                                     | Start Date | Completion Date | Reference Material                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monday    | - Learn about AWS Glue Data Catalog, Glue Database, and Glue Table.<br>- Learn the role of metadata in querying data on S3.<br>- Create the Glue Database ecommerce_raw.<br>- Take notes on the Data Catalog concept for the report.                     | 30/03/2026 | 30/03/2026      | [Getting started with the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html)<br>[Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)<br>[Creating tables - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html) |
| Tuesday   | - Learn about Glue Crawler and how a crawler detects schemas.<br>- Create crawler_ecommerce_raw for the S3 Raw Zone.<br>- Configure the S3 data source, IAM Role, target database, and table prefix.<br>- Take screenshots of the crawler configuration. | 31/03/2026 | 31/03/2026      | [Using crawlers to populate the Data Catalog - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)<br>[Configuring a crawler - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/define-crawler.html)<br>[Customizing crawler behavior - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html)<br>[Step 2: Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html)                       |
| Wednesday | - Run the Raw Crawler.<br>- Check the crawler status after running.<br>- Check the raw_events, raw_products, and raw_transactions tables in the Glue Catalog.<br>- Check the schema of each table and record the results.                                | 01/04/2026 | 01/04/2026      | [Using crawlers to populate the Data Catalog - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)<br>[Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)<br>[Creating tables - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html)<br>[Query the AWS Glue Data Catalog - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html)              |
| Thursday  | - Configure the Athena query result location in S3.<br>- Test raw tables using SELECT LIMIT queries.<br>- Check displayed data, column names, data types, and header errors.<br>- Take screenshots of the query results.                                 | 02/04/2026 | 02/04/2026      | [Specify a query result location - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location.html)<br>[What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)<br>[SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)                           |
| Friday    | - Write SQL validation queries for raw data.<br>- Check event_type, category, quantity, null values, and abnormal values.<br>- Summarize the raw validation results.<br>- Write the Glue Crawler and Athena Raw Validation sections in the report.       | 03/04/2026 | 03/04/2026      | [SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Functions in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/functions.html)<br>[Considerations and limitations for SQL queries in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/other-notable-limitations.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)          |

### Week 5 Achievements:

* Understood that Glue Data Catalog stores metadata so Athena can query data in S3.
* Successfully created a Glue Database for raw data.
* Successfully created and ran a Glue Crawler for the S3 Raw Zone.
* Raw tables were created in the Glue Data Catalog.
* Successfully configured the Athena query result location in S3.
* Queried raw data using Athena and confirmed that the data could be read from S3 through the Glue Catalog.
* Wrote SQL queries to perform initial data validation.
* Checked null values and abnormal values.
* Completed the foundation needed to move on to building the ETL pipeline.
