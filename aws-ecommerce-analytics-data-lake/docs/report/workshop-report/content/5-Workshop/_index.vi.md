---
title: "WORKSHOP XÂY DỰNG E-COMMERCE ANALYTICS DATA LAKE TRÊN AWS THEO HƯỚNG SERVERLESS"
linkTitle: "Workshop"
menuTitle: "Workshop"
date: 2026-05-29
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Tổng quan

- **Data Lake** là kiến trúc lưu trữ dữ liệu tập trung, cho phép lưu dữ liệu ở nhiều định dạng khác nhau như CSV, JSON, Parquet hoặc log file. Trong workshop này, **Amazon S3** được sử dụng làm Data Lake để lưu trữ dữ liệu thương mại điện tử theo nhiều tầng: **Raw Zone**, **Curated Zone**, **Error Zone** và **Athena Results**.

- **Serverless Data Analytics** trên AWS là cách xây dựng pipeline phân tích dữ liệu mà không cần quản lý server trực tiếp. Các dịch vụ như Amazon S3, AWS Glue, Amazon Athena, Amazon QuickSight, EventBridge và SNS giúp tự động hóa quá trình lưu trữ, xử lý, truy vấn, trực quan hóa và giám sát dữ liệu.

- **AWS Glue** là dịch vụ ETL serverless của AWS, được sử dụng để crawl metadata, tạo Data Catalog và xử lý dữ liệu bằng PySpark. Trong project này, AWS Glue được dùng cho ba nhiệm vụ chính:

  + **Glue Crawler**: tự động quét dữ liệu trong S3 và tạo metadata table trong Glue Data Catalog.
  + **Glue ETL Job**: làm sạch dữ liệu, chuyển đổi kiểu dữ liệu, validate dữ liệu lỗi, ghi dữ liệu curated dưới định dạng Parquet và partition theo thời gian.
  + **Glue Workflow**: điều phối thứ tự chạy của pipeline gồm Raw Crawler, Glue ETL Job và Curated Crawler.

- **Amazon Athena** là dịch vụ query serverless cho phép truy vấn dữ liệu trực tiếp trên Amazon S3 bằng SQL. Trong project này, Athena được dùng để validate raw/curated data và tạo các business views phục vụ dashboard.

- **Amazon QuickSight** là dịch vụ Business Intelligence của AWS, dùng để trực quan hóa dữ liệu từ Athena. Dashboard trong project giúp phân tích doanh thu, đơn hàng, funnel, hiệu quả marketing, hiệu suất sản phẩm và A/B testing.

- **EventBridge Scheduler**, **EventBridge Rules** và **Simple Notification Service** (SNS) được sử dụng để tự động hóa và giám sát pipeline. EventBridge Scheduler tự động kích hoạt Glue Workflow theo lịch, EventBridge Rules bắt lỗi Glue Job/Crawler, còn SNS gửi email thông báo khi pipeline gặp lỗi.

Mục tiêu của workshop là xây dựng một pipeline phân tích dữ liệu thương mại điện tử hoàn chỉnh trên AWS, từ dữ liệu thô ban đầu đến dashboard phân tích business, đồng thời có tự động hóa và cảnh báo lỗi cơ bản.
