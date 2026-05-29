---
title: "5.18.6. Create EventBridge Failure Alert Rules"
linkTitle: "5.18.6. Create EventBridge Failure Alert Rules"
menuTitle: "5.18.6. Create EventBridge Failure Alert Rules"
date: 2026-05-29
weight: 686
chapter: false
---

# 5.18.6. Create EventBridge Failure Alert Rules

This page creates EventBridge rules that detect Glue crawler and Glue job failures and send notifications through SNS.

## What This Page Covers
- Create an EventBridge rule for raw and curated crawler failure events.
- Set the SNS topic as the rule target.
- Create an EventBridge rule for Glue ETL job failure events.
- Set the same SNS topic as the notification target.
- Use the alerts to detect pipeline failures without checking the console manually.

## Reference Commands and Queries

The SQL, JSON, or command snippets used in the Vietnamese walkthrough are kept below for the English version.

```json
{
"source": ["aws.glue"],
"detail-type": ["Glue Crawler State Change"],
"detail": {
"crawlerName": [
"crawler_ecommerce_raw",
"crawler_ecommerce_curated"
],
"state": ["Failed"]
}
}
```

```sql
Select a target: SNS Topic
```

```json
{
"source": ["aws.glue"],
"detail-type": ["Glue Job State Change"],
"detail": {
"jobName": ["etl_ecommerce_raw_to_curated_1"],
"state": ["FAILED", "TIMEOUT", "STOPPED"]
}
}
```

## Screenshots

The following screenshots match the implementation steps in this page.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-001.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-002.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-003.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-004.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-005.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-006.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-007.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-008.png)

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-009.png)
