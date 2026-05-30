---

title: "Week 4 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
----------------------

## Week 4: Building the S3 Data Lake and Preparing Raw Data

**Time:** 23/03/2026 - 27/03/2026

### Week 4 Objectives:

* Design the S3 Data Lake structure for the project.
* Create an S3 bucket and organize data folders by zone.
* Perform local preprocessing for the dataset.
* Upload raw data to Amazon S3.
* Create the necessary IAM Role so that AWS Glue can access data in S3.

### Tasks to be carried out this week:

| Day       | Task                                                                                                                                                                                                                                                                 | Start Date | Completion Date | Reference Material                                                                                                                                                                                                                                                                                                                     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monday    | - Learn about S3 Data Lake design.<br>- Plan the folder structure for raw, curated, error, and athena-results.<br>- Define naming conventions for the bucket and prefixes.<br>- Take notes on the role of each zone in the data lake.                                | 23/03/2026 | 23/03/2026      |                                                                                                                                                                                                                                                                                                                                        |
| Tuesday   | - Create an S3 bucket for the project.<br>- Create folders raw/events, raw/products, and raw/transactions.<br>- Create curated, error, and athena-results folders.<br>- Take screenshots of the bucket structure to include in the report.                           | 24/03/2026 | 24/03/2026      |                                                                                                                                                                                                                                                                                                                                        |
| Wednesday | - Perform local preprocessing for the dataset.<br>- Rename timestamp to event_timestamp and transaction_timestamp.<br>- Check headers, encoding, row counts, and data format.<br>- Take notes on the local preprocessing steps in the report.                        | 25/03/2026 | 25/03/2026      |                                                                                                                                                                                                                                                                                                                                        |
| Thursday  | - Upload events.csv, products.csv, and transactions.csv to the correct S3 prefixes.<br>- Check the uploaded files in each folder.<br>- Check the S3 URI path of each dataset.<br>- Take screenshots to illustrate the data upload process.                           | 26/03/2026 | 26/03/2026      |                                                                                                                                                                                                                                                                                                                                        |
| Friday    | - Create an IAM Role for AWS Glue.<br>- Learn about the permissions required for Glue to access S3 and the Data Catalog.<br>- Attach suitable policies for the workshop environment.<br>- Take notes on least privilege considerations for a production environment. | 27/03/2026 | 27/03/2026      | [Setting up IAM permissions for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/set-up-iam.html)<br>[Step 2: Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html)<br>[How AWS Glue works with IAM](https://docs.aws.amazon.com/glue/latest/dg/security_iam_service-with-iam.html) |

### Week 4 Achievements:

* Successfully created an S3 bucket for the workshop project.
* Designed the data lake structure, including:

  * raw/
  * curated/
  * error/
  * athena-results/
* Organized raw data by domain:

  * raw/events/
  * raw/products/
  * raw/transactions/
* Performed local preprocessing for the data, including renaming the timestamp columns to make ETL processing easier.
* Successfully uploaded the CSV files to the correct folders in the S3 Raw Zone.
* Created an IAM Role for AWS Glue with access to S3 and the Glue Data Catalog.
* Understood the role of S3 as the central data lake for the entire pipeline.
