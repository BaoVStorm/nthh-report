---
title: "Worklog Tuần 8"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

## Worklog Tuần 8: Athena Views và semantic layer

**Thời gian:** 20/04/2026 - 24/04/2026

### Mục tiêu tuần 8:

* Tìm hiểu vai trò của semantic layer trong hệ thống phân tích dữ liệu.
* Tạo các Athena Views phục vụ dashboard.
* Viết SQL để tổng hợp dữ liệu business-ready.
* Chuẩn bị dữ liệu cho các dashboard Executive, Funnel, Marketing, Product và A/B Testing.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ 2 | - Tìm hiểu semantic layer và vai trò của Athena Views.<br>- Xác định các dashboard cần xây dựng.<br>- Lập danh sách view cần tạo cho Executive, Funnel, Marketing, Product và A/B Testing.<br>- Chuẩn bị SQL template cho các view. | 20/04/2026 | 20/04/2026 | Amazon Athena Documentation |
| Thứ 3 | - Tạo view vw_executive_overview.<br>- Tính total_orders, total_units_sold, total_revenue, avg_order_value và refund_rate.<br>- Query kiểm tra kết quả view.<br>- Ghi chú ý nghĩa business của view. | 21/04/2026 | 21/04/2026 | SQL, Athena |
| Thứ 4 | - Tạo view vw_daily_event_funnel và vw_funnel_summary.<br>- Tính views, clicks, add_to_carts, purchases và các conversion rate.<br>- Kiểm tra logic funnel bằng Athena.<br>- Ghi chú cách view này phục vụ Funnel Dashboard. | 22/04/2026 | 22/04/2026 | SQL, Athena |
| Thứ 5 | - Tạo view vw_traffic_source_performance và vw_campaign_performance.<br>- Tính conversion rate, bounce rate và campaign performance.<br>- Kiểm tra kết quả theo traffic_source và campaign_id.<br>- Ghi chú phần Marketing Analytics. | 23/04/2026 | 23/04/2026 | SQL, Athena |
| Thứ 6 | - Tạo view vw_product_revenue và vw_ab_testing_summary.<br>- Join transaction với product để phân tích category/brand/premium.<br>- Tính chỉ số A/B Testing theo experiment_group.<br>- Tổng hợp danh sách views đã tạo và cập nhật report. | 24/04/2026 | 24/04/2026 | SQL, Athena |

### Kết quả đạt được tuần 8:

* Hiểu được lý do cần tạo Athena Views thay vì để QuickSight truy vấn trực tiếp các bảng curated.
* Tạo được các view phục vụ phân tích, bao gồm:
* vw_executive_overview
* vw_daily_event_funnel
* vw_funnel_summary
* vw_traffic_source_performance
* vw_campaign_performance
* vw_product_revenue
* vw_ab_testing_summary
* Viết được các câu SQL sử dụng:
* COUNT
* SUM
* AVG
* CASE WHEN
* ROUND
* NULLIF
* GROUP BY
* JOIN
* Tính được các chỉ số quan trọng như total revenue, total orders, average order value, refund rate, conversion rate, bounce rate và funnel rate.
* Kiểm tra được kết quả của từng view trước khi đưa vào QuickSight.
* Hoàn thành lớp semantic layer phục vụ trực quan hóa dữ liệu.
