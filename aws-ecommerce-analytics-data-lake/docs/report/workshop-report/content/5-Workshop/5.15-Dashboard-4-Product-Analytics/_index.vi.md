---
title: "5.15. Dashboard 4: Product Analytics"
linkTitle: "5.15. Dashboard 4: Product Analytics"
menuTitle: "5.15. Dashboard 4: Product Analytics"
date: 2026-05-29
weight: 650
chapter: false
---

Dashboard **Product Analytics** dùng để đánh giá hiệu quả bán hàng theo sản phẩm, category, brand và nhóm premium/non-premium.

**Dashboard này giúp trả lời:**

- Sản phẩm nào tạo nhiều revenue nhất?

- Category nào bán tốt nhất?

- Brand nào có hiệu quả cao nhất?

- Premium product có tạo doanh thu tốt không?

- Product/category nào có refund rate cao?

View sử dụng **vw_product_revenue**.

### I. TẠO FILTER THEO THỜI GIAN

Tạo các calculated fields:
- **transaction_year** = `extract('YYYY', {transaction_date})`
- **transaction_quarter** = `floor((extract('MM', {transaction_date}) - 1) / 3) + 1`
- **transaction_month** = `extract('MM', {transaction_date})`

Sau đó tạo filter controls tương tự Dashboard 1.

### II. TẠO KPI CARDS:

#### KPI 1: TOTAL REVENUE

Vẽ KPI Card Total Revenue theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **KPI**
- Value: **total_revenue(Sum)**
- Format: **Currency**
- Title: **TOTAL REVENUE**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-001.png)

**Insight**:
Cho biết tổng doanh thu tạo ra từ sản phẩm. Đây là chỉ số tổng quan quan trọng nhất của Product Analytics.

#### KPI 2: TOTAL TRANSACTIONS

Vẽ KPI Card Total Transactions theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **KPI**
- Value: **total_transactions(Sum)**
- Title: **TOTAL TRANSACTIONS**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-002.png)

**Insight**:
Cho biết tổng số giao dịch phát sinh theo sản phẩm. Nếu revenue cao nhưng transactions thấp, có thể sản phẩm bán ít nhưng giá trị đơn cao.

#### KPI 3: TOTAL UNITS SOLD

Vẽ KPI Card Total Units Sold theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **KPI**
- Value: **total_units_sold(Sum)**
- Title: **TOTAL UNITS SOLD**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-003.png)

**Insight**:
Cho biết tổng số lượng sản phẩm đã bán. Dùng để đánh giá sản phẩm/category/brand nào có volume bán tốt.

#### KPI 4: AVERAGE TRANSACTION VALUE

Vẽ KPI Card Average Transaction Value theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **KPI**
- Value: **avg_transaction_value(Average)**
- Format: **Currency**
- Title: **AVERAGE TRANSACTION VALUE**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-004.png)

**Insight**:
Cho biết giá trị giao dịch trung bình. Nếu chỉ số này cao, sản phẩm hoặc nhóm sản phẩm đang tạo đơn hàng có giá trị tốt.

#### KPI 5: REFUNDED TRANSACTIONS

Vẽ KPI Card Refunded Transactions theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **KPI**
- Value: **refunded_transactions(Sum)**
- Title: **REFUNDED TRANSACTIONS**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-005.png)

**Insight**:
Cho biết tổng số giao dịch bị refund. Dùng để phát hiện vấn đề về chất lượng sản phẩm hoặc kỳ vọng khách hàng.

#### KPI 6: REFUND RATE

Vẽ KPI Card Refund Rate theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **KPI**
- Value: **refund_rate(Average)**
- Format: **Percentage**
- Title: **REFUND RATE**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-006.png)

**Insight**:
Cho biết tỷ lệ refund trung bình của sản phẩm. Nếu refund rate cao, cần kiểm tra category/brand/product nào đang gây ra hoàn hàng nhiều.

#### I. TẠO PRODUCT REVENUE TREND LINE CHART

Vẽ Product Revenue Trend theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Line chart**
- X-axis: **transaction_date**
- Value: **total_revenue(Sum)**
- Title: **PRODUCT REVENUE TREND**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-007.png)

**Insight**:
Chart này cho biết doanh thu sản phẩm thay đổi theo thời gian. Nhìn chart sẽ biết ngày/tháng nào doanh thu tăng, giảm hoặc có spike bất thường.

#### II. TẠO PRODUCT SALES TREND LINE CHART

Vẽ Product Sales Trend theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Line chart**
- X-axis: **transaction_date**
- Value: **total_units_sold(Sum)**
- Title: **PRODUCT SALES TREND**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-008.png)

**Insight**:
Chart này cho biết số lượng sản phẩm bán ra thay đổi theo thời gian. Nếu units sold tăng nhưng revenue không tăng tương ứng, có thể sản phẩm bán nhiều là nhóm giá thấp.

#### III. TẠO PRODUCT PERFORMANCE BY CATEGORY COMBO CHART

Vẽ Product Performance by Category theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Combo chart**
- X-axis: **category**
- Bar value: **total_revenue(Sum)**
- Line value: **total_units_sold(Sum)**
- Sort: **total_revenue Descending**
- Title: **PRODUCT PERFORMANCE BY CATEGORY**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-009.png)

**Insight**:
Chart này cho biết category nào tạo doanh thu cao và category nào bán được nhiều unit. Nếu category có units sold cao nhưng revenue thấp, đó có thể là nhóm sản phẩm giá thấp. Nếu revenue cao nhưng units sold thấp, đó có thể là nhóm sản phẩm giá trị cao.

#### IV. TẠO PRODUCT PERFORMANCE BY BRAND COMBO CHART

Vẽ Product Performance by Brand theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Combo chart**
- X-axis: **brand**
- Bar value: **total_revenue(Sum)**
- Line value: **total_units_sold(Sum)**
- Sort: **total_revenue Descending**
- Title: **PRODUCT PERFORMANCE BY BRAND**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-010.png)

**Insight**:
Chart này cho biết brand nào tạo doanh thu tốt và brand nào bán được nhiều sản phẩm. Dùng để xác định brand mạnh về doanh thu, brand mạnh về volume, hoặc brand cần tối ưu thêm.

#### V. TẠO PREMIUM VS NON-PREMIUM REVENUE BAR CHART

Vẽ Premium vs Non-Premium Revenue theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Bar chart**
- X-axis: **is_premium**
- Value: **total_revenue(Sum)**
- Sort: **total_revenue Descending**
- Title: **PREMIUM VS NON-PREMIUM REVENUE**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-011.png)

**Insight**:
Chart này cho biết nhóm sản phẩm premium hay non-premium đóng góp doanh thu nhiều hơn. Nếu premium revenue cao hơn, có thể nhóm sản phẩm cao cấp đang là nguồn doanh thu chính. Nếu non-premium revenue cao hơn, doanh thu chủ yếu đến từ volume lớn của sản phẩm phổ thông.

#### VI. TẠO PREMIUM VS NON-PREMIUM SALES VOLUME GROUPED BAR CHART

Vẽ Premium vs Non-Premium Sales Volume theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Grouped bar chart**
- X-axis: **is_premium**
- Value:
  + **total_transactions(Sum)**
  + **total_units_sold(Sum)**
- Title: **PREMIUM VS NON-PREMIUM SALES VOLUME**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-012.png)

**Insight**:
Chart này cho biết nhóm premium hay non-premium có volume bán tốt hơn. Nếu non-premium có transactions/units cao hơn nhưng revenue không vượt nhiều, nghĩa là nhóm này bán nhiều nhưng giá trị thấp hơn. Nếu premium bán ít hơn nhưng revenue cao, nghĩa là premium có giá trị đơn hàng tốt.

#### VII. TẠO TOP PRODUCTS BY REVENUE HORIZONTAL BAR CHART

Vẽ Top Products by Revenue theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Horizontal bar chart**
- Y-axis: **product_id**
- Value: **total_revenue(Sum)**
- Sort: **total_revenue Descending**
- Title: **TOP PRODUCTS BY REVENUE**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-013.png)

**Insight**:
Chart này cho biết sản phẩm nào tạo doanh thu cao nhất. Đây là nhóm sản phẩm chủ lực cần ưu tiên tồn kho, marketing hoặc upsell.

#### VIII. TẠO AVG TRANSACTION VALUE BY CATEGORY BAR CHART

Vẽ Avg Transaction Value by Category theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Bar chart**
- X-axis: **category**
- Value: **avg_transaction_value(Average)**
- Format: **Currency**
- Sort: **avg_transaction_value Descending**
- Title: **AVG TRANSACTION VALUE BY CATEGORY**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-014.png)

**Insight**:
Chart này cho biết category nào có giá trị giao dịch trung bình cao. Category có average transaction value cao thường phù hợp để upsell, bundle hoặc chạy campaign premium.

#### IX. TẠO TOP REFUNDED PRODUCTS HORIZONTAL BAR CHART

Vẽ Top Refunded Products theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Horizontal bar chart**
- Y-axis: **product_id**
- Value: **refunded_transactions(Sum)**
- Sort: **refunded_transactions Descending**
- Group/Color: **category**
- Title: **TOP REFUNDED PRODUCTS**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-015.png)

**Insight**:
Chart này cho biết sản phẩm nào bị refund nhiều nhất theo category. Dùng để phát hiện sản phẩm có vấn đề về chất lượng, mô tả, giá trị thực tế hoặc vận chuyển.

#### X. TẠO REFUND RATE BY CATEGORY BAR CHART

Vẽ Refund Rate by Category theo cấu hình sau:

- View: **vw_product_revenue**
- Visual type: **Bar chart**
- X-axis: **category**
- Value: **refund_rate(Average)**
- Format: **Percentage**
- Sort: **refund_rate Descending**
- Title: **REFUND RATE BY CATEGORY**

![](/images/5-Workshop/5.15-Dashboard-4-Product-Analytics/image-016.png)

**Insight**:
Chart này cho biết category nào có tỷ lệ refund cao nhất. Nếu một category có refund rate cao, cần kiểm tra chất lượng sản phẩm, mô tả sản phẩm, kỳ vọng khách hàng hoặc vấn đề vận chuyển.


#### XIII. Dashboard hoàn chỉnh filter theo Tháng 4/2023

<iframe 
  src="/files/Dashboard_4.pdf" 
  width="100%" 
  height="700px"
  style="border: 1px solid #ccc;">
</iframe>

Hoặc tải file tại đây: [Download PDF](/files/Dashboard_4.pdf)
