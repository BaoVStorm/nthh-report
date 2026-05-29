---
title: "5.10. Tạo Athena Views cho analytics"
linkTitle: "5.10. Tạo Athena Views cho analytics"
menuTitle: "5.10. Tạo Athena Views cho analytics"
date: 2026-05-29
weight: 600
chapter: false
---

Sau khi dữ liệu curated đã được tạo và crawl vào Glue Data Catalog, bước tiếp theo là tạo các **Athena Views** phục vụ phân tích.

Thay vì để QuickSight truy vấn trực tiếp vào các bảng curated, ta sẽ tạo các business views trong Athena. Như vậy sẽ làm cho project giống thực tế hơn vì:

- Tách phần xử lý logic business ra khỏi dashboard

- Giúp QuickSight dễ sử dụng hơn

- Giảm việc phải viết lại công thức nhiều lần trong dashboard

- Dữ liệu đưa vào dashboard đã được tổng hợp theo đúng mục tiêu phân tích

**Các view chính sẽ được sử dụng gồm:**

- vw_daily_event_funnel

- vw_traffic_source_performance

- vw_discount_refund_analysis

- vw_ab_testing_summary

- vw_executive_overview

- vw_product_revenue

- vw_campaign_performance

- vw_daily_funnel_by_source_device

- vw_funnel_summary

### 1.  View: Daily event funnel

View này dùng để phân tích funnel hành vi người dùng theo từng ngày, gồm các bước: **view → click → add_to_cart → purchase**.

View này giúp trả lời:

- Mỗi ngày có bao nhiêu lượt view, click, add to cart và purchase?

- Tỷ lệ chuyển đổi giữa các bước funnel là bao nhiêu?

- Bounce rate theo ngày có cao không?

Chạy câu SQL sau trong Athena:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_daily_event_funnel AS
SELECT
event_date,
COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_click_rate,

ROUND(
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END), 0),
4
) AS click_to_cart_rate,

ROUND(
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_cart_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END), 0),
4
) AS cart_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY event_date;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-001.png)

Sau khi tạo view, kiểm tra bằng câu query:

```sql
SELECT * FROM "ecommerce_curated"."vw_daily_event_funnel";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-002.png)

### 2. View: Discount and refund analysis

View này dùng để phân tích mối quan hệ giữa discount và refund.

View này giúp trả lời:

- Các mức discount khác nhau có ảnh hưởng đến refund rate không?

- Ngày nào có refund cao?

- Tổng revenue và average revenue thay đổi như thế nào theo discount?

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_discount_refund_analysis AS
SELECT
transaction_date,
discount_applied,
COUNT(*) AS total_transactions,
SUM(gross_revenue) AS total_revenue,
AVG(gross_revenue) AS avg_revenue,
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) AS refunded_transactions,
ROUND(
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS refund_rate
FROM ecommerce_curated.curated_fact_transactions
GROUP BY
transaction_date,
discount_applied;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-003.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_discount_refund_analysis";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-004.png)

### 3. View: Traffic Source Performance

View này dùng để đánh giá hiệu quả của từng nguồn traffic theo từng ngày.

View này giúp trả lời:

- Traffic source nào mang lại nhiều view, click, purchase nhất?

- Organic, Paid Search, Social, Email hay Direct có conversion rate tốt hơn?

- Nguồn traffic nào có bounce rate cao?

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_traffic_source_performance AS
SELECT
event_date,
traffic_source,

COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
traffic_source;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-005.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_traffic_source_performance";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-006.png)

### 4. View: A/B Testing Summary

View này dùng để phân tích hiệu quả giữa các nhóm thử nghiệm A/B testing.

View này giúp trả lời:

- Experiment group nào có conversion rate cao hơn?

- Nhóm nào có add to cart rate tốt hơn?

- Nhóm nào có bounce rate thấp hơn?

- Session duration trung bình của từng nhóm là bao nhiêu?

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_ab_testing_summary AS
SELECT
event_date,
experiment_group,
COUNT(*) AS total_events,
SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,
AVG(session_duration_sec) AS avg_session_duration,
ROUND(SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 / NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0), 4) AS conversion_rate,
ROUND(SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 / NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0), 4) AS add_to_cart_rate,
ROUND(SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(*), 0), 4) AS bounce_rate
FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
experiment_group;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-007.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_ab_testing_summary";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-008.png)

### 5. View: Executive Overview

View này dùng cho dashboard tổng quan cấp quản lý. Đây là view chính cho Dashboard 1 — Executive Overview.

View này giúp trả lời:

- Doanh thu tăng hay giảm?

- Số lượng đơn hàng thay đổi như thế nào?

- Giá trị đơn hàng trung bình là bao nhiêu?

- Refund rate có đang tăng bất thường không?

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_executive_overview AS
SELECT
transaction_date,
COUNT(*) AS total_orders,
SUM(quantity) AS total_units_sold,
SUM(gross_revenue) AS total_revenue,
AVG(gross_revenue) AS avg_order_value,
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) AS refunded_orders,
ROUND(
SUM(CASE WHEN is_refunded = true THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS refund_rate
FROM ecommerce_curated.curated_fact_transactions
GROUP BY transaction_date;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-009.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_executive_overview";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-010.png)

### 6. View: vw_product_revenue

View này dùng để phân tích doanh thu theo sản phẩm, category, brand và nhóm premium.

View này giúp trả lời:

- Product nào tạo nhiều revenue nhất?

- Category nào bán tốt nhất?

- Brand nào mạnh nhất?

- Premium product có hiệu quả không?

- Product hoặc category nào có refund rate cao?

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_product_revenue AS
SELECT
t.transaction_date,
p.product_id,
p.category,
p.brand,
p.is_premium,
COUNT(t.transaction_id) AS total_transactions,
SUM(t.quantity) AS total_units_sold,
SUM(t.gross_revenue) AS total_revenue,
AVG(t.gross_revenue) AS avg_transaction_value,
SUM(CASE WHEN t.is_refunded = true THEN 1 ELSE 0 END) AS refunded_transactions,
ROUND(
SUM(CASE WHEN t.is_refunded = true THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(t.transaction_id), 0), 4) AS refund_rate
FROM ecommerce_curated.curated_fact_transactions t
LEFT JOIN ecommerce_curated.curated_dim_products p
ON t.product_id = p.product_id
GROUP BY
t.transaction_date,
p.product_id,
p.category,
p.brand,
p.is_premium;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-011.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_product_revenue";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-012.png)

### 7. View: Campaign Performance

View này dùng để phân tích hiệu quả của từng campaign theo ngày và traffic source.

View này giúp trả lời:

- Campaign nào có nhiều view, click và purchase nhất?

- Campaign nào có conversion rate cao?

- Campaign nào có bounce rate cao?

- Traffic source nào hỗ trợ campaign hiệu quả nhất?

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_campaign_performance AS
SELECT
event_date,
campaign_id,
traffic_source,

COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS conversion_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
campaign_id,
traffic_source;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-013.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_campaign_performance";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-014.png)

### 8. View: Daily Funnel by Source and Device

View này dùng để phân tích funnel theo cả traffic source và device type.

View này giúp trả lời:

- Funnel theo từng nguồn traffic có khác nhau không?

- Mobile, desktop hoặc tablet có conversion rate khác nhau không?

- Nguồn traffic nào trên thiết bị nào đang có bounce rate cao?

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_daily_funnel_by_source_device AS
SELECT
event_date,
traffic_source,
device_type,

COUNT(*) AS total_events,

SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_carts,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) AS bounces,

ROUND(
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS view_to_click_rate,

ROUND(
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END), 0),
4
) AS click_to_cart_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END), 0),
4
) AS cart_to_purchase_rate,

ROUND(
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END), 0),
4
) AS conversion_rate,

ROUND(
SUM(CASE WHEN event_type = 'bounce' THEN 1 ELSE 0 END) * 1.0 /
NULLIF(COUNT(*), 0),
4
) AS bounce_rate

FROM ecommerce_curated.curated_fact_events
GROUP BY
event_date,
traffic_source,
device_type;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-015.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_daily_funnel_by_source_device";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-016.png)

### 9. View: Funnel Summary

View này dùng để tạo funnel chart trong QuickSight. Dữ liệu được chuyển từ dạng nhiều cột sang dạng từng stage để dễ trực quan hóa.

View này giúp hiển thị funnel theo các bước **Views → Clicks → Add to Cart → Purchases**.

Chạy câu SQL sau:

```sql
CREATE OR REPLACE VIEW ecommerce_curated.vw_funnel_summary AS
SELECT
event_date,
'01 Views' AS funnel_stage,
SUM(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date
UNION ALL
SELECT
event_date,
'02 Clicks' AS funnel_stage,
SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date
UNION ALL
SELECT
event_date,
'03 Add to Cart' AS funnel_stage,
SUM(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date
UNION ALL
SELECT
event_date,
'04 Purchases' AS funnel_stage,
SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS funnel_count
FROM ecommerce_curated.curated_fact_events
GROUP BY event_date;
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-017.png)

Kiểm tra view:

```sql
SELECT * FROM "ecommerce_curated"."vw_funnel_summary";
```

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-018.png)

### Kiểm tra danh sách views đã tạo:

Sau khi tạo xong các view, kiểm tra trong Athena hoặc Glue Data Catalog để đảm bảo các view đã xuất hiện trong database **ecommerce_curated**.

![](/images/5-Workshop/5.10-Tao-Athena-Views-cho-analytics/image-019.png)

Vậy là đã có đầy đủ các view cần thiết để thực hiện visualize.
