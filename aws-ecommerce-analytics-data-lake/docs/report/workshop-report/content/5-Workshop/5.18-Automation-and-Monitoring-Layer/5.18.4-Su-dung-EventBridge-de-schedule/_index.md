---
title: "5.18.4. Use EventBridge Scheduler"
linkTitle: "5.18.4. Use EventBridge Scheduler"
menuTitle: "5.18.4. Use EventBridge Scheduler"
date: 2026-05-29
weight: 684
chapter: false
---

# 5.18.4. Use EventBridge Scheduler

This page schedules the Glue Workflow so the data pipeline can run automatically.

## What This Page Covers
- Create an IAM policy and role that allow EventBridge Scheduler to start the Glue Workflow.
- Create a new EventBridge schedule.
- Choose the Glue StartWorkflowRun target.
- Provide the target input and schedule settings.
- Confirm that the schedule can trigger the workflow at the configured time.

## Reference Commands and Queries

The SQL, JSON, or command snippets used in the Vietnamese walkthrough are kept below for the English version.

```json
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "AllowStartGlueWorkflow",
"Effect": "Allow",
"Action": "glue:StartWorkflowRun",
"Resource": "arn:aws:glue:ap-southeast-1:270642943130:workflow/ecommerce-scheduled-etl-workflow"
}
]
}
```

```json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Service": "scheduler.amazonaws.com"
},
"Action": "sts:AssumeRole"
}
]
}
```

```json
{
"Name": "ecommerce-scheduled-etl-workflow"
}
```

```sql
Select an existing role: EventBridgeSchedulerStartGlueWorkflowRole
```

## Screenshots

The following screenshots match the implementation steps in this page.

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-001.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-002.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-003.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-004.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-005.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-006.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-007.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-008.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-009.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-010.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-011.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-012.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-013.png)

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-014.png)
