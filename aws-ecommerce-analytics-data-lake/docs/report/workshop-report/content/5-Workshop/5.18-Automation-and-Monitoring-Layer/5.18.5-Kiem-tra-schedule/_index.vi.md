---
title: "5.18.5. Kiểm tra schedule"
linkTitle: "5.18.5. Kiểm tra schedule"
menuTitle: "5.18.5. Kiểm tra schedule"
date: 2026-05-29
weight: 685
chapter: false
---

# 5.18.5. Kiểm tra schedule

Sau khi EventBridge Scheduler chạy theo lịch, kiểm tra workflow tại: AWS Glue → Workflows → ecommerce-scheduled-etl-workflow → History (mục 17.2.5)

Ngoài ra, có thể kiểm tra thêm bằng cách truy cập vào dịch vụ AWS Glue, trong tùy chọn bên trái chọn Job run monitoring để xác nhận Glue ETL Job etl_ecommerce_raw_to_curated_1 đã được tự động chạy theo lịch mỗi ngày lúc 9:00.

Trong hình ta thấy các job đã được tự động chạy mỗi ngày 1 lần theo lịch vào lúc 9:00 kể từ ngày tạo Workflow (25/05/2026)

![](/images/5-Workshop/5.18.5-Kiem-tra-schedule/image-001.png)
