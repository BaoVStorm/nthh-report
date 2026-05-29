---
title: "5.18. Automation & Monitoring Layer"
linkTitle: "5.18. Automation & Monitoring Layer"
menuTitle: "5.18. Automation & Monitoring Layer"
date: 2026-05-29
weight: 680
chapter: false
---

# 5.18. Automation & Monitoring Layer

Sau khi pipeline đã chạy thủ công thành công, bước tiếp theo là tự động hóa và giám sát pipeline.

Kiến trúc automation và monitoring:

EventBridge Scheduler

→ StartWorkflowRun

→ Glue Workflow

→ Raw Crawler

→ Glue ETL Job

→ Curated Crawler

→ EventBridge Rules for failure detection

→ SNS Email Notification

Mô tả Monitoring Layer

Monitoring layer dùng để theo dõi quá trình chạy pipeline và cảnh báo khi có lỗi.

SNS Email Notification

SNS dùng để gửi email cảnh báo khi alarm được kích hoạt.

Ví dụ:

Glue Job Failed → EventBridge Rule → SNS → Email Notification
