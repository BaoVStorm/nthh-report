---
title: "Bản đề xuất"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

## XÂY DỰNG E-COMMERCE ANALYTICS DATA LAKE TRÊN AWS THEO HƯỚNG SERVERLESS

### 1. Tóm tắt điều hành

**E-commerce Analytics Data Lake on AWS** được xây dựng nhằm xử lý và phân tích dữ liệu thương mại điện tử theo hướng serverless trên nền tảng AWS. Giải pháp sử dụng bộ dữ liệu Marketing & E-commerce từ Kaggle, bao gồm dữ liệu hành vi người dùng, dữ liệu sản phẩm và dữ liệu giao dịch.

Giải pháp được thiết kế theo mô hình data lake, trong đó Amazon S3 đóng vai trò là nơi lưu trữ dữ liệu trung tâm. Dữ liệu ban đầu được đưa vào S3 Raw Zone dưới dạng CSV, sau đó được xử lý bằng AWS Glue ETL Job để làm sạch, chuẩn hóa, validate lỗi và chuyển đổi sang định dạng Parquet tại S3 Curated Zone. Amazon Athena được sử dụng để truy vấn dữ liệu và tạo semantic views phục vụ phân tích. Amazon QuickSight được dùng để xây dựng dashboard trực quan hóa các chỉ số kinh doanh quan trọng.

Ngoài phần xử lý và phân tích dữ liệu, workshop còn triển khai lớp tự động hóa và giám sát pipeline. EventBridge Scheduler được sử dụng để tự động kích hoạt Glue Workflow theo lịch, trong khi EventBridge Rules và SNS Email Notification được dùng để cảnh báo khi Glue Job hoặc Glue Crawler gặp lỗi.

Workshop hướng đến mục tiêu mô phỏng một pipeline phân tích dữ liệu thương mại điện tử hoàn chỉnh, từ dữ liệu thô đến dashboard business.

### 2. Tuyên bố vấn đề

***Vấn đề hiện tại***

Trong thương mại điện tử, dữ liệu thường phát sinh từ nhiều nguồn khác nhau như sự kiện người dùng, chiến dịch marketing, thông tin sản phẩm và giao dịch mua hàng. Nếu các dữ liệu này chỉ được lưu ở dạng CSV thô, việc phân tích sẽ gặp nhiều khó khăn:

* Dữ liệu phân tán theo nhiều file và nhiều domain khác nhau.
* Dữ liệu raw có thể chứa giá trị thiếu, sai kiểu dữ liệu hoặc định dạng không nhất quán.
* Các giá trị như traffic source có thể bị viết hoa/thường không đồng nhất.
* Dữ liệu giao dịch có thể chứa bản ghi lỗi, ví dụ thiếu product_id, thiếu gross_revenue hoặc doanh thu âm không được đánh dấu là refund.
* Việc query trực tiếp CSV raw bằng Athena có thể tốn chi phí và hiệu năng thấp hơn so với dữ liệu Parquet.
* Dashboard sẽ khó xây dựng nếu toàn bộ logic business phải viết trực tiếp trong QuickSight.
* Pipeline thủ công dễ gây sai sót nếu phải chạy crawler, ETL job và crawler curated từng bước bằng tay.

Do đó, cần có một pipeline dữ liệu có khả năng lưu trữ, xử lý, chuẩn hóa, phân tích, trực quan hóa và tự động hóa theo quy trình rõ ràng.

***Giải pháp***

Giải pháp đề xuất là xây dựng một E-commerce Analytics Data Lake trên AWS theo hướng serverless.

Pipeline sử dụng Amazon S3 làm data lake, chia dữ liệu thành các vùng:

* Raw Zone: lưu dữ liệu CSV ban đầu.
* Curated Zone: lưu dữ liệu đã xử lý dưới định dạng Parquet.
* Error Zone: lưu các bản ghi giao dịch không hợp lệ.
* Athena Results: lưu kết quả truy vấn của Athena.

AWS Glue Crawler được sử dụng để tự động quét dữ liệu trong S3 và tạo metadata trong AWS Glue Data Catalog. AWS Glue ETL Job xử lý dữ liệu bằng PySpark, thực hiện cast kiểu dữ liệu, parse timestamp, chuẩn hóa text, validate transaction lỗi, ghi dữ liệu hợp lệ sang curated zone và ghi dữ liệu lỗi sang error zone.

Amazon Athena được sử dụng để kiểm tra dữ liệu raw/curated và tạo các business views. Các view này đóng vai trò semantic layer để phục vụ Amazon QuickSight. Amazon QuickSight trực quan hóa dữ liệu thông qua các dashboard như Executive Overview, Funnel Analytics, Marketing Performance, Product Analytics và A/B Testing.

Để tự động hóa pipeline, EventBridge Scheduler được dùng để kích hoạt Glue Workflow theo lịch. Glue Workflow điều phối thứ tự chạy gồm Raw Crawler → Glue ETL Job → Curated Crawler. EventBridge Rules được dùng để bắt lỗi Glue Job hoặc Glue Crawler và gửi thông báo qua SNS Email Notification.

***Lợi ích và hoàn vốn đầu tư (ROI)***

Giải pháp mang lại các lợi ích chính:

* Tự động hóa quy trình xử lý dữ liệu từ raw đến curated.
* Giảm thao tác thủ công khi chạy crawler và ETL job.
* Tối ưu truy vấn bằng cách chuyển dữ liệu từ CSV sang Parquet.
* Tổ chức dữ liệu theo mô hình data lake rõ ràng.
* Tách dữ liệu lỗi sang Error Zone để dễ kiểm tra và debug.
* Tạo semantic layer bằng Athena Views giúp dashboard dễ sử dụng hơn.
* Hỗ trợ ra quyết định business thông qua QuickSight dashboard.
* Có cơ chế cảnh báo lỗi pipeline bằng EventBridge Rules và SNS.
* Phù hợp cho môi trường học tập, demo workshop và portfolio AWS Data Engineering.

Về ROI, giải pháp giúp giảm thời gian thao tác thủ công, giảm thời gian chuẩn bị dữ liệu cho dashboard và tạo nền tảng có thể mở rộng cho các bài toán phân tích nâng cao như customer segmentation, recommendation hoặc churn analysis trong tương lai.

### 3. Kiến trúc giải pháp

Giải pháp sử dụng kiến trúc AWS Serverless Data Analytics, trong đó các thành phần chính bao gồm Amazon S3, AWS Glue, Amazon Athena, Amazon QuickSight, EventBridge, CloudWatch Logs, SNS và IAM.

Luồng kiến trúc tổng thể:

```text
Kaggle Marketing & E-commerce Dataset
        |
        v
Local Preprocessing
Rename columns only
        |
        v
Amazon S3 Raw Zone
raw/events/
raw/products/
raw/transactions/
        |
        v
AWS Glue Crawler Raw
Raw metadata catalog
        |
        v
Amazon Athena Raw Validation
Schema checks, null checks, duplicates, abnormal values
        |
        v
AWS Glue Batch ETL Job
Clean, cast, validate, enrich, partition, convert to Parquet
        |
        v
Amazon S3 Curated Zone + Error Zone
curated/fact_events/
curated/dim_products/
curated/fact_transactions/
error/transactions/
        |
        v
AWS Glue Crawler Curated
Curated metadata catalog
        |
        v
Amazon Athena Semantic Views
Business-ready SQL views
        |
        v
Amazon QuickSight Dashboards
Executive, Funnel, Marketing, Product, A/B Testing
        |
        v
Automation & Monitoring
EventBridge Scheduler + Glue Workflow + EventBridge Rules + CloudWatch Logs + SNS Alert
```

#### Dịch vụ AWS sử dụng

- **Amazon S3:**
Được sử dụng làm data lake chính để lưu trữ dữ liệu raw, dữ liệu curated, dữ liệu lỗi và kết quả truy vấn Athena.

- **AWS Glue Data Catalog:**
Lưu metadata của raw tables và curated tables để Athena có thể truy vấn dữ liệu trên S3.

- **AWS Glue Crawler:**
Tự động quét dữ liệu trong S3 và tạo bảng metadata. Project sử dụng Raw Crawler và Curated Crawler.

- **AWS Glue ETL Job:**
Xử lý dữ liệu CSV từ raw zone, làm sạch, chuẩn hóa, validate và ghi dữ liệu Parquet sang curated zone.

- **AWS Glue Workflow:**
Điều phối luồng chạy Raw Crawler → Glue ETL Job → Curated Crawler theo thứ tự.

- **Amazon Athena:**
Truy vấn dữ liệu trực tiếp trên S3 bằng SQL, validate dữ liệu và tạo business views cho dashboard.

- **Amazon QuickSight:**
Kết nối với Athena để xây dựng dashboard phân tích dữ liệu thương mại điện tử.

- **Amazon EventBridge Scheduler:**
Tự động kích hoạt Glue Workflow theo lịch thông qua API StartWorkflowRun.

- **Amazon EventBridge Rules:**
Bắt các event lỗi từ Glue Job và Glue Crawler.

- **Amazon SNS:**
Gửi email notification khi pipeline gặp lỗi.

- **Amazon CloudWatch Logs:**
Lưu log của Glue ETL Job để kiểm tra và debug.

- **AWS IAM:**
Quản lý quyền truy cập cho Glue, EventBridge Scheduler và các service liên quan.

#### Thiết kế thành phần

- **Data Source:**
Bộ dữ liệu Marketing & E-commerce từ Kaggle, bao gồm events.csv, products.csv và transactions.csv.

- **Local Preprocessing:**
Kiểm tra dữ liệu ban đầu và đổi tên một số cột để dễ xử lý hơn, ví dụ timestamp thành event_timestamp hoặc transaction_timestamp.

- **S3 Raw Zone:**
Lưu dữ liệu CSV ban đầu theo từng domain: events, products và transactions.

- **Raw Glue Crawler:**
Quét dữ liệu raw và tạo các bảng metadata trong database ecommerce_raw.

- **Athena Raw Validation:**
Kiểm tra schema, số dòng, event type, category, quantity, null values và abnormal values.

- **Glue ETL Job:**
Làm sạch dữ liệu, chuẩn hóa kiểu dữ liệu, validate transaction lỗi, tạo cột thời gian, ghi dữ liệu Parquet và partition theo year/month/day.

- **S3 Curated Zone:**
Lưu dữ liệu đã xử lý gồm fact_events, dim_products và fact_transactions.

- **Error Zone:**
Lưu các transaction không hợp lệ để kiểm tra sau.

- **Curated Glue Crawler:**
Quét dữ liệu curated và tạo các bảng metadata trong database ecommerce_curated.

- **Athena Semantic Views:**
Tạo các view phục vụ dashboard như executive overview, funnel, marketing, product và A/B testing.

- **QuickSight Dashboards:**
Trực quan hóa dữ liệu theo nhiều góc nhìn business.

- **Automation & Monitoring:**
EventBridge Scheduler chạy workflow theo lịch, EventBridge Rules bắt lỗi, SNS gửi email và CloudWatch Logs hỗ trợ debug.

### 4. Triển khai kỹ thuật

#### Các giai đoạn triển khai

Project được triển khai theo các giai đoạn chính sau:

**Giai đoạn 1: Khảo sát dữ liệu và thiết kế kiến trúc**
Nghiên cứu dataset từ Kaggle, xác định các file dữ liệu chính, phân tích schema, xác định các bảng fact/dimension và thiết kế kiến trúc data lake trên AWS.

**Giai đoạn 2: Xây dựng S3 Data Lake**
Tạo S3 bucket và tổ chức thư mục theo các zone: raw, curated, error và athena-results. Upload dữ liệu CSV sau local preprocessing vào đúng thư mục trong Raw Zone.

**Giai đoạn 3: Tạo Glue Data Catalog cho Raw Data**
Tạo IAM Role cho AWS Glue, tạo Glue Database ecommerce_raw và tạo Raw Crawler để crawl dữ liệu CSV trong Raw Zone.

**Giai đoạn 4: Validate dữ liệu raw bằng Athena**
Cấu hình Athena query result location, query thử dữ liệu raw và chạy các câu query kiểm tra dữ liệu như số dòng, event type, product category và quantity distribution.

**Giai đoạn 5: Phát triển Glue ETL Job**
Viết Glue ETL script bằng PySpark để xử lý dữ liệu events, products và transactions. ETL Job thực hiện clean, cast, validate, partition và chuyển đổi dữ liệu sang Parquet.

**Giai đoạn 6: Tạo Glue Data Catalog cho Curated Data**
Tạo Glue Database ecommerce_curated, tạo Curated Crawler và crawl dữ liệu Parquet trong Curated Zone.

**Giai đoạn 7: Validate dữ liệu curated**
Dùng Athena để kiểm tra dữ liệu sau ETL, bao gồm tổng số dòng, dữ liệu refund, transaction lỗi, null values và schema curated.

**Giai đoạn 8: Tạo Athena Views**
Tạo các business views phục vụ dashboard như vw_executive_overview, vw_daily_event_funnel, vw_traffic_source_performance, vw_product_revenue và vw_ab_testing_summary.

**Giai đoạn 9: Xây dựng QuickSight Dashboards**
Kết nối QuickSight với Athena bằng Direct Query và xây dựng các dashboard phân tích business.

**Giai đoạn 10: Automation & Monitoring**
Tạo Glue Workflow, EventBridge Scheduler, EventBridge Rules, SNS Email Notification và kiểm tra CloudWatch Logs cho Glue ETL Job.

#### Yêu cầu kỹ thuật

**Dữ liệu đầu vào:**

* events.csv
* products.csv
* transactions.csv

**Hạ tầng AWS:**

* Amazon S3 bucket cho data lake.
* AWS Glue Data Catalog cho raw và curated database.
* AWS Glue Crawlers cho raw zone và curated zone.
* AWS Glue ETL Job sử dụng PySpark.
* Amazon Athena để query dữ liệu.
* Amazon QuickSight để trực quan hóa.
* EventBridge Scheduler để chạy workflow theo lịch.
* EventBridge Rules và SNS để cảnh báo lỗi.
* CloudWatch Logs để theo dõi log ETL.

**Quyền truy cập:**

* IAM Role cho AWS Glue với quyền AWSGlueServiceRole và quyền truy cập S3.
* IAM Role cho EventBridge Scheduler với quyền glue:StartWorkflowRun.
* SNS subscription email đã được confirm.

**Yêu cầu xử lý dữ liệu:**

* Parse timestamp.
* Cast kiểu dữ liệu.
* Chuẩn hóa traffic_source.
* Xử lý null device_type.
* Cast is_premium và is_refunded sang boolean.
* Validate transaction lỗi.
* Ghi Parquet.
* Partition fact_events và fact_transactions theo year/month/day.
* Tạo Athena Views cho QuickSight.

### 5. Lộ trình & Mốc triển khai

#### Chuẩn bị

* Xác định đề tài và phạm vi project.
* Chọn dataset phù hợp từ Kaggle.
* Khảo sát schema và các vấn đề dữ liệu.
* Thiết kế kiến trúc tổng thể của pipeline.
* Chuẩn bị tài khoản AWS, S3 bucket và quyền truy cập cần thiết.

#### Giai đoạn 1: Data Lake Foundation

* Tạo S3 bucket.
* Tạo cấu trúc thư mục raw, curated, error và athena-results.
* Upload dữ liệu CSV lên S3 Raw Zone.
* Tạo Glue IAM Role.
* Tạo Glue Database cho raw data.
* Tạo và chạy Raw Crawler.

#### Giai đoạn 2: Data Validation & ETL

* Cấu hình Athena query result location.
* Query kiểm tra raw tables.
* Phát triển Glue ETL Job.
* Chạy Glue ETL Job.
* Kiểm tra output trong S3 Curated Zone và Error Zone.
* Tạo Glue Database và Crawler cho curated data.
* Validate dữ liệu curated bằng Athena.

#### Giai đoạn 3: Analytics Layer & Dashboard

* Tạo Athena Views cho analytics.
* Kết nối QuickSight với Athena.
* Tạo các calculated fields và filters.
* Xây dựng dashboard Executive Overview.
* Xây dựng dashboard Funnel Analytics.
* Xây dựng dashboard Marketing Performance.
* Xây dựng dashboard Product Analytics.
* Xây dựng dashboard A/B Testing.

#### Giai đoạn 4: Automation & Monitoring

* Tạo SNS Topic và email subscription.
* Tạo Glue Workflow.
* Tạo EventBridge Scheduler để start Glue Workflow.
* Tạo EventBridge Rules để bắt lỗi crawler/job.
* Kiểm tra CloudWatch Logs.
* Test schedule và alert.
* Hoàn thiện documentation và host report bằng Hugo/GitHub Pages.

### 6. Ước tính ngân sách

Chi phí thực tế phụ thuộc vào dung lượng dữ liệu, số lần chạy Glue Job, số lần query Athena, số lượng dashboard QuickSight và thời gian sử dụng. Trong phạm vi workshop, project được triển khai ở quy mô nhỏ, chủ yếu phục vụ học tập và demo.

Có thể sử dụng **AWS Pricing Calculator** để ước tính chi phí chính xác hơn trước khi triển khai.

#### Chi phí hạ tầng dự kiến

- **Amazon S3:**
Dùng để lưu raw CSV, curated Parquet, error data và Athena query results. Với dung lượng dữ liệu nhỏ trong workshop, chi phí lưu trữ thấp.

- **AWS Glue Crawler:**
Chi phí phát sinh khi crawler chạy để crawl Raw Zone và Curated Zone.

- **AWS Glue ETL Job:**
Chi phí phát sinh theo thời gian chạy và số DPU sử dụng. Project chỉ chạy ETL theo lịch hoặc khi cần test, nên có thể kiểm soát chi phí.

- **Amazon Athena:**
Chi phí dựa trên lượng dữ liệu scan khi query. Việc chuyển dữ liệu sang Parquet và partition theo year/month/day giúp giảm lượng dữ liệu scan.

- **Amazon QuickSight:**
Chi phí phụ thuộc vào loại tài khoản, số lượng author/reader và chế độ sử dụng. Project sử dụng Direct Query để tránh phải quản lý refresh SPICE.

- **Amazon EventBridge Scheduler** và **EventBridge Rules:**
Chi phí thấp trong phạm vi workshop vì số lượng schedule và rule ít.

- **Amazon SNS:**
Chi phí thấp do chỉ gửi email notification khi pipeline gặp lỗi.

- **Amazon CloudWatch Logs:**
Chi phí phụ thuộc vào lượng log phát sinh từ Glue ETL Job.

#### Ước tính tổng quan

Ở quy mô workshop, chi phí có thể được kiểm soát bằng cách:

* Chạy Glue Job theo lịch hợp lý.
* Không chạy crawler quá nhiều lần.
* Dùng Parquet để giảm Athena scan.
* Xóa dữ liệu test không cần thiết.
* Theo dõi billing trong AWS Billing Dashboard.
* Tạo AWS Budget nếu cần cảnh báo chi phí.

### 7. Đánh giá rủi ro

#### Ma trận rủi ro

**Rủi ro 1: Glue ETL Job failed**
- Ảnh hưởng: Cao
- Xác suất: Trung bình
- Nguyên nhân: có thể do sai schema, sai kiểu dữ liệu, thiếu quyền S3 hoặc lỗi PySpark.

**Rủi ro 2: Glue Crawler không nhận đúng schema**
- Ảnh hưởng: Trung bình
- Xác suất: Trung bình
- Nguyên nhân: có thể do dữ liệu CSV không đồng nhất, header lỗi hoặc folder S3 sai.

**Rủi ro 3: Athena query lỗi hoặc scan nhiều dữ liệu**
- Ảnh hưởng: Trung bình
- Xác suất: Trung bình
- Nguyên nhân: có thể do table metadata chưa cập nhật, partition chưa đúng hoặc query chưa tối ưu.

**Rủi ro 4: QuickSight không kết nối được Athena/S3**
- Ảnh hưởng: Trung bình
- Xác suất: Trung bình
- Nguyên nhân: có thể do sai region, thiếu quyền truy cập S3 hoặc chưa cấp quyền QuickSight cho Athena.

**Rủi ro 5: Chi phí AWS tăng ngoài dự kiến**
- Ảnh hưởng: Trung bình
- Xác suất: Thấp đến trung bình
- Nguyên nhân: có thể do chạy Glue/Athena/QuickSight nhiều lần hoặc query dữ liệu raw CSV quá nhiều.

**Rủi ro 6: EventBridge Scheduler hoặc alert cấu hình sai**
- Ảnh hưởng: Trung bình
- Xác suất: Trung bình
- Nguyên nhân: có thể do sai IAM Role, sai API target, sai input JSON hoặc SNS email chưa confirm.

#### Chiến lược giảm thiểu

**Đối với Glue ETL Job failed:**

* Kiểm tra CloudWatch Logs.
* Test script với dữ liệu nhỏ trước.
* Validate schema raw trước khi chạy ETL.
* Tách dữ liệu lỗi vào Error Zone.

**Đối với Glue Crawler:**

* Kiểm tra đúng S3 path.
* Dùng prefix table rõ ràng.
* Chạy crawler lại sau khi ETL ghi dữ liệu mới.

**Đối với Athena:**

* Dùng Parquet thay vì query trực tiếp CSV raw.
* Partition fact_events và fact_transactions theo year/month/day.
* Tạo Athena Views để giảm lỗi khi dùng trong QuickSight.

**Đối với QuickSight:**

* Đảm bảo QuickSight, Athena, Glue và S3 cùng region.
* Cấp quyền QuickSight truy cập Athena và S3 bucket.
* Dùng Direct Query để dữ liệu cập nhật theo Athena views.

**Đối với chi phí:**

* Theo dõi AWS Billing Dashboard.
* Hạn chế chạy Glue Job và Crawler liên tục.
* Xóa tài nguyên không cần thiết sau workshop.
* Dùng AWS Budget nếu cần.

**Đối với automation và alert:**

* Test Glue Workflow thủ công trước.
* Test EventBridge Scheduler bằng cron gần thời điểm hiện tại.
* Kiểm tra Workflow History và Job run monitoring.
* Confirm SNS email subscription trước khi tạo rule alert.

#### Kế hoạch dự phòng

* Nếu EventBridge Scheduler lỗi, có thể chạy Glue Workflow thủ công.
* Nếu Glue Workflow lỗi, có thể chạy từng bước riêng: Raw Crawler → Glue ETL Job → Curated Crawler.
* Nếu QuickSight gặp lỗi, có thể dùng Athena query result để minh họa phân tích.
* Nếu chi phí vượt dự kiến, tạm dừng schedule và chỉ chạy pipeline khi cần demo.
* Nếu alert chưa hoạt động, kiểm tra thủ công CloudWatch Logs và Glue Job Run History.


### 8. Kết quả kỳ vọng

Sau khi hoàn thành workshop, project kỳ vọng đạt được các kết quả sau:

#### Kết quả kỹ thuật

* Xây dựng được một AWS Data Lake có cấu trúc rõ ràng gồm Raw Zone, Curated Zone, Error Zone và Athena Results.
* Tạo được Glue Data Catalog cho raw data và curated data.
* Xây dựng được Glue ETL Job để xử lý dữ liệu CSV sang Parquet.
* Validate được dữ liệu lỗi và tách transaction không hợp lệ vào Error Zone.
* Tạo được Athena Views đóng vai trò semantic layer cho dashboard.
* Kết nối được QuickSight với Athena bằng Direct Query.
* Xây dựng được các dashboard phân tích business.
* Tạo được Glue Workflow để điều phối pipeline.
* Tạo được EventBridge Scheduler để tự động chạy workflow theo lịch.
* Tạo được EventBridge Rules và SNS Email Notification để cảnh báo lỗi.

#### Kết quả phân tích business

Project giúp trả lời các câu hỏi phân tích quan trọng:

* Doanh thu thay đổi như thế nào theo thời gian?
* Số lượng đơn hàng và average order value có ổn định không?
* Refund rate có tăng bất thường không?
* Người dùng rơi rụng nhiều nhất ở bước nào trong funnel?
* Traffic source nào tạo nhiều purchases nhất?
* Campaign nào có conversion rate tốt?
* Product, category hoặc brand nào tạo doanh thu cao nhất?
* Premium product có hiệu quả hơn non-premium product không?
* Product hoặc category nào có refund rate cao?
* Experiment group nào trong A/B testing có conversion tốt hơn?

#### Giá trị dài hạn

Project có thể được mở rộng để phục vụ các bài toán nâng cao như:

* Customer segmentation.
* Churn analysis.
* Recommendation system.
* Marketing attribution.
* Data quality monitoring.
* CI/CD cho Glue scripts và Athena views.
* Cost monitoring bằng AWS Budgets.
* Dashboard sharing hoặc embedding.

Nhìn chung, project không chỉ là một dashboard phân tích dữ liệu mà còn mô phỏng một quy trình Data Engineering hoàn chỉnh trên AWS. Đây là nền tảng phù hợp để phát triển kỹ năng thực tế về data lake, ETL, SQL analytics, BI dashboard, automation và monitoring trong môi trường cloud.
