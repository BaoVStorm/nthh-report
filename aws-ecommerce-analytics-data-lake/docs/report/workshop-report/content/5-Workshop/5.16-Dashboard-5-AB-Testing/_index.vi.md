---
title: "5.16. Dashboard 5: A/B Testing"
linkTitle: "5.16. Dashboard 5: A/B Testing"
menuTitle: "5.16. Dashboard 5: A/B Testing"
date: 2026-05-29
weight: 660
chapter: false
---

Dashboard **A/B Testing** dùng để so sánh hiệu quả giữa các nhóm thử nghiệm, ví dụ nhóm A và nhóm B.

**Dashboard này giúp trả lời:**

- Experiment group nào có conversion rate cao hơn?

- Nhóm nào có add to cart rate tốt hơn?

- Nhóm nào có bounce rate thấp hơn?

- Nhóm nào có session duration cao hơn?

- Sự khác biệt giữa các nhóm có ổn định theo thời gian không?

View sử dụng: **vw_ab_testing_summary**

### I. TẠO FILTER THEO THỜI GIAN

Tạo các **calculated fields** từ **event_date**:

- **event_year** = `extract('YYYY', {event_date})`

- **event_quarter** = `floor((extract('MM', {event_date}) - 1) / 3) + 1`

- **event_month** = `extract('MM', {event_date})`

Sau đó tạo **filter controls** cho Year, Quarter và Month.

### II. TẠO KPI CARDS

#### KPI 1: TOTAL EVENTS
Vẽ KPI Card Total Events theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **KPI**
- Value: **total_events(Sum)**
- Title: **TOTAL EVENTS**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-001.png)

**Insight**:

Cho biết tổng số event được ghi nhận trong A/B testing. Chỉ số này giúp đánh giá quy mô dữ liệu và mức độ đủ lớn của mẫu trước khi so sánh hiệu quả giữa các experiment group..

#### KPI 2: TOTAL VIEWS
Vẽ KPI Card Total Views theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **KPI**
- Value: **views(Sum)**
- Title: **TOTAL VIEWS**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-002.png)

**Insight**:
Biết tổng sample size đầu vào của A/B test. Nếu views quá thấp thì chưa nên kết luận nhóm nào thắng.

#### KPI 3: TOTAL PURCHASES
Vẽ KPI Card Total Purchases theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **KPI**
- Value: **purchases(Sum)**
- Title: **TOTAL PURCHASES**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-003.png)

**Insight**:
Biết tổng số lượt mua hàng trong A/B test. Đây là business outcome quan trọng nhất.

#### KPI 4: CONVERSION RATE
Vẽ KPI Card Conversion Rate theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **KPI**
- Value: **conversion_rate(Average)**
- Format: **Percentage**
- Title: **CONVERSION RATE**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-004.png)

**Insight**:
Biết tỷ lệ chuyển đổi trung bình. Đây là chỉ số chính để đánh giá group nào tốt hơn.

#### KPI 5: ADD TO CART RATE
Vẽ KPI Card Add to Cart Rate theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **KPI**
- Value: **add_to_cart_rate(Average)**
- Format: **Percentage**
- Title: **ADD TO CART RATE**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-005.png)

**Insight**:
Biết nhóm nào làm người dùng có ý định mua cao hơn.

#### KPI 6: BOUNCE RATE
Vẽ KPI Card Bounce Rate theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **KPI**
- Value: **bounce_rate(Average)**
- Format: **Percentage**
- Title: **BOUNCE RATE**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-006.png)

**Insight**:
Biết nhóm nào giữ chân người dùng tốt hơn. Nhóm tốt thường có bounce rate thấp.

#### I. TẠO EXPERIMENT FUNNEL VOLUME BY GROUP BAR CHART
Vẽ Experiment Funnel Volume by Group theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **Bar chart**
- X-axis: **experiment_group**
- Value:
  + **views(Sum)**
  + **clicks(Sum)**
  + **add_to_carts(Sum)**
  + **purchases(Sum)**
- Title: **EXPERIMENT FUNNEL VOLUME BY GROUP**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-007.png)

**Insight**:
Biết từng group có volume ở mỗi bước funnel như thế nào. Nếu group B có views tương đương group A nhưng purchases cao hơn, group B có khả năng hiệu quả hơn

#### II. TẠO EXPERIMENT RATE COMPARISON BAR CHART
Vẽ Experiment Rate Comparison theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **Bar chart**
- X-axis: **experiment_group**
- Value:
  + **conversion_rate(Average)**
  + **add_to_cart_rate(Average)**
  + **bounce_rate(Average)**
- Format: **Percentage**
- Title: **EXPERIMENT RATE COMPARISON**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-008.png)

**Insight**:
Đây là chart quan trọng nhất của dashboard. Nhìn chart này biết group nào có:
- conversion_rate cao
- add_to_cart_rate cao
- bounce_rate thấp

Nếu một group có conversion cao nhưng bounce cũng cao, cần xem lại vì có thể group đó tạo kết quả không ổn định.

#### III. TẠO CONVERSION RATE TREND BY EXPERIMENT GROUP LINE CHART
Vẽ Conversion Rate Trend by Experiment Group theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **Line chart**
- X-axis: **event_date**
- Value: **conversion_rate(Average)**
- Color/Group: **experiment_group**
- Format: **Percentage**
- Title: **CONVERSION RATE TREND BY EXPERIMENT GROUP**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-009.png)

**Insight**:
Biết kết quả A/B test có ổn định theo thời gian không. Nếu một group cao hơn liên tục nhiều ngày, kết quả đáng tin hơn so với chỉ cao trong một ngày.

#### IV. TẠO PURCHASE AND CONVERSION TREND BY EXPERIMENT GROUP BAR CHART
Vẽ Purchase and Conversion Trend by Experiment Group theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **Bar chart**
- X-axis: **event_date**
- Value: **purchases(Sum)**
- Group/Color: **experiment_group**
- Title: **PURCHASE AND CONVERSION TREND BY EXPERIMENT GROUP**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-010.png)

**Insight**:
Chart này cho biết số lượng purchases của từng experiment group thay đổi theo thời gian. Nhìn vào chart có thể xác định nhóm nào tạo ra nhiều lượt mua hàng hơn và kết quả đó có ổn định qua nhiều ngày hay chỉ tăng đột biến trong một thời điểm ngắn. Nếu một experiment group có purchases cao hơn liên tục, nhóm đó có khả năng mang lại hiệu quả kinh doanh tốt hơn. Ngược lại, nếu purchases dao động mạnh hoặc chỉ tăng trong một vài ngày, cần kiểm tra thêm conversion rate, traffic volume và sample size trước khi kết luận nhóm đó là tốt nhất.

#### V. TẠO A/B TESTING PERFORMANCE DETAIL PIVOT TABLE
Vẽ A/B Testing Performance Detail theo cấu hình sau:
- View: **vw_ab_testing_summary**
- Visual type: **Pivot table**
- Rows: **event_date**
- Columns: **experiment_group**
- Values:
  + **views(Sum)**
  + **clicks(Sum)**
  + **add_to_carts(Sum)**
  + **purchases(Sum)**
  + **conversion_rate(Average)**
  + **add_to_cart_rate(Average)**
  + **bounce_rate(Average)**
- Format:
  + **conversion_rate: Percentage**
  + **add_to_cart_rate: Percentage**
  + **bounce_rate: Percentage**
- Title: **A/B TESTING PERFORMANCE DETAIL**

![](/images/5-Workshop/5.16-Dashboard-5-AB-Testing/image-011.png)

**Insight**:
Dùng để kiểm tra chi tiết theo ngày và từng experiment group. Khi chart phía trên có điểm bất thường, table giúp xác định ngày nào/group nào gây ra thay đổi.

#### VIII. Dashboard hoàn chỉnh filter theo năm 2023

<iframe 
  src="/files/Dashboard_4.pdf" 
  width="100%" 
  height="700px"
  style="border: 1px solid #ccc;">
</iframe>

Hoặc tải file tại đây: [Download PDF](/files/Dashboard_4.pdf)
