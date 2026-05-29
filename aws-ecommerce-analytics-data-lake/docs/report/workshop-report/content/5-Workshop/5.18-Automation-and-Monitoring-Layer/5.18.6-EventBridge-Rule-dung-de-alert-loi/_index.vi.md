---
title: "5.18.6. EventBridge Rule dùng để alert lỗi"
linkTitle: "5.18.6. EventBridge Rule dùng để alert lỗi"
menuTitle: "5.18.6. EventBridge Rule dùng để alert lỗi"
date: 2026-05-29
weight: 686
chapter: false
---

# 5.18.6. EventBridge Rule dùng để alert lỗi

Ta sẽ sử dụng EventBridge để tạo rule bắt các lỗi:

- Raw Crawler Failed

- Glue ETL Job FAILED / TIMEOUT / STOPPED

- Curated Crawler Failed

Rồi gửi về Email đã được đăng ký trong SNS Email subscription.

#### Tạo EventBridge Rule

Truy cập AWS Management Console, tìm kiếm và chọn dịch vụ Amazon EventBridge.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-001.png)

Ở màn hình chính, chọn Create rule.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-002.png)

#### Tạo alert khi Raw Crawler hoặc Curated Crawler failed

Trong phần Builder mode, chọn Advanced builder.

Sau đó màn hình sẽ hiển thị các bước cấu hình cho Rule, ở bước Define rule detail ta cấu hình như sau:

- Name: alert-ecommerce-crawler-failed

Nhấn Next.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-003.png)

Ở bước Build event pattern, ta chọn Custom pattern (JSON editor) rồi dán đoạn JSON sau vào ô Event pattern:

```json
{
"source": ["aws.glue"],
"detail-type": ["Glue Crawler State Change"],
"detail": {
"crawlerName": [
"crawler_ecommerce_raw",
"crawler_ecommerce_curated"
],
"state": ["Failed"]
}
}
```

Sau đó nhấn Next.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-004.png)

Tiếp theo là đến bước Select target(s), ta cấu hình như sau:

- Target types: AWS service

```sql
Select a target: SNS Topic
```

- Target location: Target in this account

- Topic: ecommerce-etl-alerts

- Execution role: Create a new role for this specific resource

Sau đó nhấn Next.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-005.png)

Review lại các cấu hình, sau đó nhấn Create rule.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-006.png)

EventBridge Rule cho crawler đã tạo thành công.

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-007.png)

AWS Glue crawler state change events có các trạng thái như Started, Succeeded, và Failed, nên rule này sẽ gửi SNS khi raw crawler hoặc curated crawler fail.

#### Tạo alert khi Glue ETL Job failed

Tạo rule alert khi Glue ETL Job failed các thao tác tương tự như tạo rule cho crawler, cấu hình như sau:

- Name: alert-ecommerce-glue-job-failed

- JSON:

```json
{
"source": ["aws.glue"],
"detail-type": ["Glue Job State Change"],
"detail": {
"jobName": ["etl_ecommerce_raw_to_curated_1"],
"state": ["FAILED", "TIMEOUT", "STOPPED"]
}
}
```

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-008.png)

Rule đã tạo thành công

![](/images/5-Workshop/5.18.6-EventBridge-Rule-dung-de-alert-loi/image-009.png)

Rule này quan trọng nhất vì nó bắt lỗi ETL chính. Khi Glue job bị FAILED, TIMEOUT, hoặc STOPPED thì sẽ nhận email qua SNS. AWS Glue job state change events được EventBridge hỗ trợ để phản ứng với trạng thái job.
