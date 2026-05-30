---
title: "5.19. Dọn dẹp tài nguyên"
linkTitle: "5.19. Dọn dẹp tài nguyên"
menuTitle: "5.19. Dọn dẹp tài nguyên"
date: 2026-05-29
weight: 690
chapter: false
---

Sau khi hoàn thành workshop và đã lưu lại các hình ảnh, dashboard, kết quả chạy workflow và nội dung báo cáo, cần dọn dẹp các tài nguyên AWS đã tạo để tránh phát sinh chi phí không cần thiết.

#### I. EventBridge Scheduler

Go to: **Amazon EventBridge Console**

Delete Schedule: ```schedule-ecommerce-glue-workflow```

Các bước thực hiện:

1. Vào **Amazon EventBridge**.
2. Chọn **Scheduler** → **Schedules**.
3. Chọn schedule `schedule-ecommerce-glue-workflow`.
4. Chọn **Delete** nếu không còn sử dụng.
5. Xác nhận xóa schedule.

Schedule này trước đó được dùng để gọi Glue API `StartWorkflowRun` và tự động chạy workflow theo lịch.


#### II. EventBridge Rules

Go to: **Amazon EventBridge Console**

Delete Rules:```alert-ecommerce-crawler-failed``` và ```alert-ecommerce-glue-job-failed```

Các bước thực hiện:

1. Vào **Amazon EventBridge**.
2. Chọn **Rules**.
3. Chọn rule `alert-ecommerce-crawler-failed`.
4. Chọn **Delete**.
5. Thực hiện tương tự với rule `alert-ecommerce-glue-job-failed`.

Các rule này được dùng để bắt lỗi Glue Crawler hoặc Glue ETL Job và gửi cảnh báo đến SNS.

#### III. SNS Topic

Go to: **Amazon SNS Console**

Delete Topic: ```ecommerce-etl-alerts```

Các bước thực hiện:

1. Vào **Amazon SNS**.
2. Chọn **Topics**.
3. Chọn topic `ecommerce-etl-alerts`.
4. Chọn **Delete**.
5. Xác nhận xóa topic.

SNS Topic này được dùng để gửi email notification khi pipeline gặp lỗi. Khi xóa topic, các email subscription liên quan cũng không còn được sử dụng.

#### IV. Glue Workflow

Go to: **AWS Glue Console**

Delete Workflow: ```ecommerce-scheduled-etl-workflow```

Các bước thực hiện:

1. Vào **AWS Glue**.
2. Chọn **ETL** → **Workflows**.
3. Chọn workflow `ecommerce-scheduled-etl-workflow`.
4. Chọn **Actions** → **Delete**.
5. Xác nhận xóa workflow.

***Lưu ý:*** Xóa workflow chỉ xóa phần điều phối. Glue Crawlers và Glue ETL Job vẫn cần được xóa riêng.

#### V. Glue Crawlers

Go to: **AWS Glue Console**

Delete Crawlers: ```crawler_ecommerce_raw``` và ```crawler_ecommerce_curated```

Các bước thực hiện:

1. Vào **AWS Glue**.
2. Chọn **Data Catalog** → **Crawlers**.
3. Chọn crawler `crawler_ecommerce_raw`.
4. Chọn **Actions** → **Delete crawler**.
5. Thực hiện tương tự với crawler `crawler_ecommerce_curated`.

#### VI. Glue ETL Job

Go to: **AWS Glue Console**

Delete Job: ```etl_ecommerce_raw_to_curated_1```

Các bước thực hiện:

1. Vào **AWS Glue**.
2. Chọn **ETL jobs**.
3. Chọn job `etl_ecommerce_raw_to_curated_1`.
4. Chọn **Actions** → **Delete**.
5. Xác nhận xóa job.

#### VII. Glue Databases

Go to: **AWS Glue Console**

Delete Databases: ```ecommerce_raw``` và ```ecommerce_curated```

Các bước thực hiện:

1. Vào **AWS Glue**.
2. Chọn **Data Catalog** → **Databases**.
3. Chọn database `ecommerce_raw`.
4. Chọn **Delete**.
5. Thực hiện tương tự với database `ecommerce_curated`.

***Lưu ý:*** Xóa Glue Database chỉ xóa metadata trong Glue Data Catalog, không xóa dữ liệu thực tế trong Amazon S3.

#### VIII. Athena Query Results

Go to: **Amazon S3 Console**

Delete Athena results folder: ```s3://ecommerce-analytics-datalake-270642943130-ap-southeast-1-an/athena-results/```

Các bước thực hiện:

1. Vào **Amazon S3**.
2. Chọn bucket: ```ecommerce-analytics-datalake-270642943130-ap-southeast-1-an```
3. Chọn folder `athena-results/`.
4. Chọn **Delete**.
5. Xác nhận xóa các query result không còn cần thiết.

#### IX. QuickSight Dashboards

Go to: **Amazon QuickSight Console**

Delete Dashboards: Executive Overview, Funnel Analytics, Marketing Performance, Product Analytics, A/B Testing.

Các bước thực hiện:

1. Vào **Amazon QuickSight**.
2. Chọn **Dashboards**.
3. Chọn từng dashboard đã publish.
4. Chọn **Delete**.
5. Xác nhận xóa dashboard.

#### X. QuickSight Analyses

Go to: **Amazon QuickSight Console**

Delete Analyses:Executive Overview Analysis, Funnel Analytics Analysis, Marketing, Performance Analysis, Product Analytics Analysis, A/B Testing Analysis.

Các bước thực hiện:

1. Vào **Amazon QuickSight**.
2. Chọn **Analyses**.
3. Chọn các analysis tương ứng với dashboard đã tạo.
4. Chọn **Delete**.
5. Xác nhận xóa analysis.

#### XI. QuickSight Datasets

Go to: **Amazon QuickSight Console**

Delete Datasets created from Athena views.

Các bước thực hiện:

1. Vào **Amazon QuickSight**.
2. Chọn **Datasets**.
3. Chọn dataset được tạo từ Athena.
4. Chọn **Delete**.
5. Xác nhận xóa dataset.

#### XII. CloudWatch Logs

Go to: **Amazon CloudWatch Console**

Delete Glue log groups nếu không còn dùng nữa: ```/aws-glue/jobs/output``` và ```/aws-glue/jobs/error```

Các bước thực hiện:

1. Vào **Amazon CloudWatch**.
2. Chọn **Logs** → **Log groups**.
3. Tìm các log group liên quan đến AWS Glue.
4. Chọn log group không còn cần sử dụng.
5. Chọn **Delete log group**.
6. Xác nhận xóa.

#### XIII. S3 Data Lake Bucket

Go to: **Amazon S3 Console**

Delete Bucket: ```ecommerce-analytics-datalake-270642943130-ap-southeast-1-an```

Trước khi xóa bucket, cần empty bucket.

Các folder cần kiểm tra:

```
raw/
curated/
error/
athena-results/
```

Các bước thực hiện:

1. Vào **Amazon S3**.
2. Chọn bucket `ecommerce-analytics-datalake-270642943130-ap-southeast-1-an`.
3. Xóa các folder hoặc object bên trong bucket:
   * `raw/`
   * `curated/`
   * `error/`
   * `athena-results/`
4. Sau khi bucket đã rỗng, quay lại danh sách bucket.
5. Chọn bucket.
6. Chọn **Delete**.
7. Nhập tên bucket để xác nhận.
8. Chọn **Delete bucket**.

#### XIV. IAM Role for EventBridge Scheduler

Go to: **IAM Console**

Delete Role: ```EventBridgeSchedulerStartGlueWorkflowRole```

Các bước thực hiện:

1. Vào **IAM**.
2. Chọn **Roles**.
3. Tìm role `EventBridgeSchedulerStartGlueWorkflowRole`.
4. Kiểm tra role không còn được EventBridge Scheduler sử dụng.
5. Chọn **Delete**.
6. Xác nhận xóa role.

#### XV. IAM Policy for EventBridge Scheduler

Go to: **IAM Console**

Delete Policy: ```AllowStartGlueWorkflow```

Các bước thực hiện:

1. Vào **IAM**.
2. Chọn **Policies**.
3. Tìm policy `AllowStartGlueWorkflow`.
4. Đảm bảo policy không còn attached với role nào.
5. Chọn **Delete**.
6. Xác nhận xóa policy.

#### XVI. IAM Role for AWS Glue

Go to: **IAM Console**

Check Role: ```AWSGlueServiceRoleDefault```

Các bước thực hiện:

1. Vào **IAM**.
2. Chọn **Roles**.
3. Tìm role `AWSGlueServiceRoleDefault`.
4. Chỉ xóa role này nếu chắc chắn nó chỉ được tạo cho workshop và không còn Glue Job/Crawler nào sử dụng.
5. Nếu không chắc chắn, nên giữ lại role để tránh ảnh hưởng đến các project khác.

***Lưu ý:*** Không xóa AWS managed policies như `AWSGlueServiceRole` hoặc `AmazonS3FullAccess`. Nếu cần dọn dẹp, chỉ detach khỏi role hoặc xóa role custom đã tạo cho workshop.


#### Kết luận

Bước dọn dẹp tài nguyên giúp tránh phát sinh chi phí sau khi hoàn thành workshop. Trong project này, các tài nguyên cần kiểm tra và xóa bao gồm EventBridge Scheduler, EventBridge Rules, SNS Topic, Glue Workflow, Glue Crawlers, Glue ETL Job, Glue Databases, QuickSight dashboards, Athena results, CloudWatch Logs, S3 bucket và các IAM role/policy liên quan.

Sau khi dọn dẹp, cần kiểm tra lại AWS Billing để đảm bảo không còn tài nguyên nào tiếp tục phát sinh chi phí ngoài ý muốn.
