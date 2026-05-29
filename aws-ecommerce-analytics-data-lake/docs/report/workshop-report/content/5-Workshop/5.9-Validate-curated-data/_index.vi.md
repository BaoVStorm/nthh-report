---
title: "5.9. Validate curated data"
linkTitle: "5.9. Validate curated data"
menuTitle: "5.9. Validate curated data"
date: 2026-05-29
weight: 590
chapter: false
---

Trước khi xây dựng dashboard trên QuickSight, cần kiểm tra dữ liệu ở tầng curated để đảm bảo dữ liệu đã được xử lý đúng.

**Mục tiêu của bước validate là:**

- Kiểm tra số dòng của từng bảng

- Kiểm tra dữ liệu phân loại như event_type, category

- Kiểm tra dữ liệu doanh thu và refund

- Đảm bảo dữ liệu curated có thể sử dụng cho phân tích và dashboard

### Kiểm tra số dòng từng bảng

Số lượng dòng:

- events = 2,000,000

- products = 2,000

- transactions <= 103,127 (transactions nhỏ hơn 103,127 vì Glue ETL đã đưa record lỗi sang error/transactions/).

### Kiểm tra event type

Chạy câu query sau để kiểm tra số lượng bản ghi theo từng loại event:

```sql
SELECT
event_type,
COUNT(*) AS event_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_type
ORDER BY event_count DESC;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-001.png)

Kết quả truy vấn giúp kiểm tra:

- Có những loại event nào trong dữ liệu

- Số lượng từng loại event có hợp lý không

- Có giá trị bất thường như null, rỗng hoặc sai định dạng không

### Kiểm tra product category

Chạy câu query sau để kiểm tra số lượng sản phẩm theo từng category:

```sql
SELECT
category,
COUNT(*) AS product_count
FROM ecommerce_curated.curated_dim_products
GROUP BY category
ORDER BY product_count DESC;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-002.png)

Kết quả truy vấn giúp kiểm tra:

- Các nhóm category sản phẩm

- Số lượng sản phẩm trong từng category

### Kiểm tra revenue âm và refund

Chạy câu query sau để kiểm tra tổng doanh thu theo trạng thái refund:
```sql
SELECT
is_refunded,
COUNT(*) AS transaction_count,
SUM(gross_revenue) AS total_revenue
FROM ecommerce_curated.curated_fact_transactions
GROUP BY is_refunded;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-003.png)

Câu query này giúp kiểm tra logic xử lý transaction sau ETL.

**Kết quả:**

- Các transaction có is_refunded = true có thể có gross_revenue âm

- Các transaction có is_refunded = false không có gross_revenue âm

- Những record có gross_revenue < 0 nhưng is_refunded = false đã được đưa sang error/transactions/

### Kiểm tra transaction âm không hợp lệ

Để chắc chắn rằng các transaction có doanh thu âm nhưng không phải refund đã bị loại khỏi curated layer, chạy query:

```sql
SELECT
    COUNT(*) AS invalid_negative_revenue_count
FROM ecommerce_curated.curated_fact_transactions
WHERE gross_revenue < 0
  AND is_refunded = false;
  ```

Kết quả:

![](/images/5-Workshop/5.9-Validate-curated-data/image-004.png)

Vậy là logic validate trong Glue ETL Job đã loại bỏ hết transaction lỗi.

### Kiểm tra dữ liệu null quan trọng trong fact_transactions

Chạy query sau để kiểm tra các cột quan trọng trong bảng transaction:

```sql
SELECT
SUM(CASE WHEN transaction_id IS NULL THEN 1 ELSE 0 END) AS null_transaction_id,
SUM(CASE WHEN transaction_timestamp IS NULL THEN 1 ELSE 0 END) AS null_transaction_timestamp,
SUM(CASE WHEN product_id IS NULL THEN 1 ELSE 0 END) AS null_product_id,
SUM(CASE WHEN gross_revenue IS NULL THEN 1 ELSE 0 END) AS null_gross_revenue
FROM ecommerce_curated.curated_fact_transactions;
```

![](/images/5-Workshop/5.9-Validate-curated-data/image-005.png)

Kết quả cho thấy:

- null_transactions_id = 0

- null_transaction_timestamp = 0

- null_product_id = 0

- null_gross_revenue = 0

Các cột này là những cột đã được dùng trong logic validate của Glue ETL Job, vì vậy dữ liệu hợp lệ trong curated layer không được còn lỗi ở các trường này.

#### Kết luận

Sau khi hoàn tất bước validate, có thể xác nhận rằng:

- Dữ liệu curated đã được crawl thành công vào Glue Data Catalog

- Athena có thể query được các bảng Parquet trong tầng curated

- Các bảng fact_events, dim_products, fact_transactions đã có schema đúng

- Dữ liệu đã được làm sạch và chuyển đổi kiểu dữ liệu phù hợp

- Dữ liệu transaction lỗi đã được loại khỏi bảng curated_fact_transactions

- Tầng curated đã sẵn sàng để kết nối với Amazon QuickSight và xây dựng dashboard phân tích

Sau bước này, project có thể chuyển sang phần kết nối Athena với QuickSight để trực quan hóa dữ liệu.
