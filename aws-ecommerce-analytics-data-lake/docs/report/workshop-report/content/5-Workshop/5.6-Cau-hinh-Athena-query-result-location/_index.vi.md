---
title: "5.6. Cấu hình Athena query result location"
linkTitle: "5.6. Cấu hình Athena query result location"
menuTitle: "5.6. Cấu hình Athena query result location"
date: 2026-05-29
weight: 560
chapter: false
---

**Amazon Athena** cần một vị trí trong Amazon S3 để lưu kết quả truy vấn. Vì vậy, trước khi thực hiện query dữ liệu, cần cấu hình **Query result location cho Athena**.

Trong project này, kết quả truy vấn của Athena sẽ được lưu tại folder: 

**s3:// ecommerce-analytics-datalake-270642943130-ap-southeast-1-an/athena-results/**

### Truy cập Amazon Athena

Tìm và chọn dịch vụ **Amazon Athena** trên thanh tìm kiếm:

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-001.png)

### Cấu hình Query result location

Trong giao diện **Athena Query editor**, chọn **Edit settings**.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-002.png)

Tiếp theo, chọn **Manage** để cấu hình vị trí lưu kết quả truy vấn.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-003.png)

Tại phần **Query result location**, nhấn **Browse S3**.

Chọn bucket S3 đã tạo, sau đó chọn folder **athena-results/**. Nhấn **Choose** để xác nhận vị trí lưu kết quả.

Sau đó nhấn **Save** để lưu cấu hình.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-004.png)

Sau khi lưu thành công, Athena đã được cấu hình vị trí lưu query result trong S3.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-005.png)

### Query thử raw data bằng Athena

Sau khi cấu hình query result location, tiến hành kiểm tra dữ liệu raw đã được Glue Crawler tạo metadata trong Glue Data Catalog.

Trong giao diện **Query editor**, cấu hình như sau:

- Data source: **AwsDataCatalog**

- Database: **ecommerce_raw**

- Chọn **raw_events**

Sau đó chọn **Preview Table** để Athena tự động tạo câu lệnh truy vấn thử dữ liệu.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-006.png)

### Truy vấn thử 10 dòng dữ liệu từ bảng raw_events

Athena sẽ tự động sinh câu lệnh truy vấn tương tự như sau:

```sql
SELECT *
FROM "ecommerce_raw"."raw_events"
LIMIT 10;
```

Truy vấn chạy thành công, kết quả sẽ hiển thị 10 dòng dữ liệu đầu tiên của bảng raw_events.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-007.png)

Sau khi query thành công, kiểm tra các thông tin:

- Dữ liệu có hiển thị đúng không

- Tên cột có đúng với file CSV ban đầu không

- Kiểu dữ liệu có hợp lý không

- Có bị lỗi header, null hoặc lệch cột không

Dữ liệu hiển thị đúng, nghĩa là bảng raw_events đã được Glue Crawler tạo metadata thành công và Athena có thể đọc được dữ liệu từ S3.

Thực hiện tương tự với hai bảng **raw_products**, **raw_transactions**.

#### Kiểm tra bảng raw_products

```sql
SELECT *
FROM "ecommerce_raw"."raw_products"
LIMIT 10;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-008.png)

#### Kiểm tra bảng raw_transactions

```sql
SELECT *
FROM "ecommerce_raw"."raw_transactions"
LIMIT 10;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-009.png)

Cả ba bảng đều truy vấn thành công, dữ liệu raw trong S3 đã sẵn sàng để sử dụng cho bước xử lý ETL bằng AWS Glue.

### Kiểm tra dữ liệu bằng các câu query tổng hợp

Sau khi kiểm tra preview dữ liệu, tiếp tục chạy một số câu query tổng hợp để kiểm tra logic dữ liệu trong từng bảng.

#### Kiểm tra số lượng event theo từng loại sự kiện

Câu query sau dùng để đếm số lượng bản ghi theo từng event_type trong bảng raw_events.

```sql
SELECT
event_type,
COUNT(*) AS event_count
FROM "ecommerce_raw"."raw_events"
GROUP BY event_type
ORDER BY event_count DESC;
```

Kết quả truy vấn cho biết mỗi loại sự kiện xuất hiện bao nhiêu lần trong dữ liệu raw.

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-010.png)

#### Kiểm tra số lượng sản phẩm theo từng category

Câu query sau dùng để đếm số lượng sản phẩm theo từng category trong bảng raw_products.

```sql
SELECT
category,
COUNT(*) AS category_count
FROM "ecommerce_raw"."raw_products"
GROUP BY category
ORDER BY category_count DESC;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-011.png)

Kết quả truy vấn giúp kiểm tra dữ liệu sản phẩm đang được phân loại theo những nhóm category nào.

#### Kiểm tra số lượng giao dịch theo quantity

Câu query sau dùng để đếm số lượng giao dịch theo từng giá trị quantity trong bảng raw_transactions.

```sql
SELECT
quantity,
COUNT(*) AS quantity_count
FROM "ecommerce_raw"."raw_transactions"
GROUP BY quantity
ORDER BY quantity_count DESC;
```

![](/images/5-Workshop/5.6-Cau-hinh-Athena-query-result-location/image-012.png)

Kết quả truy vấn giúp kiểm tra phân bố số lượng sản phẩm trong các giao dịch.

#### Kết luận

Sau khi chạy thành công các câu query trên, có thể xác nhận rằng:

- Athena đã được cấu hình đúng query result location

- Glue Data Catalog đã nhận diện được metadata của dữ liệu raw

- Các bảng **raw_events**, **raw_products** và **raw_transactions** có thể được truy vấn thành công

- Dữ liệu raw trong S3 đã sẵn sàng cho bước xử lý ETL bằng AWS Glue

Ở bước tiếp theo, project sẽ tiến hành tạo Glue ETL Job để chuyển đổi dữ liệu từ tầng raw sang tầng curated.
