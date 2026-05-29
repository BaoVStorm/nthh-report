---
title: "5.2. Kaggle Dataset preprocessing locally"
linkTitle: "5.2. Kaggle Dataset preprocessing locally"
menuTitle: "5.2. Kaggle Dataset preprocessing locally"
date: 2026-05-29
weight: 520
chapter: false
---

### Explore dataset:

- Link: https://www.kaggle.com/datasets/geethasagarbonthu/marketing-and-e-commerce-analytics-dataset

- The dataset is generated from Python, using 3 files: **events.csv**, **products.csv**, **transactions.csv**

#### events.csv: 2000000 records

- A fact table containing user interactions: **views**, **clicks**, **add-to-cart**, **bounces**, **purchases**

- Includes metadata such as **device type**, **traffic source**, **page category**, and **session duration**.

- **campaign_id** and **experiment_group** support uplift analysis and A/B testing analysis.

- Data has real-world noise: missing device type information, inconsistent capitalization of traffic source values.

- The primary key is **event_id**, with foreign keys linking to the customers, products, and campaigns tables.

**Table data information:**

| # | Column | Dtype | Non-null | Describe |
| --- | --- | --- | --- | --- |
| 0 | event_id | int64 | X |  |
| 1 | timestamp | str | X | 01-01-2021 -> 31-12-2023<br>Template: yyyy/mm/dd hh:mm |
| 2 | customer_id | int64 | X |  |
| 3 | session_id | int64 | X |  |
| 4 | event_type | str | X | 'view': 1043573<br>'click': 379008<br>'add_to_cart': 284370<br>'bounce': 189922<br>'purchase': 103127 |
| 5 | product_id | float64 | Missing 200371 |  |
| 6 | device_type | str | Missing 40300 | 'mobile': 1176146<br>'desktop': 685433<br>'tablet': 98121<br>Nan -> fill with 'unknown' |
| 7 | traffic_source | str | x | 'Organic': 776758<br>'Paid Search': 387657<br>'Social': 291194<br>'Email': 290651<br>'Direct': 193870<br>'ORGANIC': 23731<br>'PAID SEARCH': 12181<br>'SOCIAL': 9077<br>'EMAIL': 8989<br>'DIRECT': 5892 |
| 8 | campaign_id | int64 | X |  |
| 9 | page_category | str | X | 'PLP': 601284<br>'PDP' 599638<br>'Home' 399723<br>'Checkout' 199871<br>'Cart': 199484 |
| 10 | session_duration_sec | float64 | X |  |
| 11 | experiment_group | str | X | 'Control': 1198404<br>'Variant_A': 401413<br>'Variant_B': 400183 |

#### products.csv: 2000 records

- Each row corresponds to a product in the catalog, including metadata about **category** and **brand**.

- The **base_price** value reflects the actual price distribution for each product category.

- Includes the product launch date for product lifecycle analysis.

- **is_premium** is used to identify product segments with a higher price point.

- The primary key is **product_id**, used to link with the events and transactions tables.

**Table data information:**

| # | Column | Dtype | Non-null | Describe |
| --- | --- | --- | --- | --- |
| 0 | product_id | int64 | X |  |
| 1 | category | str | X | 'Electronics': 455<br>'Fashion': 418<br>'Home': 396<br>'Grocery': 312<br>'Sports': 218<br>'Beauty': 201 |
| 2 | brand | str | X | Brand_1 -> Brand_100 |
| 3 | base_price | float64 | X |  |
| 4 | launch_date | str | X | yyyy/mm/dd |
| 5 | is_premium | int64 | X | 0; 1 |

#### transactions.csv: 103127 records

- Each row is a completed purchase transaction.

- Includes **quantity**, **discounts_applied**, and **gross revenue** (where refunds are recorded as negative values).

- Directly linked to purchase events through **timestamp** and **customer/product IDs**.

- Supports analysis of revenue, refund behavior, and campaign effectiveness.

- The primary key is **transaction_id**, referencing the customers, products, and campaigns tables.

**Table data information:**

| # | Column | Dtype | Not-null | Describe |
| --- | --- | --- | --- | --- |
| 0 | transaction_id | int64 | X |  |
| 1 | timestamp | str | X | yyyy/mm/dd |
| 2 | customer_id | int64 | X |  |
| 3 | product_id | float64 | Missing 10449 | Send to error/quarantine or keep with error flag |
| 4 | quantity | int64 | X | 1 -> 4<br>1: 77352<br>2: 15327<br>3: 7324<br>4: 3124 |
| 5 | discount_applied | float64 | X | 0.0: 61923<br>0.05: 15473<br>0.1: 12370<br>0.15: 8311<br>0.2: 5050 |
| 6 | gross_revenue | float64 | Missing 10449 | 2704 negative values (negative due to refund) |
| 7 | campaign_id | int64 | X |  |
| 8 | refund_flag | int64 | X | 0: 100098<br>1: 3029 (negative or null gross_revenue) |

#### Local preprocessing:

- **events.csv**: Rename column timestamp -> event_timestamp

- **transactions.csv**: timestamp -> transaction_timestamp
