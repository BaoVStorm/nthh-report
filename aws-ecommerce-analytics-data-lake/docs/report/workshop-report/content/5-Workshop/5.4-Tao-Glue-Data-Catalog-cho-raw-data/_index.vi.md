---
title: "5.4. Tạo Glue Data Catalog cho raw data"
linkTitle: "5.4. Tạo Glue Data Catalog cho raw data"
menuTitle: "5.4. Tạo Glue Data Catalog cho raw data"
date: 2026-05-29
weight: 540
chapter: false
---


Mục tiêu của bước này là tạo **AWS Glue Data Catalog** để lưu metadata của các file CSV trong Amazon S3. Sau khi có Data Catalog, Amazon Athena có thể đọc và truy vấn dữ liệu raw từ S3.

Trong project này, dữ liệu raw gồm 3 nhóm file:

- raw/events/

- raw/products/

- raw/transactions/

Sau khi crawler chạy thành công, Glue sẽ tự động tạo schema và bảng metadata tương ứng cho từng nhóm dữ liệu.

**Luồng tiếp theo:**

S3 raw -> Glue IAM Role -> Glue Database -> Glue Crawler raw -> Run crawler -> Kiểm tra bảng trong Glue Data Catalog -> Query thử bằng Athena
