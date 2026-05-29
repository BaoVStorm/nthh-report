---
title: "Worklog Tuần 11"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---

## Tuần 11: Automation và Monitoring

**Thời gian:** 11/05/2026 - 15/05/2026

### Mục tiêu tuần 11:

* Tự động hóa pipeline bằng AWS Glue Workflow và EventBridge Scheduler.
* Cấu hình pipeline chạy theo thứ tự Raw Crawler → ETL Job → Curated Crawler.
* Thiết lập cảnh báo lỗi bằng EventBridge Rules và SNS.
* Kiểm tra log và trạng thái pipeline bằng CloudWatch.
* Hoàn thiện phần automation và monitoring cho workshop.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Tìm hiểu Glue Workflow và trigger.<br>- Thiết kế thứ tự chạy pipeline: Raw Crawler → ETL Job → Curated Crawler.<br>- Tạo Glue Workflow cho project.<br>- Ghi chú vai trò của workflow trong automation. | 11/05/2026 | 11/05/2026 | [Overview of workflows in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html)<br>[AWS Glue triggers](https://docs.aws.amazon.com/glue/latest/dg/about-triggers.html) |
| Thứ 3 | - Tạo các trigger trong Glue Workflow.<br>- Cấu hình trigger start raw crawler.<br>- Cấu hình trigger chạy ETL sau khi raw crawler thành công.<br>- Cấu hình trigger chạy curated crawler sau khi ETL thành công. | 12/05/2026 | 12/05/2026 | [AWS Glue triggers](https://docs.aws.amazon.com/glue/latest/dg/about-triggers.html)<br>[Starting jobs and crawlers using triggers - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html)<br>[Triggers API - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html) |
| Thứ 4 | - Chạy thử Glue Workflow thủ công.<br>- Kiểm tra workflow history và từng node trong graph.<br>- Kiểm tra job run monitoring và CloudWatch Logs.<br>- Debug nếu workflow chưa chạy đúng thứ tự. | 13/05/2026 | 13/05/2026 | [AWS Glue job run statuses on the console](https://docs.aws.amazon.com/glue/latest/dg/view-job-runs.html)<br>[Monitoring AWS Glue using Amazon CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html)<br>[What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br>[Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) |
| Thứ 5 | - Tìm hiểu EventBridge Scheduler và cron expression.<br>- Tạo IAM Policy cho phép StartWorkflowRun.<br>- Tạo IAM Role cho EventBridge Scheduler.<br>- Tạo schedule tự động kích hoạt Glue Workflow. | 14/05/2026 | 14/05/2026 | [What is Amazon EventBridge Scheduler?](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)<br>[Schedule types in EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html)<br>[Amazon EventBridge Scheduler](https://docs.aws.amazon.com/eventbridge/latest/userguide/using-eventbridge-scheduler.html)<br>[StartWorkflowRun - AWS Glue API](https://docs.aws.amazon.com/glue/latest/webapi/API_StartWorkflowRun.html)<br>[Step 2: Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html) |
| Thứ 6 | - Tạo SNS Topic và email subscription.<br>- Tạo EventBridge Rules bắt lỗi Glue Crawler và Glue Job.<br>- Kiểm tra rule pattern cho FAILED, TIMEOUT, STOPPED.<br>- Viết phần Automation & Monitoring trong report. | 15/05/2026 | 15/05/2026 | [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)<br>[Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html)<br>[Creating a subscription to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html)<br>[Amazon SNS email subscription setup and management](https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html)<br>[AWS Glue events - Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-glue.html)<br>[Creating Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html)<br>[Automating AWS Glue with EventBridge](https://docs.aws.amazon.com/glue/latest/dg/automating-awsglue-with-cloudwatch-events.html) |

### Kết quả đạt được tuần 11:

* Hiểu được vai trò của Glue Workflow trong việc điều phối các bước pipeline.
* Tạo được Glue Workflow cho project.
* Cấu hình được các trigger trong workflow:
  + Trigger chạy Raw Crawler.
  + Trigger chạy Glue ETL Job sau khi Raw Crawler thành công.
  + Trigger chạy Curated Crawler sau khi ETL Job thành công.
* Chạy thử workflow thủ công và kiểm tra được workflow history.
* Tạo được EventBridge Scheduler để tự động kích hoạt Glue Workflow theo lịch.
* Tạo được IAM Role cho EventBridge Scheduler với quyền gọi StartWorkflowRun.
* Tạo được SNS Topic và email subscription để nhận thông báo.
* Tạo được EventBridge Rules để bắt lỗi Glue Job và Glue Crawler.
* Biết cách kiểm tra lỗi pipeline thông qua CloudWatch Logs, Glue Job Run Monitoring và Workflow History.
