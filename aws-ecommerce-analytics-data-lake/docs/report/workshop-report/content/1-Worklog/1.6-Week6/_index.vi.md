---
title: "Worklog Tuần 6"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

## Tuần 6: Xây dựng Glue ETL Job

**Thời gian:** 06/04/2026 - 10/04/2026

### Mục tiêu tuần 6:

* Tìm hiểu AWS Glue ETL Job và cách xử lý dữ liệu bằng PySpark.
* Xây dựng script ETL để chuyển dữ liệu từ Raw Zone sang Curated Zone.
* Làm sạch, chuẩn hóa và chuyển đổi kiểu dữ liệu cho events, products và transactions.
* Validate dữ liệu transaction lỗi.
* Ghi dữ liệu đầu ra dưới định dạng Parquet và partition theo thời gian.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---:|---:|---|
| Thứ 2 | - Tìm hiểu AWS Glue ETL Job và PySpark DataFrame.<br>- Tìm hiểu cách đọc CSV từ S3 trong Glue script.<br>- Cấu hình Glue Job, IAM Role và job parameter.<br>- Tạo khung script ETL ban đầu. | 06/04/2026 | 06/04/2026 | [Programming Spark scripts - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming.html)<br>[Program AWS Glue ETL scripts in PySpark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python.html)<br>[AWS Glue Spark and PySpark jobs](https://docs.aws.amazon.com/glue/latest/dg/spark_and_pyspark.html)<br>[Using the CSV format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-csv-home.html) |
| Thứ 3 | - Viết logic xử lý bảng events.<br>- Parse event_timestamp, cast kiểu dữ liệu, xử lý product_id dạng float/string.<br>- Chuẩn hóa device_type và traffic_source.<br>- Tạo các cột event_date, event_hour, year, month, day. | 07/04/2026 | 07/04/2026 | [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)<br>[PySpark Column cast](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Column.cast.html)<br>[PySpark to_timestamp](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_timestamp.html)<br>[PySpark to_date](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_date.html)<br>[PySpark date functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#datetime-functions) |
| Thứ 4 | - Viết logic xử lý bảng products.<br>- Cast product_id, base_price và launch_date.<br>- Chuyển is_premium sang boolean.<br>- Ghi dim_products ra Parquet và kiểm tra output. | 08/04/2026 | 08/04/2026 | [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)<br>[PySpark Column cast](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Column.cast.html)<br>[PySpark to_date](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_date.html)<br>[PySpark when](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.when.html)<br>[Using the Parquet format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html) |
| Thứ 5 | - Viết logic xử lý bảng transactions.<br>- Parse transaction_timestamp, cast quantity, discount_applied, gross_revenue.<br>- Xây dựng điều kiện validate transaction lỗi.<br>- Tách valid_transactions và invalid_transactions. | 09/04/2026 | 09/04/2026 | [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)<br>[PySpark Column cast](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Column.cast.html)<br>[PySpark to_timestamp](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_timestamp.html)<br>[PySpark when](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.when.html)<br>[PySpark filter](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.filter.html)<br>[AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality.html) |
| Thứ 6 | - Chạy thử Glue ETL Job.<br>- Kiểm tra trạng thái job run, output S3 và CloudWatch Logs.<br>- Debug lỗi nếu có trong quá trình đọc/ghi dữ liệu.<br>- Ghi chú kết quả ETL và cập nhật report. | 10/04/2026 | 10/04/2026 | [AWS Glue job run statuses on the console](https://docs.aws.amazon.com/glue/latest/dg/view-job-runs.html)<br>[Monitoring AWS Glue using Amazon CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html)<br>[What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br>[Using the Parquet format in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html) |

### Kết quả đạt được tuần 6:

* Hiểu được cách AWS Glue ETL Job hoạt động trong pipeline xử lý dữ liệu.
* Tạo được Glue ETL Job đọc dữ liệu CSV từ S3 Raw Zone.
* Xử lý được bảng events, products, transactions với một số bước cơ bản.
* Tách được dữ liệu hợp lệ sang Curated Zone và dữ liệu lỗi sang Error Zone.
* Ghi dữ liệu đầu ra ở định dạng Parquet.
* Biết cách kiểm tra Glue Job Run, trạng thái chạy job và log lỗi trong CloudWatch.
