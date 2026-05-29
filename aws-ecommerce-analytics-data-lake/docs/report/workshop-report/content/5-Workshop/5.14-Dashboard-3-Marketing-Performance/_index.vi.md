---
title: "5.14. Dashboard 3: Marketing Performance"
linkTitle: "5.14. Dashboard 3: Marketing Performance"
menuTitle: "5.14. Dashboard 3: Marketing Performance"
date: 2026-05-29
weight: 640
chapter: false
---

Dashboard **Marketing Performance** dùng để đánh giá hiệu quả của các nguồn traffic và campaign marketing.

**Dashboard này giúp trả lời:**

- Traffic source nào tạo nhiều view, click, add to cart và purchase nhất?

- Nguồn traffic nào có conversion rate tốt nhất?

- Nguồn traffic nào có bounce rate cao?

- Campaign nào tạo nhiều purchases nhất?

- Campaign nào có conversion tốt nhưng bounce thấp?

**Các view sử dụng:**

- vw_traffic_source_performance

- vw_campaign_performance

### I. TẠO FILTER THỜI GIAN THEO THỜI GIAN

Vì các view dùng cột **event_date**, tạo các calculated fields:

- event_year
- event_quarter
- event_month

Công thức tương tự Dashboard 2:

- **event_year** = `extract('YYYY', {event_date})`
- **event_quarter** = `floor((extract('MM', {event_date}) - 1) / 3) + 1`
- **event_month** = `extract('MM', {event_date})`

Sau đó tạo filter controls cho dashboard.

### II. VẼ KPI CARDS

#### KPI 1: TOTAL EVENTS

Vẽ KPI Card Total Events theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **KPI**
- Value: **total_events(Sum)**
- Title: **TOTAL EVENTS**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-001.png)

**Insight**:
Cho biết tổng số event marketing tạo ra. Dùng để đánh giá tổng traffic/interaction đến từ các kênh marketing.

#### KPI 2: TOTAL VIEWS

Vẽ KPI Card Total Views theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **KPI**
- Value: **views(Sum)**
- Title: **TOTAL VIEWS**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-002.png)

**Insight**:
Cho biết tổng lượt xem đến từ các nguồn marketing. Nếu views cao nhưng conversion thấp thì traffic nhiều nhưng chất lượng chưa tốt.

#### KPI 3: TOTAL CLICKS

Vẽ KPI Card Total Clicks theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **KPI**
- Value: **clicks(Sum)**
- Title: **TOTAL CLICKS**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-003.png)

**Insigh**t:
Cho biết mức độ người dùng tương tác sau khi nhìn thấy sản phẩm/nội dung marketing.

#### KPI 4: TOTAL ADD TO CARTS

Vẽ KPI Card Total Add to Carts theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **KPI**
- Value: **add_to_carts(Sum)**
- Title: **TOTAL ADD TO CARTS**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-004.png)

**Insight**:
Cho biết marketing có kéo được người dùng đến bước có ý định mua hay không.

#### KPI 5: TOTAL PURCHASES

Vẽ KPI Card Total Purchases theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **KPI**
- Value: **purchases(Sum)**
- Title: **TOTAL PURCHASES**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-005.png)

**Insight**:
Cho biết tổng số lượt mua hàng đến từ hoạt động marketing.

#### KPI 6: BOUNCE RATE

Vẽ KPI Card Bounce Rate theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **KPI**
- Value: **bounce_rate(Average)**
- Format: **Percentage**
- Title: **BOUNCE RATE**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-006.png)

**Insight**:
Cho biết chất lượng traffic tổng quan. Bounce rate cao nghĩa là người dùng vào nhưng thoát nhanh, có thể do traffic không đúng target hoặc landing page chưa tốt.

#### I. TẠO MARKETING FUNNEL VOLUME BY TRAFFIC SOURCE VERTICAL BAR CHART

Visual này dùng để so sánh volume funnel theo từng nguồn traffic.

Vẽ Marketing Funnel Volume by Traffic Source theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **Vertical bar chart**
- X-axis: **traffic_source**
- Value:
  + **views(Sum)**
  + **clicks(Sum)**
  + **add_to_carts(Sum)**
  + **purchases(Sum)**
- Sort: **purchases Descending**
- Title: **MARKETING FUNNEL VOLUME BY TRAFFIC SOURCE**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-007.png)

**Insight**:
Chart này cho biết mỗi traffic source tạo ra bao nhiêu views, clicks, add to carts và purchases. Có thể dùng để phát hiện kênh nào kéo traffic nhiều nhưng không tạo purchase tương ứng.

#### II. TẠO TRAFFIC SOURCE QUALITY VERTICAL BAR CHART

Visual này dùng để so sánh chất lượng traffic giữa các nguồn.

Vẽ Traffic Source Quality theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **Vertical Bar chart**
- X-axis: **traffic_source**
- Value:
  + **view_to_purchase_rate(Average)**
  + **bounce_rate(Average)**
- Format: **Percentage**
- Sort: **view_to_purchase_rate Descending**
- Title: **TRAFFIC SOURCE QUALITY**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-008.png)

**Insight**:
Nguồn traffic tốt là nguồn có view_to_purchase_rate cao và bounce_rate thấp. Ví dụ, nếu Email có conversion cao và bounce thấp thì đây là nguồn traffic chất lượng. Nếu Social có nhiều traffic nhưng bounce cao, cần xem lại target audience hoặc nội dung quảng cáo.

#### III. TẠO PURCHASE TREND BY TRAFFIC SOURCE LINE CHART

Vẽ Purchase Trend by Traffic Source theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **Line chart**
- X-axis: **event_date**
- Value: **purchases(Sum)**
- Color/Group: **traffic_source**
- Title: **PURCHASE TREND BY TRAFFIC SOURCE**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-009.png)

**Insight**:
Chart này cho biết số purchase theo từng nguồn traffic thay đổi theo thời gian. Có thể dùng để phát hiện nguồn nào tăng trưởng tốt, nguồn nào giảm hiệu quả hoặc thời điểm nào có spike purchase do campaign/promotion.

#### IV. TẠO CONVERSION RATE TREND BY TRAFFIC SOURCE LINE CHART

Vẽ Conversion Rate Trend by Traffic Source theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **Line chart**
- X-axis: **event_date**
- Value: **view_to_purchase_rate(Average)**
- Color/Group: **traffic_source**
- Format: **Percentage**
- Title: **CONVERSION RATE TREND BY TRAFFIC SOURCE**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-010.png)

**Insight**:
Chart này cho biết hiệu quả chuyển đổi của từng nguồn traffic theo thời gian. Nếu purchases tăng nhưng conversion rate giảm, có thể nguồn đó kéo nhiều traffic hơn nhưng chất lượng traffic thấp hơn.

#### V. TẠO BOUNCE RATE TREND BY TRAFFIC SOURCE LINE CHART

Vẽ Bounce Rate Trend by Traffic Source theo cấu hình sau:

- View: **vw_traffic_source_performance**
- Visual type: **Line chart**
- X-axis: **event_date**
- Value: **bounce_rate(Average)**
- Color/Group: **traffic_source**
- Format: **Percentage**
- Title: **BOUNCE RATE TREND BY TRAFFIC SOURCE**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-011.png)

**Insight**:
Chart này cho biết nguồn traffic nào có bounce rate tăng/giảm theo thời gian. Nếu bounce rate tăng đột ngột ở một source, có thể campaign mới đang kéo sai đối tượng hoặc landing page có vấn đề.

#### VI. TẠO TOP CAMPAIGNS BY PURCHASES HORIZONTAL BAR CHART

Vẽ Top Campaigns by Purchases theo cấu hình sau:

- View: **vw_campaign_performance**
- Visual type: **Horizontal bar chart**
- Y-axis: **campaign_id**
- Value: **purchases(Sum)**
- Sort: **purchases Descending**
- Title: **TOP CAMPAIGNS BY PURCHASES**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-012.png)

**Insight**:
Chart này cho biết campaign nào tạo ra nhiều lượt mua hàng nhất. Đây là chart quan trọng để xác định campaign đóng góp nhiều nhất vào kết quả marketing.

#### VII. TẠO CAMPAIGN CONVERSION VS BOUNCE RATE CLUSTERED BAR COMBO CHART

Vẽ Campaign Conversion vs Bounce Rate theo cấu hình sau:

- View: **vw_campaign_performance**
- Visual type: **Clustered bar combo chart**
- X-axis: **campaign_id**
- Value:
  + **conversion_rate(Average)**
  + **bounce_rate(Average)**
- Format: **Percentage**
- Title: **CAMPAIGN CONVERSION VS BOUNCE RATE**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-013.png)

**Insight**:
Chart này giúp đánh giá chất lượng campaign. Campaign tốt là campaign có conversion rate cao và bounce rate thấp. Nếu một campaign có purchases cao nhưng bounce rate cũng cao, campaign đó có thể kéo được volume nhưng chưa tối ưu chất lượng traffic.

#### VIII. TẠO CAMPAIGN FUNNEL VOLUME VERTICAL STACKED BAR CHART

Vẽ Campaign Funnel Volume theo cấu hình sau:

- View: **vw_campaign_performance**
- Visual type: **Vertical stacked bar chart**
- X-axis: **campaign_id**
- Value:
  + **views(Sum)**
  + **clicks(Sum)**
  + **add_to_carts(Sum)**
  + **purchases(Sum)**
- Sort: **purchases Descending**
- Title: **CAMPAIGN FUNNEL VOLUME**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-014.png)

**Insight**:
Chart này cho biết từng campaign tạo ra volume ở mỗi bước funnel. Có thể dùng để phát hiện campaign nào nhiều views nhưng ít purchases, hoặc campaign nào views không cao nhưng chuyển đổi tốt.

#### IX. TẠO CAMPAIGN CONVERSION RATE TREND LINE CHART

Vẽ Campaign Conversion Rate Trend theo cấu hình sau:

- View: **vw_campaign_performance**
- Visual type: **Line chart**
- X-axis: **event_date**
- Value: **conversion_rate(Average)**
- Color/Group: **campaign_id**
- Format: **Percentage**
- Title: **CAMPAIGN CONVERSION RATE TREND**

![](/images/5-Workshop/5.14-Dashboard-3-Marketing-Performance/image-015.png)

**Insight**:
Chart này cho biết conversion rate của từng campaign thay đổi theo thời gian. Nếu một campaign giảm conversion sau vài ngày chạy, có thể audience bị bão hòa hoặc nội dung quảng cáo mất hiệu quả.

#### XII. Dashboard hoàn chỉnh filter theo Tháng 4/2023

<iframe 
  src="/files/Dashboard_3.pdf" 
  width="100%" 
  height="700px"
  style="border: 1px solid #ccc;">
</iframe>

Hoặc tải file tại đây: [Download PDF](/files/Dashboard_3.pdf)
