---
title: "5.2. Kaggle Dataset preprocessing ở local"
linkTitle: "5.2. Kaggle Dataset preprocessing ở local"
menuTitle: "5.2. Kaggle Dataset preprocessing ở local"
date: 2026-05-29
weight: 520
chapter: false
---

### Explore dataset:

- Link: https://www.kaggle.com/datasets/geethasagarbonthu/marketing-and-e-commerce-analytics-dataset

- Dataset được sinh từ python, sử dụng 3 files: **events.csv**, **products.csv**, **transactions.csv**

#### events.csv: 2000000 records

- Bảng fact chứa các tương tác của người dùng: **views**, **clicks**, **add-to-cart**, **bounces**, **purchases**

- Bao gồm các metadata như **device type**, **traffic source**,**page category**, và **session duration**.

- **campaign_id** và **experiment_group** hỗ trợ phân tích uplift và phân tích A/B testing.

- Dữ liệu có độ nhiễu thực tế: thiếu thông tin loại thiết bị, cách viết hoa/thường của nguồn truy cập không nhất quán.

- Khóa chính là **event_id**, với các khóa ngoại liên kết đến bảng customers, products, and campaigns.

**Thông tin dữ liệu trong bảng:**

| # | Column | Dtype | Non-null | Describe |
| --- | --- | --- | --- | --- |
| 0 | event_id | int64 | X |  |
| 1 | timestamp | str | X | 01-01-2021 -> 31-12-2023<br>Template: yyyy/mm/dd hh:mm |
| 2 | customer_id | int64 | X |  |
| 3 | session_id | int64 | X |  |
| 4 | event_type | str | X | 'view': 1043573<br>'click': 379008<br>'add_to_cart': 284370<br>'bounce': 189922<br>'purchase': 103127 |
| 5 | product_id | float64 | Thiếu 200371 |  |
| 6 | device_type | str | Thiếu 40300 | 'mobile': 1176146<br>'desktop': 685433<br>'tablet': 98121<br>Nan -> fill bằng ‘unknown’ |
| 7 | traffic_source | str | x | 'Organic': 776758<br>'Paid Search': 387657<br>'Social': 291194<br>'Email': 290651<br>'Direct': 193870<br>'ORGANIC': 23731<br>'PAID SEARCH': 12181<br>'SOCIAL': 9077<br>'EMAIL': 8989<br>'DIRECT': 5892 |
| 8 | campaign_id | int64 | X |  |
| 9 | page_category | str | X | ‘PLP': 601284<br>'PDP' 599638<br>'Home' 399723<br>'Checkout' 199871<br>'Cart': 199484 |
| 10 | session_duration_sec | float64 | X |  |
| 11 | experiment_group | str | X | 'Control': 1198404<br>'Variant_A': 401413<br>'Variant_B': 400183 |

#### products.csv: 2000 records

- Mỗi dòng tương ứng với một sản phẩm trong danh mục, bao gồm metadata về **category** và **brand**.

- Giá trị **base_price** phản ánh phân bố giá thực tế theo từng danh mục sản phẩm.

- Bao gồm thời điểm ra mắt sản phẩm để phân tích vòng đời sản phẩm.

- **is_premium** dùng để xác định các phân khúc sản phẩm có mức giá cao hơn.

- Khóa chính là **product_id** được dùng để liên kết với bảng events và transactions

**Thông tin dữ liệu trong bảng:**

| # | Column | Dtype | Non-null | Describe |
| --- | --- | --- | --- | --- |
| 0 | product_id | int64 | X |  |
| 1 | category | str | X | ‘Electronics’: 455<br>‘Fashion’: 418<br>‘Home’: 396<br>‘Grocery’: 312<br>‘Sports’: 218<br>‘Beauty’: 201 |
| 2 | brand | str | X | Brand_1 -> Brand_100 |
| 3 | base_price | float64 | X |  |
| 4 | launch_date | str | X | yyyy/mm/dd |
| 5 | is_premium | int64 | X | 0; 1 |

#### transactions.csv: 103127 records

- Một dòng là một giao dịch mua hàng đã hoàn tất.

- Bao gồm **quantity**, **discounts_applied**, và **gross revenue** (trong đó các khoản hoàn tiền được ghi nhận bằng giá trị âm).

- Được liên kết trực tiếp với các sự kiện mua hàng thông qua **timestamp** và **customer/product IDs**.

- Hỗ trợ phân tích doanh thu, hành vi hoàn tiền và hiệu quả của campaign.

- Khóa chính là **transaction_id**, tham chiếu đến bảng customers, products và campaigns.

**Thông tin dữ liệu trong bảng:**

| # | Column | Dtype | Not-null | Describe |
| --- | --- | --- | --- | --- |
| 0 | transaction_id | int64 | X |  |
| 1 | timestamp | str | X | yyyy/mm/dd |
| 2 | customer_id | int64 | X |  |
| 3 | product_id | float64 | Thiếu 10449 | Đưa vào error/quarantine hoặc giữ với flag lỗi |
| 4 | quantity | int64 | X | 1 -> 4<br>1: 77352<br>2: 15327<br>3: 7324<br>4: 3124 |
| 5 | discount_applied | float64 | X | 0.0: 61923<br>0.05: 15473<br>0.1: 12370<br>0.15: 8311<br>0.2: 5050 |
| 6 | gross_revenue | float64 | Thiếu 10449 | 2704 giá trị âm (âm vì refund) |
| 7 | campaign_id | int64 | X |  |
| 8 | refund_flag | int64 | X | 0: 100098<br>1: 3029 (gross_revenue âm hoặc null) |

#### Xử lý preprocessing local:

- **events.csv**: Đổi tên cột timestamp -> event_timestamp

- **transactions.csv**: timestamp -> transaction_timestamp
