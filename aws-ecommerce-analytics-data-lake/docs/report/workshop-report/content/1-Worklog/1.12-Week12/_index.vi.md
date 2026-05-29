---
title: "Worklog Tuần 12"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.12 </b> "
---

## Worklog Tuần 12: Kiểm thử tổng thể, hoàn thiện workshop và viết report

**Thời gian:** 18/05/2026 - 29/05/2026

### Mục tiêu tuần 12:

* Kiểm thử toàn bộ pipeline từ raw data đến dashboard.
* Rà soát lại các bước triển khai kỹ thuật.
* Kiểm tra dashboard, automation, monitoring và alert.
* Hoàn thiện báo cáo thực tập/workshop.
* Tổng hợp worklog 12 tuần và chuẩn bị bản cuối cùng để nộp.

### Các công việc cần triển khai trong tuần này:

| Thời gian | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 18/05/2026 | - Kiểm thử lại pipeline từ S3 Raw Zone đến Glue Crawler Raw.<br>- Kiểm tra dữ liệu raw trong S3 và Glue Catalog.<br>- Query lại raw tables bằng Athena.<br>- Cập nhật hình ảnh minh họa cho phần raw data. | 18/05/2026 | 18/05/2026 | AWS Console, Athena |
| 19/05/2026 | - Kiểm thử Glue ETL Job.<br>- Kiểm tra output curated và error zone.<br>- Đọc CloudWatch Logs để xác nhận job chạy ổn định.<br>- Cập nhật phần Glue ETL Job trong report. | 19/05/2026 | 19/05/2026 | AWS Glue, CloudWatch |
| 20/05/2026 | - Kiểm thử Curated Crawler và Athena Views.<br>- Query lại các view phục vụ dashboard.<br>- Kiểm tra logic revenue, funnel, marketing, product và A/B Testing.<br>- Cập nhật phần Athena Views trong report. | 20/05/2026 | 20/05/2026 | Athena |
| 21/05/2026 | - Kiểm tra Dashboard Executive Overview và Funnel Analytics.<br>- Rà soát filter year/quarter/month.<br>- Kiểm tra format currency, percent, number.<br>- Chụp lại hình dashboard sau khi hoàn thiện. | 21/05/2026 | 21/05/2026 | QuickSight |
| 22/05/2026 | - Kiểm tra Dashboard Marketing, Product và A/B Testing.<br>- Rà soát insight cho từng biểu đồ.<br>- Kiểm tra layout dashboard và publish dashboard.<br>- Cập nhật phần dashboard trong report. | 22/05/2026 | 22/05/2026 | QuickSight |
| 25/05/2026 | - Kiểm tra lại Glue Workflow và EventBridge Scheduler.<br>- Xác nhận pipeline có thể chạy theo lịch.<br>- Kiểm tra SNS email subscription và EventBridge alert rule.<br>- Cập nhật phần automation/monitoring trong report. | 25/05/2026 | 25/05/2026 | EventBridge, SNS |
| 26/05/2026 | - Viết và chỉnh sửa phần tổng quan đề tài.<br>- Hoàn thiện phần problem statement, proposed solution và architecture.<br>- Rà soát mô tả các AWS services sử dụng.<br>- Chỉnh sửa câu chữ cho chuyên nghiệp hơn. | 26/05/2026 | 26/05/2026 | Report Draft |
| 27/05/2026 | - Hoàn thiện phần triển khai kỹ thuật.<br>- Rà soát các bước S3, Glue, Athena, QuickSight, EventBridge.<br>- Kiểm tra thứ tự hình ảnh minh họa.<br>- Bổ sung kết quả đạt được sau từng giai đoạn. | 27/05/2026 | 27/05/2026 | Report Draft |
| 28/05/2026 | - Kiểm tra và chỉnh sửa toàn bộ report.<br>- Bổ sung phần rủi ro, chi phí, kết quả kỳ vọng và hướng phát triển.<br>- Chuẩn hóa tên service AWS trong toàn bộ tài liệu. | 28/05/2026 | 28/05/2026 | Report Draft |
| 29/05/2026 | - Hoàn thiện bản báo cáo cuối cùng.<br>- Tổng hợp worklog 12 tuần.<br>- Kiểm tra lại file nộp, hình ảnh, nội dung workshop và phần kết luận.<br>- Chuẩn bị bản cuối để nộp. | 29/05/2026 | 29/05/2026 | Final Report |

### Kết quả đạt được tuần 12:

* Kiểm thử lại toàn bộ pipeline workshop từ đầu đến cuối:
* Upload dữ liệu raw lên S3.
* Crawl raw data bằng Glue Crawler.
* Query và validate raw data bằng Athena.
* Chạy Glue ETL Job.
* Ghi dữ liệu curated dạng Parquet.
* Tách dữ liệu lỗi sang Error Zone.
* Crawl curated data bằng Glue Crawler.
* Tạo và kiểm tra Athena Views.
* Kết nối QuickSight với Athena.
* Xây dựng và kiểm tra dashboard.
* Tự động hóa pipeline bằng EventBridge Scheduler.
* Cấu hình cảnh báo lỗi bằng EventBridge Rules và SNS.
* Rà soát và chỉnh sửa các dashboard về filter, format số liệu, tiêu đề và insight.
* Kiểm tra lại phần automation và monitoring để đảm bảo pipeline có thể chạy tự động và có cảnh báo khi lỗi.
* Tổng hợp worklog 12 tuần.
* Hoàn thiện bản báo cáo cuối cùng để nộp.
