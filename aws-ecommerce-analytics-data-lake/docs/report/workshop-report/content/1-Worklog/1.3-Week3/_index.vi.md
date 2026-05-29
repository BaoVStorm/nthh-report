---
title: "Worklog Tuần 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

## Tuần 3: Xác định đề tài workshop và khảo sát dữ liệu

**Thời gian:** 16/03/2026 - 20/03/2026

### Mục tiêu tuần 3:

* Tìm hiểu khái niệm Data Engineering, Data Lake và ETL pipeline.
* Xác định đề tài workshop phù hợp với định hướng AWS Data Analytics.
* Khảo sát bộ dữ liệu thương mại điện tử sử dụng cho project.
* Phân tích cấu trúc dữ liệu đầu vào gồm events, products và transactions.
* Thiết kế kiến trúc tổng quan cho workshop.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Tìm hiểu Data Engineering, Data Lake, ETL pipeline và batch processing.<br>- Tìm hiểu các khái niệm Raw Zone, Curated Zone, Error Zone.<br>- Xác định hướng đề tài phù hợp với AWS Data Analytics.<br>- Ghi chú các service có thể sử dụng trong workshop. | 16/03/2026 | 16/03/2026 | [What is Data Engineering? - AWS](https://aws.amazon.com/what-is/data-engineering/)<br>[What is a Data Lake? - AWS](https://aws.amazon.com/what-is/data-lake/)<br>[What is ETL? - AWS](https://aws.amazon.com/what-is/etl/)<br>[What is Batch Processing? - AWS](https://aws.amazon.com/what-is/batch-processing/)<br>[AWS Analytics Services](https://aws.amazon.com/big-data/datalakes-and-analytics/)<br>[Recommended data layers for data lakes - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/data-layer-definitions.html) |
| Thứ 3 | - Khảo sát dataset Marketing & E-commerce Analytics từ Kaggle.<br>- Kiểm tra các file dữ liệu gồm events.csv, products.csv, transactions.csv.<br>- Đọc schema, số lượng bản ghi, kiểu dữ liệu và ý nghĩa từng bảng.<br>- Ghi chú các vấn đề dữ liệu ban đầu. | 17/03/2026 | 17/03/2026 | [Marketing & E-Commerce Analytics Dataset - Kaggle](https://www.kaggle.com/datasets/geethasagarbonthu/marketing-and-e-commerce-analytics-dataset)<br>[Working with CSV files - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-csv-home.html) |
| Thứ 4 | - Phân tích bảng events: event_type, device_type, traffic_source, session_duration, experiment_group.<br>- Phân tích bảng products: category, brand, base_price, launch_date, is_premium.<br>- Phân tích bảng transactions: quantity, discount, gross_revenue, refund_flag.<br>- Xác định bảng fact và dimension cho project. | 18/03/2026 | 18/03/2026 | [Marketing & E-Commerce Analytics Dataset - Kaggle](https://www.kaggle.com/datasets/geethasagarbonthu/marketing-and-e-commerce-analytics-dataset) |
| Thứ 5 | - Xác định các vấn đề cần xử lý: null value, sai kiểu dữ liệu, traffic_source không đồng nhất, transaction lỗi.<br>- Đề xuất logic xử lý dữ liệu cho từng bảng.<br>- Phác thảo output gồm fact_events, dim_products, fact_transactions và error/transactions.<br>- Ghi chú phần data understanding cho report. | 19/03/2026 | 19/03/2026 |  |
| Thứ 6 | - Thiết kế kiến trúc tổng quan workshop.<br>- Xác định pipeline: Kaggle Dataset → Local Preprocessing → S3 → Glue → Athena → QuickSight → EventBridge/SNS.<br>- Vẽ/ghi lại luồng xử lý dữ liệu tổng thể.<br>- Viết phần mô tả đề tài và mục tiêu workshop. | 20/03/2026 | 20/03/2026 | [Guidance for Data Lakes on AWS](https://docs.aws.amazon.com/solutions/data-lakes-on-aws/)<br>[Building a Data Lake on AWS](https://pages.awscloud.com/rs/112-TZM-766/images/Building-a-data-lake-on-Amazon-Web-Services.pdf)<br>[AWS Analytics Services](https://aws.amazon.com/big-data/datalakes-and-analytics/)<br>[What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)<br>[What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)<br>[What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)<br>[What is Amazon QuickSight?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)<br>[What is Amazon EventBridge Scheduler?](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)<br>[What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) |

### Kết quả đạt được tuần 3:

* Xác định được đề tài workshop là E-commerce Analytics Data Lake on AWS.
* Hiểu được mục tiêu của workshop là xây dựng một pipeline phân tích dữ liệu thương mại điện tử theo hướng serverless trên AWS.
* Khảo sát được dataset gồm ba file chính:
  + events.csv
  + products.csv
  + transactions.csv
* Phân tích được ý nghĩa từng bảng dữ liệu:
  + events dùng để phân tích hành vi người dùng.
  + products dùng để lưu thông tin sản phẩm.
  + transactions dùng để phân tích giao dịch, doanh thu và refund.
* Xác định được các vấn đề dữ liệu cần xử lý như null value, sai kiểu dữ liệu, traffic_source không đồng nhất và transaction lỗi.
* Phác thảo được kiến trúc tổng quan của workshop gồm S3, Glue, Athena, QuickSight, EventBridge, SNS, CloudWatch và IAM.
