---
title: "5.3. Create S3 Raw Zone"
linkTitle: "5.3. Create S3 Raw Zone"
menuTitle: "5.3. Create S3 Raw Zone"
date: 2026-05-29
weight: 530
chapter: false
---

The next step is to create the S3 Raw Zone and upload the 3 files with renamed columns to the correct prefixes.

### Create an S3 bucket:

Access the **AWS Management Console**. In the search bar, type S3, then select the **S3** service.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-001.png)

In the Amazon S3 console, select **Buckets**, then click **Create bucket** to start creating a new bucket.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-002.png)

#### Configure bucket details

In the Create bucket screen, configure the information as follows:

- Bucket namespace: select **Account Regional namespace**

- Bucket name prefix: enter the name **ecommerce-analytics-datalake**

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-003.png)

Then check the remaining settings before creating the bucket. Keep other settings at their default. Click **Create bucket**.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-004.png)

The bucket has been successfully created.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-005.png)

### Create folders in the S3 Bucket:

After successfully creating the bucket, access the newly created bucket. In the bucket interface, click **Create folder** to create a new folder.

Create the first folder with the following information:

- Folder name: **raw**

Click **Create folder** to complete.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-006.png)

Successfully created the folder **raw/**

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-007.png)

After successfully creating the raw/ folder, access this folder and continue to create the following subfolders: **events**, **products**, **transactions**.

Current directory tree:
```
raw/
raw/events/
raw/products/
raw/transactions/
curated/
curated/fact_events/
curated/dim_products/
curated/fact_transactions/
error/
error/events/
error/transactions/
athena-results/
```

Folder contents:

- **raw/**: used to store initial CSV data before processing with AWS Glue.

- **curated/**: contains data after being processed in Parquet format.

- **error/**: used to store erroneous data or ETL error output.

- **athena-results/**: the location where Athena stores query results.

### Upload data from local to S3

After creating the folder structure in S3, proceed to upload the CSV files processed on your local machine to their respective folders.

- Uploading **events.csv**: Access the path **raw/events/** in the bucket, click Upload to start uploading the file.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-008.png)

In the upload screen:

- Click **Add files**

- Select the file **events.csv** from your local machine

- Click **Upload**

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-009.png)

Once the upload is complete, check the **raw/events/** folder to ensure that the file events.csv has been successfully uploaded.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-010.png)

Do the same for the remaining files:

| File to upload | Corresponding S3 folder |
| --- | --- |
| products.csv | raw/products/ |
| transactions.csv | raw/transactions/ |

Once completed, the data structure in S3 will look like:

```
ecommerce-analytics-datalake/
└── raw/
    ├── events/
    │   └── events.csv
    ├── products/
    │   └── products.csv
    └── transactions/
        └── transactions.csv
```

At this step, raw data has been successfully uploaded to Amazon S3 and is ready to be used for the next steps such as creating the **Glue Crawler**, **Glue Data Catalog**, and ETL processing.
