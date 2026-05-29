---
title: "5.3. Tạo S3 Raw Zone"
linkTitle: "5.3. Tạo S3 Raw Zone"
menuTitle: "5.3. Tạo S3 Raw Zone"
date: 2026-05-29
weight: 530
chapter: false
---

Bước tiếp theo là tạo S3 Raw Zone và upload 3 file đã rename columns lên đúng prefix.

### Tạo S3 bucket:

Truy cập **AWS Management Console**. Tại thanh tìm kiếm, nhập S3, sau đó chọn dịch vụ **S3**.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-001.png)

Trong giao diện Amazon S3, chọn mục **Buckets**, sau đó nhấn **Create bucket** để bắt đầu tạo bucket mới.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-002.png)

#### Cấu hình thông tin bucket

Trong giao diện Create bucket, cấu hình các thông tin như sau:

- Bucket namespace: chọn **Account Regional namespace**

- Bucket name prefix: nhập tên **ecommerce-analytics-datalake**

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-003.png)

Sau đó tiếp tục kiểm tra các thiết lập còn lại trước khi tạo bucket. Các thiết lập khác giữ mặc định. Nhấn **Create bucket**.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-004.png)

Bucket đã được tạo thành công.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-005.png)

### Tạo thư mục trong S3 Bucket:

Sau khi tạo bucket thành công, truy cập vào bucket vừa tạo. Trong giao diện bucket, nhấn **Create folder** để tạo thư mục mới.

Tạo thư mục đầu tiên với thông tin sau:

- Folder name: **raw**

Nhấn **Create folder** để hoàn tất.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-006.png)

Tạo thành công folder **raw/**

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-007.png)

Sau khi tạo thành công thư mục raw/, truy cập vào thư mục này và tiếp tục tạo các thư mục con sau: **events**, **products**, **transactions**.

Cây thư mục hiện tại:
```
raw/
raw/events/
raw/products/
raw/transactions/
curated/
curated/fact_events/
curated/dim_products/
curated/fact_transactions/
error/
error/events/
error/transactions/
athena-results/
```

Nội dung thư mục:

- **raw/**: dùng để lưu trữ dữ liệu CSV ban đầu trước khi xử lý bằng AWS Glue.

- **curated/**: chứa data sau khi đã xử lý dạng Parquet.

- **error/**: dùng để lưu dữ liệu lỗi hoặc output lỗi ETL.

- **athena-results/**: nơi Athena lưu kết quả query.

### Upload dữ liệu từ local lên S3

Sau khi tạo xong cấu trúc thư mục trong S3, tiến hành upload các file CSV đã xử lý ở máy local lên đúng thư mục tương ứng.

- Upload file **events.csv**: Truy cập vào đường dẫn **raw/events/** trong bucket, nhấn Upload để bắt đầu upload file.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-008.png)

Trong giao diện upload:

- Nhấn **Add files**

- Chọn file **events.csv** từ máy local

- Nhấn **Upload**

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-009.png)

Sau khi upload hoàn tất, kiểm tra lại trong thư mục **raw/events/** để đảm bảo file events.csv đã được tải lên thành công.

![](/images/5-Workshop/5.3-Tao-S3-Raw-Zone/image-010.png)

Thực hiện tương tự cho các file còn lại:

| File cần upload | Thư mục S3 tương ứng |
| --- | --- |
| products.csv | raw/products/ |
| transactions.csv | raw/transactions/ |

Sau khi hoàn tất, cấu trúc dữ liệu trong S3 sẽ có dạng:

```
ecommerce-analytics-datalake/
└── raw/
    ├── events/
    │   └── events.csv
    ├── products/
    │   └── products.csv
    └── transactions/
        └── transactions.csv
```

Ở bước này, dữ liệu raw đã được upload thành công lên Amazon S3 và sẵn sàng để sử dụng cho các bước tiếp theo như tạo **Glue Crawler**, **Glue Data Catalog** và xử lý ETL.
