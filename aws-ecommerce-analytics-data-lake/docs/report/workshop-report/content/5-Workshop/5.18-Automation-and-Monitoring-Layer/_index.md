---
title: "5.18. Automation & Monitoring Layer"
linkTitle: "5.18. Automation & Monitoring Layer"
menuTitle: "5.18. Automation & Monitoring Layer"
date: 2026-05-29
weight: 680
chapter: false
---

# 5.18. Automation & Monitoring Layer

After the pipeline has successfully run manually, the next step is to automate and monitor the pipeline.

Automation and monitoring architecture:

EventBridge Scheduler

→ StartWorkflowRun

→ Glue Workflow

→ Raw Crawler

→ Glue ETL Job

→ Curated Crawler

→ EventBridge Rules for failure detection

→ SNS Email Notification

Monitoring Layer Description

The monitoring layer is used to track the pipeline execution and alert when errors occur.

SNS Email Notification

SNS is used to send alert emails when an alarm is triggered.

Example:

Glue Job Failed → EventBridge Rule → SNS → Email Notification
