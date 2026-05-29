---
title: "5.5. Tạo Glue Crawler cho Raw Data"
linkTitle: "5.5. Tạo Glue Crawler cho Raw Data"
menuTitle: "5.5. Tạo Glue Crawler cho Raw Data"
date: 2026-05-29
weight: 550
chapter: false
---


**AWS Glue Crawler** được sử dụng để quét dữ liệu trong S3, tự động nhận diện schema và tạo bảng metadata trong Glue Data Catalog.

Trong bước này, crawler sẽ quét folder: **s3:// ecommerce-analytics-datalake-270642943130-ap-southeast-1-an/raw/**

Sau khi crawler chạy thành công, hệ thống sẽ tạo ra 3 bảng tương ứng với dữ liệu raw:

- raw_events

- raw_products

- raw_transactions

### Tạo Glue Crawler

Truy cập **AWS Glue**, trong menu bên trái chọn: **Data Catalog** → **Crawlers**

Sau đó nhấn **Create crawler**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-001.png)

### Cấu hình thông tin crawler

Tại màn hình **Set crawler properties**, nhập:

- Name: **crawler_ecommerce_raw**

Sau đó nhấn **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-002.png)

### Thêm data source cho crawler

Tại bước chọn **Data sources**, nhấn **Add a data source**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-003.png)

Trong giao diện **Add a data source**, cấu hình như sau:

- Data source: Chọn **S3**

- S3 path: Nhấn Browse **S3**

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-004.png)

Chọn bucket đã tạo ở bước trước, sau đó chọn vào folder **raw/**, nhấn **Choose** để xác nhận đường dẫn.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-005.png)

Sau khi chọn xong S3 path, nhấn **Add an S3 data source**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-006.png)

Sau đó nhấn **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-007.png)

### Chọn IAM Role cho crawler

Tại màn hình **Configure security settings**, phần IAM Role chọn Role **AWSGlueServiceRoleDefault** đã tạo ở bước trước, sau đó nhấn **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-008.png)

Role này cho phép Glue Crawler truy cập vào dữ liệu trong S3 và ghi metadata vào Glue Data Catalog.

### Cấu hình output và lịch chạy crawler

Tại màn hình **Set output and scheduling**, cấu hình như sau:

- Target database: chọn **ecommerce_raw**

- Table name prefix: **raw_**

- Crawler schedule: **On demand** vì crawler sẽ được chạy thủ công. Phần schedule tự động bằng EventBridge/Glue Workflow sẽ được cấu hình ở các bước sau.

Sau khi cấu hình xong, nhấn **Next**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-009.png)

### Kiểm tra và tạo crawler

Tại màn hình **Review and create**, kiểm tra lại các thông tin đã cấu hình:

- Tên crawler

- S3 data source

- IAM Role

- Target database

- Table name prefix

- Crawler schedule

Nếu thông tin chính xác, nhấn **Create crawler**.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-010.png)

Crawler **crawler_ecommerce_raw** đã được tạo thành công.

![](/images/5-Workshop/5.5-Tao-Glue-Crawler-cho-Raw-Data/image-011.png)

### Chạy Crawler
Sau khi tạo crawler, chọn crawler **crawler_ecommerce_raw**

Nhấn **Run crawler** để bắt đầu quét dữ liệu trong S3.

Crawler sẽ đọc dữ liệu trong folder **raw/**, tự động nhận diện schema và tạo bảng metadata trong Glue Data Catalog. Sau khi crawler chạy thành công, trạng thái crawler sẽ hiển thị hoàn tất và có thông báo về số lượng bảng được tạo hoặc cập nhật.

Crawler sẽ tạo **3 bảng** tương ứng với 3 nhóm dữ liệu raw.

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-001.png)

### Kiểm tra schema trong Glue Catalog

Sau khi crawler chạy xong, vào **AWS Glue** → **Data Catalog** → **Tables**.

Tại đây, kiểm tra các bảng đã được tạo trong database **ecommerce_raw**.

Các bảng bao gồm:

- raw_events

- raw_products

- raw_transactions

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-002.png)

Chọn vào các bảng để xem thông tin chi tiết các bảng dữ liệu.

- **raw_events:**

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-003.png)

- **raw_products:**

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-004.png)

- **raw_transactions:**

![](/images/5-Workshop/5.8.3-Chay-Glue-Crawler/image-005.png)

Cả 3 bảng raw_events, raw_products và raw_transactions đã xuất hiện trong Glue Data Catalog, quá trình tạo crawler cho raw data đã hoàn tất.
Sau bước này, dữ liệu raw trong Amazon S3 đã được đăng ký metadata vào AWS Glue Data Catalog. Dữ liệu có thể được truy vấn thử bằng Amazon Athena trước khi thực hiện bước ETL sang tầng curated.