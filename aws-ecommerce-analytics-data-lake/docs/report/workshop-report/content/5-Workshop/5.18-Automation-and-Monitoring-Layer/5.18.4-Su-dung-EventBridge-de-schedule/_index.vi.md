---
title: "5.18.4. Sử dụng EventBridge để schedule"
linkTitle: "5.18.4. Sử dụng EventBridge để schedule"
menuTitle: "5.18.4. Sử dụng EventBridge để schedule"
date: 2026-05-29
weight: 684
chapter: false
---

# 5.18.4. Sử dụng EventBridge để schedule

EventBridge Scheduler chịu trách nhiệm chạy workflow theo lịch, còn Glue Workflow chịu trách nhiệm điều phối thứ tự chạy Raw Crawler → ETL Job → Curated Crawler.

#### Tạo IAM Policy

Vào IAM -> Policies -> Create policy

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-001.png)

- Chọn tab JSON

- Dán policy này:

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

Nhấn Next.

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-002.png)

- Policy name: AllowStartGlueWorkflow

Sau đó nhấn Create policy

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-003.png)

#### Tạo IAM role cho EventBridge Scheduler

TẠO ROLE:

IAM → Roles → Create role

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-004.png)

Ở Trusted entity type, chọn Custom trust policy, dán policy dưới đây vào

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

EventBridge Scheduler cần execution role để assume role và gọi target service thay cho con người nên Trust principal phải là scheduler.amazonaws.com.

Rồi nhấn Next.

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-005.png)

ATTACH POLICY

Ở bước Add permissions, tìm và chọn policy AllowStartGlueWorkflow.

Sau đó nhấn Next.

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-006.png)

- Đặt role name EventBridgeSchedulerStartGlueWorkflowRole

Kiểm tra lại các thông tin, sau đó nhấn Create role.

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-007.png)

#### Tạo EventBridge Schedule

Truy cập AWS Management Console, tìm kiếm và chọn dịch vụ Amazon EventBridge

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-008.png)

Trong menu bên trái chọn Schedules, sau đó nhấn Create schedule

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-009.png)

Trong bước Specify schedule detail, cấu hình:

- Schedule name: schedule-ecommerce-glue-workflow

- Schedule pattern: Recurring schedule

- Time zone: Asia/Saigon

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-010.png)

- Schedule type: Cron-based schedule

- Cron expression: cron(0 09 * * ? *)

- Flexible time window: OFF

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-011.png)

EventBridge Scheduler hỗ trợ recurring schedule bằng cron/rate expression và cũng hỗ trợ timezone trong schedule.

#### Chọn target

Ở bước Select target, cấu hình như sau:

- Target API: All APIs

- Chọn service: AWS Glue

- Chọn API: StartWorkflowRun

- Ở ô input dán script JSON:

```json
{
"Name": "ecommerce-scheduled-etl-workflow"
}
```

Sau đó nhấn Next

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-012.png)

#### Settings

- Enable schedule: Enable

- Action after schedule completion: NONE

- Execution role:  Use existing role

```sql
Select an existing role: EventBridgeSchedulerStartGlueWorkflowRole
```

Sau đó nhấn Next

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-013.png)

Sau đó Review lại và nhấn Create schedule. Schedule đã được tạo thành công.

![](/images/5-Workshop/5.18.4-Su-dung-EventBridge-de-schedule/image-014.png)
