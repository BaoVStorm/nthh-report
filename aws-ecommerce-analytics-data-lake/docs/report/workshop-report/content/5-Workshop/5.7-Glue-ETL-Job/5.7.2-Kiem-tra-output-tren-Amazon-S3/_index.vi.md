---
title: "5.7.2. Kiểm tra output trên Amazon S3"
linkTitle: "5.7.2. Kiểm tra output trên Amazon S3"
menuTitle: "5.7.2. Kiểm tra output trên Amazon S3"
date: 2026-05-29
weight: 573
chapter: false
---

Sau khi Glue Job chạy thành công, quay lại dịch vụ Amazon S3.

Truy cập vào bucket của project **ecommerce-analytics-datalake-270642943130-ap-southeast-1-an**

Sau đó kiểm tra folder **curated/**

Cấu trúc dữ liệu sau ETL sẽ có dạng:

```
curated/
├── dim_products/
├── fact_events/
└── fact_transactions/
```

Cấu trúc data sau khi ETL:

```
curated/
├── dim_products/
│   └── part-xxxxx.snappy.parquet
│
├── fact_events/
│   └── year=2021/
│       └── month=1/
│           └── day=1/
│               └── part-xxxxx.snappy.parquet
│
└── fact_transactions/
    └── year=2021/
        └── month=1/
            └── day=1/
                └── part-xxxxx.snappy.parquet
```

#### Kiểm tra bảng dim_products

- Truy cập vào **curated/dim_products/**

- Folder này chứa dữ liệu sản phẩm đã được làm sạch và ghi dưới định dạng Parquet.

- Dữ liệu trong folder này không partition theo ngày vì đây là bảng dimension sản phẩm.

![](/images/5-Workshop/5.7.3-Kiem-tra-output-tren-Amazon-S3/image-001.png)

#### Kiểm tra bảng fact_events

- Truy cập vào **curated/fact_events/**

- Bảng **fact_events** được partition theo year, month, day, vì vậy cấu trúc folder sẽ có dạng tương tự:

```
curated/fact_events/
└── year=YYYY/
    └── month=MM/
        └── day=DD/
            └── part-xxxxx.parquet
```

Cách tổ chức partition này giúp Athena và các công cụ phân tích truy vấn dữ liệu hiệu quả hơn khi lọc theo ngày, tháng hoặc năm.

![](/images/5-Workshop/5.7.3-Kiem-tra-output-tren-Amazon-S3/image-002.png)

#### Kiểm tra bảng fact_transactions

- Truy cập vào **curated/fact_transactions/**

- Bảng **fact_transactions** cũng được partition theo year, month, day.

- Cấu trúc folder sẽ có dạng tương tự:

```
curated/fact_transactions/
└── year=YYYY/
    └── month=MM/
        └── day=DD/
            └── part-xxxxx.parquet
```

Folder này chỉ chứa các transaction hợp lệ sau khi đã được validate.

![](/images/5-Workshop/5.7.3-Kiem-tra-output-tren-Amazon-S3/image-003.png)

#### Kiểm tra dữ liệu lỗi

- Tiếp tục kiểm tra folder **error/transactions/**

- Folder này chứa các transaction không hợp lệ, ví dụ:

  + Thiếu product_id

  + Thiếu gross_revenue

  + Sai định dạng transaction_timestamp

  + Có gross_revenue < 0 nhưng không được đánh dấu là refund

![](/images/5-Workshop/5.7.3-Kiem-tra-output-tren-Amazon-S3/image-004.png)

Kết quả sau khi hoàn thành Glue ETL Job. Sau khi hoàn tất bước này, đã có dữ liệu curated ở định dạng Parquet trong Amazon S3.

**Kết quả đạt được:**

- Dữ liệu raw CSV đã được xử lý bằng AWS Glue ETL

- Dữ liệu được làm sạch và cast đúng kiểu dữ liệu

- Dữ liệu events và transactions được partition theo year/month/day

- Dữ liệu products được lưu thành bảng dimension

- Transaction lỗi được tách riêng vào vùng error/transactions/

- Dữ liệu curated đã sẵn sàng để tạo Glue Crawler và truy vấn bằng Athena

Bước tiếp theo là tạo Glue Data Catalog cho curated data để Athena có thể truy vấn các bảng Parquet sau ETL.
