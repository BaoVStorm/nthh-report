---

title: "Week 12 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.12 </b> "
----------------------

## Week 12: End-to-End Testing, Workshop Finalization, and Report Writing

**Time:** 18/05/2026 - 29/05/2026

### Week 12 Objectives:

* Test the entire pipeline from raw data to dashboard.
* Review all technical implementation steps.
* Check dashboards, automation, monitoring, and alerts.
* Complete the internship/workshop report.
* Summarize the 12-week worklog and prepare the final version for submission.

### Tasks to be carried out this week:

| Time       | Task                                                                                                                                                                                                                                           | Start Date | Completion Date | Reference Material |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ------------------ |
| 18/05/2026 | - Retest the pipeline from the S3 Raw Zone to the Raw Glue Crawler.<br>- Check raw data in S3 and the Glue Catalog.<br>- Query raw tables again using Athena.<br>- Update illustrative images for the raw data section.                        | 18/05/2026 | 18/05/2026      |                    |
| 19/05/2026 | - Test the Glue ETL Job.<br>- Check the curated output and error zone.<br>- Read CloudWatch Logs to confirm that the job runs stably.<br>- Update the Glue ETL Job section in the report.                                                      | 19/05/2026 | 19/05/2026      |                    |
| 20/05/2026 | - Test the Curated Crawler and Athena Views.<br>- Query the views used for dashboards again.<br>- Check the logic for revenue, funnel, marketing, product, and A/B Testing.<br>- Update the Athena Views section in the report.                | 20/05/2026 | 20/05/2026      |                    |
| 21/05/2026 | - Check the Executive Overview and Funnel Analytics dashboards.<br>- Review the year/quarter/month filters.<br>- Check currency, percentage, and number formatting.<br>- Retake dashboard screenshots after finalizing them.                   | 21/05/2026 | 21/05/2026      |                    |
| 22/05/2026 | - Check the Marketing, Product, and A/B Testing dashboards.<br>- Review insights for each chart.<br>- Check the dashboard layout and publish the dashboards.<br>- Update the dashboard section in the report.                                  | 22/05/2026 | 22/05/2026      |                    |
| 25/05/2026 | - Recheck the Glue Workflow and EventBridge Scheduler.<br>- Confirm that the pipeline can run on schedule.<br>- Check the SNS email subscription and EventBridge alert rules.<br>- Update the automation/monitoring section in the report.     | 25/05/2026 | 25/05/2026      |                    |
| 26/05/2026 | - Write and revise the project overview section.<br>- Complete the problem statement, proposed solution, and architecture sections.<br>- Review the descriptions of the AWS services used.<br>- Edit the wording to make it more professional. | 26/05/2026 | 26/05/2026      |                    |
| 27/05/2026 | - Complete the technical implementation section.<br>- Review the S3, Glue, Athena, QuickSight, and EventBridge steps.<br>- Check the order of illustrative images.<br>- Add achieved results after each phase.                                 | 27/05/2026 | 27/05/2026      |                    |
| 28/05/2026 | - Review and edit the entire report.<br>- Add the risk, cost, expected outcomes, and future development sections.<br>- Standardize AWS service names throughout the document.                                                                  | 28/05/2026 | 28/05/2026      |                    |
| 29/05/2026 | - Complete the final report version.<br>- Summarize the 12-week worklog.<br>- Recheck the submission file, images, workshop content, and conclusion section.<br>- Prepare the final version for submission.                                    | 29/05/2026 | 29/05/2026      |                    |

### Week 12 Achievements:

* Retested the entire workshop pipeline from beginning to end:

  * Uploaded raw data to S3.
  * Crawled raw data using Glue Crawler.
  * Queried and validated raw data using Athena.
  * Ran the Glue ETL Job.
  * Wrote curated data in Parquet format.
  * Separated invalid data into the Error Zone.
  * Crawled curated data using Glue Crawler.
  * Created and checked Athena Views.
  * Connected QuickSight to Athena.
  * Built and tested dashboards.
  * Automated the pipeline using EventBridge Scheduler.
  * Configured error alerts using EventBridge Rules and SNS.
  * Reviewed and edited dashboards, including filters, number formatting, titles, and insights.
  * Rechecked the automation and monitoring sections to ensure that the pipeline can run automatically and send alerts when errors occur.
* Summarized the 12-week worklog.
* Completed the final report version for submission.
