---
title: "5.8. Tạo Glue Data Catalog cho Curated Data"
linkTitle: "5.8. Tạo Glue Data Catalog cho Curated Data"
menuTitle: "5.8. Tạo Glue Data Catalog cho Curated Data"
date: 2026-05-29
weight: 580
chapter: false
---

Sau khi Glue ETL Job chạy thành công, dữ liệu đã được ghi vào tầng **curated/** dưới định dạng Parquet. Ở bước này, ta sẽ tạo Glue Database và Glue Crawler mới để crawl dữ liệu Parquet trong tầng curated. Sau khi crawler chạy xong, Athena có thể truy vấn trực tiếp các bảng curated.

Dữ liệu curated hiện có trong S3 gồm:
```
curated/
├── fact_events/
├── dim_products/
└── fact_transactions/
```

Sau khi crawler chạy thành công, Glue Data Catalog sẽ tạo ra **3 bảng**:

- curated_fact_events

- curated_dim_products

- curated_fact_transactions
