---
title: "5.18.2. Tạo Glue Workflow"
linkTitle: "5.18.2. Tạo Glue Workflow"
menuTitle: "5.18.2. Tạo Glue Workflow"
date: 2026-05-29
weight: 682
chapter: false
---

# 5.18.2. Tạo Glue Workflow

Glue Workflow dùng để gom các bước pipeline thành một luồng xử lý có thứ tự.

Luồng workflow cần tạo:

Start Workflow
      |
      v
crawler_ecommerce_raw
      |
      v
etl_ecommerce_raw_to_curated_1
      |
      v
crawler_ecommerce_curated

#### Tạo Workflow:

Truy cập AWS Glue -> Workflows nhấn Add workflow

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-001.png)

- Workflow name: ecommerce-scheduled-etl-workflow.

Sau đó nhấn Create workflow để tạo workflow.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-002.png)

Workflow đã được tạo thành công. Truy cập vào workflow đã tạo và tiến hành tạo trigger.

Nhấn Add trigger để tạo trigger.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-003.png)

#### Trigger 1: Start Raw Crawler

Trigger đầu tiên dùng để chạy raw crawler khi workflow bắt đầu.

Ta cấu hình trigger như sau:

- Name: trigger-start-raw-crawler

- Description: Start raw crawler when workflow starts

- Trigger type: On demand

Sau đó nhấn Add.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-004.png)

Sau khi tạo trigger, ta gắn action cho trigger này bằng cách nhấn nút Action, chọn Add job/crawler to trigger.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-005.png)

Trong Add job(s) and crawler(s) to trigger:

- Chọn tab Crawler

- Chọn crawler  crawler_ecommerce_raw

Sau đó nhấn Add.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-006.png)

Graph sau khi hoàn thành xong trigger 1 sẽ có hình dạng như sau:

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-007.png)

#### Trigger: Raw Crawler thành công thì chạy ETL Job

Trigger thứ hai dùng để chạy Glue ETL Job sau khi raw crawler chạy thành công.

Sau khi đã có node Raw Crawler, ta tạo trigger thứ hai bằng cách chọn node crawler_ecommerce_raw và nhấn Add trigger

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-008.png)

Tiếp theo, gắn action cho trigger này, nhấn nút Action, chọn Add jobs/crawlers to watch.

Sau đó nhấn Add node, rồi cấu hình trigger như sau:

- Name: trigger-after-raw-crawler-success

- Description: Start ETL job after raw crawler succeeds

- Trigger type: Event

- Trigger logic: Start after ANY watched event

Sau đó nhấn Add để them trigger.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-009.png)

Sau khi node được tạo thành công, nhấn Add node. Trong Add job(s) and crawler(s) to trigger:

- Chọn tab: Jobs

- Chọn Glue Job: etl_ecommerce_raw_to_curated_1

Sau đó nhấn Add.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-010.png)

Add thành công trigger ta có graph của Workflow như hình dưới. Ở bước này, trigger đang watch crawler nhưng action là run job.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-011.png)

#### Trigger 3: ETL Job thành công thì chạy Curated Crawler

Trigger thứ ba dùng để chạy curated crawler sau khi Glue ETL Job chạy thành công.

Từ node etl_ecommerce_raw_to_curated_1, nhấn Add trigger rồi cấu hình trigger như sau:

- Name: trigger-after-etl-success

- Description: Start curated crawler after ETL job succeeds

- Trigger type: Event

- Trigger logic: Start after ANY watched event

Sau đó nhấn Add

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-012.png)

Nhấn Add node. Trong Add job(s) and crawler(s) to trigger:

- Chọn tab: Crawler

- Chọn Crawler: crawler_ecommerce_curated

Nhấn Add

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-013.png)

Sau khi tạo hoàn tất 3 Trigger thì ta sẽ có workflow graph như sau:

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-014.png)

#### Run Glue Workflow

Sau khi tạo xong workflow, nhấn Run workflow.

Sau khi workflow chạy xong và Status là Completed nghĩa là workflow đã chạy thành công thì nhấn vào tab History để check workflow.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-015.png)

Chọn workflow run mới nhất, sau đó nhấn View run details.

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-016.png)

Kiểm tra từng node trong graph, ta thấy:

- crawler_ecommerce_raw đã chạy thành công

- etl_ecommerce_raw_to_curated_1 đã chạy thành công

- crawler_ecommerce_curated đã chạy thành công

![](/images/5-Workshop/5.18.2-Tao-Glue-Workflow/image-017.png)
