---
title: "5.11. Connect QuickSight to Athena"
linkTitle: "5.11. Connect QuickSight to Athena"
menuTitle: "5.11. Connect QuickSight to Athena"
date: 2026-05-29
weight: 610
chapter: false
---

After creating the Athena Views, the next step is to connect **Amazon QuickSight** with **Athena** to create datasets and build dashboards.

QuickSight will retrieve data from the **ecommerce_curated** database and use the views created in the previous step as the main datasets.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-001.png)

Next, select **Sign up for Amazon QuickSight**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-002.png)

### Check the QuickSight Region

Before connecting QuickSight to Athena, you need to verify the **Region** being used.

{{% notice note %}}
QuickSight, Athena, Glue Data Catalog, and the S3 bucket should be configured in the same Region to avoid data access errors.
{{% /notice %}}

In this workshop, the S3 bucket and Athena are in Region **ap-southeast-1**, so QuickSight must also be switched to the same Region.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-003.png)

### Configure access permissions in QuickSight

In QuickSight, go to **Manage Account**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-004.png)

Then click on **AWS resources** to check the access permissions to AWS services.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-005.png)

Select the **S3 bucket** service to add the project's bucket to the list of buckets QuickSight is allowed to access.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-006.png)

In the S3 bucket selection section, select the project's bucket, tick **Write permission for Athena Workgroup**.

Then click **Finish**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-007.png)

Ensure that QuickSight has access to:

- Amazon Athena

- The Amazon S3 bucket containing the project data

- The Glue Data Catalog through Athena

Then click **Next**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-008.png)

### Create a dataset from Athena

In the QuickSight interface, select **Datasets** → **Create dataset**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-009.png)

On the Create dataset screen, click **Create data source**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-010.png)

Select the data source **Amazon Athena**.

Then click **Next**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-011.png)

On the **Athena data source** creation screen, enter:

- Data source name: **ecommerce_curated**

Click **Validate connection** to test the connection.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-012.png)

If the connection is successful, QuickSight will display a message that SSL is enabled or the connection is valid.

Then click **Create data source**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-013.png)

### Select the database and view

After creating the data source, QuickSight will display a list of databases and tables/views from Athena.

Configure as follows:

- Database: **ecommerce_curated**

- Table/View: **vw_executive_overview**

After selecting the view, click **Select**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-014.png)

### Complete dataset creation

At the **Finish dataset creation** step, select **Directly query your data**, then click **Visualize**.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-015.png)

The reason for selecting **Directly query your data**:

- Data in Athena has already been processed at the curated layer

- Datasets are easy to update when data changes

After clicking Visualize, QuickSight will open the analysis/dashboard creation interface.

Click **Create** to create the dashboard.

![](/images/5-Workshop/5.11-Ket-noi-QuickSight-voi-Athena/image-016.png)
