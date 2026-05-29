---
title: "5.13. Dashboard 2: Funnel Analytics"
linkTitle: "5.13. Dashboard 2: Funnel Analytics"
menuTitle: "5.13. Dashboard 2: Funnel Analytics"
date: 2026-05-29
weight: 630
chapter: false
---

**Dashboard Funnel Analytics** dùng để theo dõi hành trình mua hàng của khách hàng từ lúc xem sản phẩm đến khi mua hàng thành công.

**Dashboard này giúp trả lời các câu hỏi:**

- Người dùng rơi rụng nhiều nhất ở bước nào trong funnel?

- Lượt view, click, add to cart và purchase thay đổi như thế nào theo thời gian?

- Conversion rate có giảm ở giai đoạn nào không?

- Source/device nào có conversion tốt nhất?

- Source/device nào có bounce rate cao?

**Các view sử dụng:**

- vw_daily_event_funnel

- vw_funnel_summary

- vw_daily_funnel_by_source_device

### I. TẠO FILTER THỜI GIAN THEO THỜI GIAN

Vì Dashboard sử dụng các view có cột event_date, cần tạo các calculated fields để lọc theo năm, quý và tháng. Trong từng dataset dùng cho dashboard, tạo các calculated fields sau.
- **event_year**: `extract('YYYY', {event_date})`

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-001.png)

- **event_quarter**: `floor((extract('MM', {event_date}) - 1) / 3) + 1`
- **event_month**: `extract('MM', {event_date})`

Đối với **event_quarter** và **event_month** bật **Show relevant values only** để filter hoạt động theo dạng phân cấp Year → Quarter → Month.
Sau đó tạo filter controls cho:
- event_year
- event_quarter
- event_month

Các bước trên thực hiện như **Tạo calculated fields cho filter thời gian** và **Tạo filter controls**.

### II. KPI CARDS

#### 1. KPI 1: TOTAL EVENTS

- View: **vw_daily_event_funnel**
- Visual type: **KPI**
- Value: **total_events(Sum)**
- Title: **TOTAL EVENTS**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-002.png)

**Insight:** biết tổng lượng event trên toàn funnel.

#### 2. KPI 2: TOTAL VIEWS
- View: **vw_daily_event_funnel**
- Visual type: **KPI**
- Value: **views(Sum)**
- Title: **TOTAL VIEWS**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-003.png)

**Insight:** biết tổng lượng người xem/số lượt xem sản phẩm.

#### 3.  KPI 3: TOTAL CLICKS

- View: **vw_daily_event_funnel**
- Visual type: **KPI**
- Value: **clicks(Sum)**
- Title: **TOTAL CLICKS**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-004.png)

**Insight**: biết mức độ tương tác sau khi người dùng xem.

#### 4. KPI 4: TOTAL ADD TO CARTS

- View: **vw_daily_event_funnel**
- Visual type: **KPI**
- Value: **add_to_carts(Sum)**
- Title: **TOTAL ADD TO CARTS**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-005.png)

**Insight:** biết số lượt thêm vào giỏ hàng.

#### 5. KPI 5: TOTAL PURCHASES

- View: **vw_daily_event_funnel**
- Visual type: **KPI**
- Value: **purchases(Sum)**
- Title: **TOTAL PURCHASES**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-006.png)

**Insight:** biết tổng số lượt mua hàng thành công theo event funnel.

#### 6. KPI 6: BOUNCE RATE

- View: **vw_daily_event_funnel**
- Visual type: **KPI**
- Value: **bounce_rate(Average)**
- Format: **Percentage**
- Title: **BOUNCE RATE**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-007.png)

**Insight**: biết chất lượng traffic tổng quan. Bounce rate càng cao thì càng cần xem lại nguồn traffic hoặc landing page.

#### I. TẠO CONVERSION FUNNEL CHART
Vẽ Conversion Funnel theo cấu hình sau:

Visual này dùng để hiển thị tổng quan số lượng event ở từng bước funnel.

Cấu hình:

- View: **vw_funnel_summary**

- Visual type: **Funnel chart**

- Category: **funnel_stage**

- Value: **funnel_count(Sum)**

- Sort: funnel_stage **Descending**

- Title: **CONVERSION FUNNEL**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-008.png)

**Insight**: Chart này cho biết khách hàng rơi rụng ở bước nào trong hành trình: **Views → Clicks → Add to Cart → Purchases**.

Nếu lượng Views cao nhưng Clicks thấp, có thể nội dung hiển thị, banner hoặc sản phẩm chưa đủ hấp dẫn. Nếu Add to Cart cao nhưng Purchases thấp, vấn đề có thể nằm ở checkout, phí vận chuyển hoặc phương thức thanh toán.

#### II. TẠO DAILY FUNNEL VOLUME TREND LINE CHART
Vẽ Daily Funnel Volume Trend theo cấu hình sau:

Visual này dùng để theo dõi volume của từng bước funnel theo ngày.

Cấu hình:

- View: **vw_daily_event_funnel**

- Visual type: **Line chart**

- X-axis: **event_date**

- Value:

  + **views(Sum)**

  + **clicks(Sum)**

  + **add_to_carts(Sum)**

  + **purchases(Sum)**

- Title: **DAILY FUNNEL VOLUME TREND**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-009.png)

Chart này cho biết số lượng event ở từng bước funnel thay đổi như thế nào theo thời gian. Có thể dùng chart này để phát hiện ngày traffic tăng/giảm, ngày purchases tăng bất thường hoặc các bước funnel có tăng giảm cùng nhau hay không.

#### III. TẠO FUNNEL CONVERSION RATE TREND LINE CHART
Vẽ Funnel Conversion Rate Trend theo cấu hình sau:

Visual này dùng để theo dõi tỷ lệ chuyển đổi giữa các bước funnel

Cấu hình:

- View: **vw_daily_event_funnel**

- Visual type: **Line chart**

- X-axis: **event_date**

- Value:

- **view_to_click_rate(Average)**

- **click_to_cart_rate(Average)**

- **cart_to_purchase_rate(Average)**

- **view_to_purchase_rate(Average)**

- Format: **Percentage**

- Title: **FUNNEL CONVERSION RATE TREND**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-010.png)

**Insight:** Chart này giúp xác định bước nào trong funnel có tỷ lệ chuyển đổi thấp hoặc giảm mạnh theo thời gian.

**Ý nghĩa từng chỉ số:**

- **View to Click Rate**: Cho biết người dùng sau khi xem có click hay không. Nếu thấp, nội dung hoặc sản phẩm có thể chưa đủ hấp dẫn.

- **Click to Cart Rate**: Cho biết người dùng sau khi click có thêm sản phẩm vào giỏ hàng hay không. Nếu thấp, có thể trang sản phẩm, giá bán, mô tả hoặc CTA chưa thuyết phục.

- **Cart to Purchase Rate**: Cho biết người dùng đã thêm vào giỏ có hoàn tất mua hàng hay không. Nếu thấp, vấn đề có thể nằm ở checkout, phí ship hoặc phương thức thanh toán.

- **View to Purchase Rate**: Là tỷ lệ chuyển đổi tổng thể từ view sang purchase. Đây là chỉ số quan trọng để đánh giá hiệu quả toàn bộ funnel.

#### IV. TẠO PURCHASES BY SOURCE AND DEVICE STACKED BAR CHART
Vẽ Purchases by Source and Device theo cấu hình sau:

Visual này dùng để xem purchases đến từ nguồn traffic và thiết bị nào.

Cấu hình:

- View: **vw_daily_funnel_by_source_device**

- Visual type: **Stacked bar chart**

- X-axis: **traffic_source**

- Value: **purchases(Sum)**

- Group/Color: **device_type**

- Sort: purchases **Descending**

- Title: **PURCHASES BY SOURCE AND DEVICE**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-011.png)

**Insight**:
Chart này cho biết purchases đến từ nguồn traffic nào và thiết bị nào. Nhìn vào chart có thể biết kênh nào tạo nhiều đơn hàng nhất, và đơn hàng chủ yếu đến từ mobile, desktop hay tablet

#### V. TẠO CONVERSION RATE BY SOURCE AND DEVICE HEAT MAP
Vẽ Conversion Rate by Source and Device theo cấu hình sau:

Visual này dùng để so sánh conversion rate theo nguồn traffic và thiết bị.

Cấu hình:

- View: **vw_daily_funnel_by_source_device**

- Visual type: **Heat map**

- Rows: **traffic_source**

- Columns: **device_type**

- Value: **conversion_rate(Average)**

- Format: **Percentage**

- Title: **CONVERSION RATE BY SOURCE AND DEVICE**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-012.png)

**Insight**:
Chart này cho biết tổ hợp source/device nào chuyển đổi tốt nhất, ví dụ:
- Email + Desktop
- Social + Mobile
- Organic + Tablet

Nếu một tổ hợp có conversion rate cao, có thể ưu tiên tối ưu marketing hoặc ngân sách cho tổ hợp đó.

#### VI. TẠO BOUNCE RATE BY SOURCE AND DEVICE HEAT MAP
Vẽ Bounce Rate by Source and Device theo cấu hình sau:

Visual này dùng để phát hiện traffic kém chất lượng theo source và device.

Cấu hình:

- View: **vw_daily_funnel_by_source_device**

- Visual type: **Heat map**

- Rows: **traffic_source**

- Columns: **device_type**

- Value: **bounce_rate(Average)**

- Format: **Percentage**

- Title: **BOUNCE RATE BY SOURCE AND DEVICE**

![](/images/5-Workshop/5.13-Dashboard-2-Funnel-Analytics/image-013.png)

Chart này giúp phát hiện source/device nào có bounce rate cao. Ví dụ nếu Social + Mobile có bounce rate cao, có thể traffic từ social không đúng target hoặc landing page trên mobile tải chậm, khiến người dùng thoát nhanh.

### IX. DASHBOARD FUNNEL ANALYTICS SAU KHI FILTER THEO THÁNG 4/2023

<iframe 
  src="/files/Dashboard_2.pdf" 
  width="100%" 
  height="700px"
  style="border: 1px solid #ccc;">
</iframe>

Hoặc tải file tại đây: [Download PDF](/files/Dashboard_2.pdf)
