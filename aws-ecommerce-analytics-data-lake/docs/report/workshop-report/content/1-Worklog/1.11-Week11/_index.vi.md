---
title: "Worklog Tuần 11"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---

## Worklog Tuần 11: Automation và Monitoring

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
| Thứ 2 | - Tìm hiểu Glue Workflow và trigger.<br>- Thiết kế thứ tự chạy pipeline: Raw Crawler → ETL Job → Curated Crawler.<br>- Tạo Glue Workflow cho project.<br>- Ghi chú vai trò của workflow trong automation. | 11/05/2026 | 11/05/2026 | AWS Glue Workflow Documentation |
| Thứ 3 | - Tạo các trigger trong Glue Workflow.<br>- Cấu hình trigger start raw crawler.<br>- Cấu hình trigger chạy ETL sau khi raw crawler thành công.<br>- Cấu hình trigger chạy curated crawler sau khi ETL thành công. | 12/05/2026 | 12/05/2026 | AWS Glue Console |
| Thứ 4 | - Chạy thử Glue Workflow thủ công.<br>- Kiểm tra workflow history và từng node trong graph.<br>- Kiểm tra job run monitoring và CloudWatch Logs.<br>- Debug nếu workflow chưa chạy đúng thứ tự. | 13/05/2026 | 13/05/2026 | AWS Glue, CloudWatch |
| Thứ 5 | - Tìm hiểu EventBridge Scheduler và cron expression.<br>- Tạo IAM Policy cho phép StartWorkflowRun.<br>- Tạo IAM Role cho EventBridge Scheduler.<br>- Tạo schedule tự động kích hoạt Glue Workflow. | 14/05/2026 | 14/05/2026 | EventBridge Scheduler |
| Thứ 6 | - Tạo SNS Topic và email subscription.<br>- Tạo EventBridge Rules bắt lỗi Glue Crawler và Glue Job.<br>- Kiểm tra rule pattern cho FAILED, TIMEOUT, STOPPED.<br>- Viết phần Automation & Monitoring trong report. | 15/05/2026 | 15/05/2026 | SNS, EventBridge, CloudWatch |

### Kết quả đạt được tuần 11:

* Hiểu được vai trò của Glue Workflow trong việc điều phối các bước pipeline.
* Tạo được Glue Workflow cho project.
* Cấu hình được các trigger trong workflow:
* Trigger chạy Raw Crawler.
* Trigger chạy Glue ETL Job sau khi Raw Crawler thành công.
* Trigger chạy Curated Crawler sau khi ETL Job thành công.
* Chạy thử workflow thủ công và kiểm tra được workflow history.
* Tạo được EventBridge Scheduler để tự động kích hoạt Glue Workflow theo lịch.
* Tạo được IAM Role cho EventBridge Scheduler với quyền gọi StartWorkflowRun.
* Tạo được SNS Topic và email subscription để nhận thông báo.
* Tạo được EventBridge Rules để bắt lỗi Glue Job và Glue Crawler.
* Biết cách kiểm tra lỗi pipeline thông qua CloudWatch Logs, Glue Job Run Monitoring và Workflow History.
