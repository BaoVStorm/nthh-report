---

title: "Week 7 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
----------------------

## Week 7: Curated Data Catalog and Data Validation after ETL

**Time:** 13/04/2026 - 17/04/2026

### Week 7 Objectives:

* Check the output data after running the Glue ETL Job.
* Create a Glue Data Catalog for curated data.
* Create and run a Glue Crawler for Parquet data in the Curated Zone.
* Query and validate curated data using Athena.
* Check data quality after ETL before creating dashboards.

### Tasks to be carried out this week:

| Day       | Task                                                                                                                                                                                                                                                                   | Start Date | Completion Date | Reference Material                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------: | --------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monday    | - Check the output after the Glue ETL Job in S3.<br>- Check curated/fact_events, curated/dim_products, and curated/fact_transactions.<br>- Check error/transactions.<br>- Take notes on the output structure after ETL.                                                | 13/04/2026 |      13/04/2026 | [Organizing objects using prefixes - Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html)<br>[Organizing, listing, and working with objects - Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/organizing-objects.html)<br>[Using the Parquet format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html)                                                                                                                    |
| Tuesday   | - Create the Glue Database ecommerce_curated.<br>- Learn how a crawler reads Parquet data.<br>- Prepare the crawler configuration for the Curated Zone.<br>- Take notes on the role of the curated database.                                                           | 14/04/2026 |      14/04/2026 | [Using crawlers to populate the Data Catalog - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)<br>[Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)<br>[Using the Parquet format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html)<br>[Create tables using AWS Glue or the Athena console - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/creating-tables-how-to.html) |
| Wednesday | - Create crawler_ecommerce_curated for the S3 Curated Zone.<br>- Configure the S3 path, IAM Role, target database, and table prefix.<br>- Run the crawler and check its status.<br>- Take screenshots of the crawler configuration.                                    | 15/04/2026 |      15/04/2026 | [Using crawlers to populate the Data Catalog - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)<br>[Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)<br>[Use a crawler to add a table - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/schema-crawlers.html)                                                                                                                                                                      |
| Thursday  | - Check the curated_fact_events, curated_dim_products, and curated_fact_transactions tables.<br>- Check the schema, year/month/day partitions, and S3 location.<br>- Test query the curated tables using Athena.<br>- Take notes on the curated data crawling results. | 16/04/2026 |      16/04/2026 | [Query the AWS Glue Data Catalog - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html)<br>[Use AWS Glue Data Catalog to connect to your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)<br>[Partition your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)<br>[Managing partitions for ETL output in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-partitions.html)              |
| Friday    | - Validate curated data using Athena.<br>- Check row counts, null values, refund logic, and invalid transactions.<br>- Check that invalid negative revenue data has been removed from the curated layer.<br>- Write the Validate Curated Data section in the report.   | 17/04/2026 |      17/04/2026 | [SELECT - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/select.html)<br>[Functions in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/functions.html)<br>[Query the AWS Glue Data Catalog - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html)<br>[Partition your data - Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)                                                                                                                |

### Week 7 Achievements:

* Checked the output after ETL in S3.
* Successfully created the Glue Database ecommerce_curated.
* Successfully created and ran the Glue Crawler for the Curated Zone.
* Curated tables were created in the Glue Data Catalog.
* Checked the schema and partitions of the curated tables.
* Queried Parquet data using Athena.
* Validated important data conditions:

  * No null values remain in important columns in fact_transactions.
  * Transactions with negative gross_revenue that are not refunds have been removed from the curated layer.
* fact_events and fact_transactions are partitioned by year/month/day.
* Confirmed that the curated data is ready for building semantic views and dashboards.
