---
title: "5.19. Cleanup Resources"
linkTitle: "5.19. Cleanup Resources"
menuTitle: "5.19. Cleanup Resources"
date: 2026-05-29
weight: 690
chapter: false
---
After completing the workshop and saving all screenshots, dashboards, workflow results, and report content, you should clean up the AWS resources that were created to avoid unnecessary costs.

#### I. EventBridge Scheduler

Go to: **Amazon EventBridge Console**

Delete Schedule: `schedule-ecommerce-glue-workflow`

Steps:

1. Go to **Amazon EventBridge**.
2. Select **Scheduler** → **Schedules**.
3. Select the schedule `schedule-ecommerce-glue-workflow`.
4. Choose **Delete** if it is no longer needed.
5. Confirm the schedule deletion.

This schedule was previously used to call the Glue API `StartWorkflowRun` and automatically run the workflow on a schedule.

#### II. EventBridge Rules

Go to: **Amazon EventBridge Console**

Delete Rules: `alert-ecommerce-crawler-failed` and `alert-ecommerce-glue-job-failed`

Steps:

1. Go to **Amazon EventBridge**.
2. Select **Rules**.
3. Select the rule `alert-ecommerce-crawler-failed`.
4. Choose **Delete**.
5. Repeat the same steps for the rule `alert-ecommerce-glue-job-failed`.

These rules were used to capture Glue Crawler or Glue ETL Job failures and send alerts to SNS.

#### III. SNS Topic

Go to: **Amazon SNS Console**

Delete Topic: `ecommerce-etl-alerts`

Steps:

1. Go to **Amazon SNS**.
2. Select **Topics**.
3. Select the topic `ecommerce-etl-alerts`.
4. Choose **Delete**.
5. Confirm the topic deletion.

This SNS topic was used to send email notifications when the pipeline encountered errors. When the topic is deleted, the related email subscriptions will no longer be used.

#### IV. Glue Workflow

Go to: **AWS Glue Console**

Delete Workflow: `ecommerce-scheduled-etl-workflow`

Steps:

1. Go to **AWS Glue**.
2. Select **ETL** → **Workflows**.
3. Select the workflow `ecommerce-scheduled-etl-workflow`.
4. Choose **Actions** → **Delete**.
5. Confirm the workflow deletion.

***Note:*** Deleting the workflow only removes the orchestration component. Glue Crawlers and the Glue ETL Job still need to be deleted separately.

#### V. Glue Crawlers

Go to: **AWS Glue Console**

Delete Crawlers: `crawler_ecommerce_raw` and `crawler_ecommerce_curated`

Steps:

1. Go to **AWS Glue**.
2. Select **Data Catalog** → **Crawlers**.
3. Select the crawler `crawler_ecommerce_raw`.
4. Choose **Actions** → **Delete crawler**.
5. Repeat the same steps for the crawler `crawler_ecommerce_curated`.

#### VI. Glue ETL Job

Go to: **AWS Glue Console**

Delete Job: `etl_ecommerce_raw_to_curated_1`

Steps:

1. Go to **AWS Glue**.
2. Select **ETL jobs**.
3. Select the job `etl_ecommerce_raw_to_curated_1`.
4. Choose **Actions** → **Delete**.
5. Confirm the job deletion.

#### VII. Glue Databases

Go to: **AWS Glue Console**

Delete Databases: `ecommerce_raw` and `ecommerce_curated`

Steps:

1. Go to **AWS Glue**.
2. Select **Data Catalog** → **Databases**.
3. Select the database `ecommerce_raw`.
4. Choose **Delete**.
5. Repeat the same steps for the database `ecommerce_curated`.

***Note:*** Deleting a Glue Database only removes the metadata in the Glue Data Catalog. It does not delete the actual data stored in Amazon S3.

#### VIII. Athena Query Results

Go to: **Amazon S3 Console**

Delete Athena results folder: `s3://ecommerce-analytics-datalake-270642943130-ap-southeast-1-an/athena-results/`

Steps:

1. Go to **Amazon S3**.
2. Select the bucket: `ecommerce-analytics-datalake-270642943130-ap-southeast-1-an`
3. Select the folder `athena-results/`.
4. Choose **Delete**.
5. Confirm the deletion of query results that are no longer needed.

#### IX. QuickSight Dashboards

Go to: **Amazon QuickSight Console**

Delete Dashboards: Executive Overview, Funnel Analytics, Marketing Performance, Product Analytics, A/B Testing.

Steps:

1. Go to **Amazon QuickSight**.
2. Select **Dashboards**.
3. Select each published dashboard.
4. Choose **Delete**.
5. Confirm the dashboard deletion.

#### X. QuickSight Analyses

Go to: **Amazon QuickSight Console**

Delete Analyses: Executive Overview Analysis, Funnel Analytics Analysis, Marketing Performance Analysis, Product Analytics Analysis, A/B Testing Analysis.

Steps:

1. Go to **Amazon QuickSight**.
2. Select **Analyses**.
3. Select the analyses corresponding to the dashboards created.
4. Choose **Delete**.
5. Confirm the analysis deletion.

#### XI. QuickSight Datasets

Go to: **Amazon QuickSight Console**

Delete Datasets created from Athena views.

Steps:

1. Go to **Amazon QuickSight**.
2. Select **Datasets**.
3. Select the dataset created from Athena.
4. Choose **Delete**.
5. Confirm the dataset deletion.

#### XII. CloudWatch Logs

Go to: **Amazon CloudWatch Console**

Delete Glue log groups if they are no longer needed: `/aws-glue/jobs/output` and `/aws-glue/jobs/error`

Steps:

1. Go to **Amazon CloudWatch**.
2. Select **Logs** → **Log groups**.
3. Search for log groups related to AWS Glue.
4. Select the log group that is no longer needed.
5. Choose **Delete log group**.
6. Confirm the deletion.

#### XIII. S3 Data Lake Bucket

Go to: **Amazon S3 Console**

Delete Bucket: `ecommerce-analytics-datalake-270642943130-ap-southeast-1-an`

Before deleting the bucket, you must empty the bucket.

Folders to check:

```
raw/
curated/
error/
athena-results/
```

Steps:

1. Go to **Amazon S3**.
2. Select the bucket `ecommerce-analytics-datalake-270642943130-ap-southeast-1-an`.
3. Delete the folders or objects inside the bucket:

   * `raw/`
   * `curated/`
   * `error/`
   * `athena-results/`
4. After the bucket is empty, return to the bucket list.
5. Select the bucket.
6. Choose **Delete**.
7. Enter the bucket name to confirm.
8. Choose **Delete bucket**.

#### XIV. IAM Role for EventBridge Scheduler

Go to: **IAM Console**

Delete Role: `EventBridgeSchedulerStartGlueWorkflowRole`

Steps:

1. Go to **IAM**.
2. Select **Roles**.
3. Search for the role `EventBridgeSchedulerStartGlueWorkflowRole`.
4. Make sure the role is no longer being used by EventBridge Scheduler.
5. Choose **Delete**.
6. Confirm the role deletion.

#### XV. IAM Policy for EventBridge Scheduler

Go to: **IAM Console**

Delete Policy: `AllowStartGlueWorkflow`

Steps:

1. Go to **IAM**.
2. Select **Policies**.
3. Search for the policy `AllowStartGlueWorkflow`.
4. Make sure the policy is no longer attached to any role.
5. Choose **Delete**.
6. Confirm the policy deletion.

#### XVI. IAM Role for AWS Glue

Go to: **IAM Console**

Check Role: `AWSGlueServiceRoleDefault`

Steps:

1. Go to **IAM**.
2. Select **Roles**.
3. Search for the role `AWSGlueServiceRoleDefault`.
4. Delete this role only if you are sure it was created only for the workshop and is no longer used by any Glue Job or Crawler.
5. If you are not sure, keep the role to avoid affecting other projects.

***Note:*** Do not delete AWS managed policies such as `AWSGlueServiceRole` or `AmazonS3FullAccess`. If cleanup is needed, only detach them from the role or delete the custom role created for the workshop.

#### Conclusion

The cleanup step helps prevent unnecessary costs after completing the workshop. In this project, the resources that need to be checked and deleted include EventBridge Scheduler, EventBridge Rules, SNS Topic, Glue Workflow, Glue Crawlers, Glue ETL Job, Glue Databases, QuickSight dashboards, Athena results, CloudWatch Logs, S3 bucket, and related IAM roles/policies.

After the cleanup is complete, check AWS Billing again to ensure that no resources are still generating unexpected costs.
