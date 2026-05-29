---
title: "5.12. Dashboard 1: Executive Overview"
linkTitle: "5.12. Dashboard 1: Executive Overview"
menuTitle: "5.12. Dashboard 1: Executive Overview"
date: 2026-05-29
weight: 620
chapter: false
---

Mục tiêu của dashboard này là giúp người xem trong khoảng 10 giây có thể nắm được tình hình tổng quan của business.

**Dashboard cần trả lời các câu hỏi chính:**

- Revenue đang tăng hay giảm?

- Số lượng orders có tăng không?

- Average Order Value là bao nhiêu?

- Refund rate có bất thường không?

- Có ngày/tháng nào doanh thu giảm mạnh không?

Dataset sử dụng: **vw_executive_overview**

### I. TẠO CALCULATED FIELDS CHO FILTER THỜI GIAN

Để tạo bộ lọc theo năm, quý và tháng, cần tạo các **calculated fields** từ cột **transaction_date**.

Trong QuickSight, chọn **Add calculated field**.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-001.png)

#### 1. Tạo transaction_year

- Tên calculated field: **transaction_year**

- Công thức: `extract('YYYY', {transaction_date})`

Sau đó nhấn **Save**.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-002.png)

#### 2. Tạo transaction_month

- Tên calculated field: **transaction_month**

- Công thức: `extract('MM', {transaction_date})`

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-003.png)

#### 3. Tạo transaction_quarter

- Tên calculated field: **transaction_quarter**

- Công thức: `floor((extract('MM', {transaction_date}) - 1) / 3) + 1`

Công thức này dùng để xác định quý từ tháng:

- Tháng 1, 2, 3 → Quý 1

- Tháng 4, 5, 6 → Quý 2

- Tháng 7, 8, 9 → Quý 3

- Tháng 10, 11, 12 → Quý 4

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-004.png)

### II. TẠO FILTER CONTROLS

Sau khi tạo các calculated fields, tiến hành tạo filter cho dashboard.

Trong giao diện Analysis của QuickSight:

- Nhấn biểu tượng **Filter**

- Chọn **Add**

- Chọn field cần lọc:

  - transaction_year

  - transaction_quarter

  - transaction_month

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-005.png)

Sau đó nhấn dấu ba chấm ở từng filter, chọn **Add control**. Sau đó chọn vị trí hiển thị là **Top of this sheet**.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-006.png)

Nhập tên hiển thị cho thuộc tính cần lọc, chọn kiểu filter **Dropdown** và nhấn **Add**.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-007.png)

Đối với filter theo **transaction_quarter** và **transaction_month**, bật tùy chọn **Show relevant values only** vì tùy chọn này giúp filter hoạt động theo dạng hierarchy. Ví dụ, khi chọn một năm cụ thể, filter quarter và month chỉ hiển thị các giá trị phù hợp với năm đó.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-008.png)

Chọn **Quarter** để hierarchy theo Year -> Quarter. Nhấn **Update**.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-009.png)

Các giá trị liên quan đến hierarchy đã được thêm thành công, nhấn **Add** để thêm filter.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-010.png)

Filter đã được thêm thành công.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-011.png)

### Cấu hình phạm vi áp dụng filter

Sau khi tạo filter controls, cần cấu hình phạm vi áp dụng filter cho các visual.

Trong QuickSight, mỗi filter có thể áp dụng theo một trong ba phạm vi:

| Phạm vi | Ý nghĩa |
| --- | --- |
| Only this visual | Filter chỉ áp dụng cho visual đang chọn |
| This sheet | Filter áp dụng cho tất cả visual trong sheet hiện tại |
| Cross-sheet | Filter áp dụng cho nhiều sheet có cùng dataset |

Click vào từng filter để chọn biểu tượng **This sheet** để apply cho toàn bộ visual trong cùng sheet. Vì dùng filter dạng hierarchy nên không thể sử dụng Cross-sheet.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-012.png)

Kiểm tra các filter sau khi tạo:

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-013.png)

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-014.png)

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-015.png)

### III. Tạo KPI Cards

Dashboard Executive Overview có **4 KPI Cards** chính:

- TOTAL REVENUE

- TOTAL ORDERS

- AVG ORDER VALUE

- REFUND RATE

#### Tạo KPI Card

Tạo visual mới và chọn Visual type: **KPI**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-016.png)

Cấu hình:

- Value: **total_revenue(Sum)**

- Show as: **Currency**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-017.png)

#### Tùy chỉnh KPI Cards

Để tùy chỉnh giao diện KPI Card:

- Chọn KPI Card cần chỉnh sửa

- Mở panel **Properties** ở bên phải

- Chọn phần **KPI options**

- Tùy chỉnh các thông tin như: Font size, Title, Value format, Trend display, Màu sắc, Layout,…

Để đổi tên visual, có thể **nháy đúp vào tiêu đề** của Card và nhập tên mới. Nhấn **Save** để lưu.

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-018.png)

Thực hiện tương tự tạo các KPI Cards sau:

#### KPI 1: TOTAL REVENUE

Vẽ KPI Card Total Revenue theo cấu hình sau:

- Visual type: **KPI**

- Value: **sum(total_revenue)**

- Trend group: **transaction_date**

- Format: **Currency**

- Title: **TOTAL REVENUE**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-019.png)

#### KPI 2: TOTAL ORDERS

Vẽ KPI Card Total Orders theo cấu hình sau:

- Value: **sum(total_orders)**

- Trend group: **transaction_date**

- Format: **Number**

- Title: **TOTAL ORDERS**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-020.png)

#### KPI 3: AVG ORDER VALUE

Vẽ KPI Card Avg Order Value theo cấu hình sau:

- Value: **avg(avg_order_value)**

- Trend group: **transaction_date**

- Format: **Currency**

- Title: **AVG ORDER VALUE**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-021.png)

#### KPI 4: REFUND RATE

Vẽ KPI Card Refund Rate theo cấu hình sau:

- Value: **avg(refund_rate)**

- Trend group: **transaction_date**

- Format: **Percent**

- Title: **REFUND RATE**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-022.png)

#### I. TẠO REVENUE TREND LINE CHART

Visual này dùng để theo dõi xu hướng doanh thu theo thời gian.

Nhấn **Add** để tạo visual mới và chọn: **Line chart**.

Cấu hình:

Vẽ Revenue Trend theo cấu hình sau:

- X-axis: **transaction_date**

- Value: **total_revenue(Sum)**

- Title: **REVENUE TREND**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-023.png)

**Chart này giúp trả lời:**

- Revenue đang tăng hay giảm?

- Có tính mùa vụ theo tháng/quý không?

- Quarter nào có doanh thu mạnh nhất?

- Có ngày hoặc tháng nào doanh thu giảm bất thường không?

#### II. TẠO ORDERS TREND BAR CHART

Visual này dùng để theo dõi số lượng đơn hàng theo thời gian.

Vẽ Orders Trend theo cấu hình sau:

- Visual type: **Bar chart**

- X-axis: **transaction_date**

- Value: **total_orders(Sum)**

- Title: **ORDERS TREND**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-024.png)

**Chart này giúp trả lời:**

- Order volume có tăng không?

- Số đơn hàng có đi cùng xu hướng với revenue không?

- Giai đoạn nào có lượng đơn hàng tăng hoặc giảm rõ rệt?

#### III. TẠO ORDERS TREND CLUSTERED BAR COMBO CHART

Combo chart giúp so sánh đồng thời số lượng đơn hàng và doanh thu theo thời gian.

Vẽ Orders Trend theo cấu hình sau:

- Visual type: **Clustered bar combo chart**

- X-axis: **transaction_date**

- Value: **total_orders(Sum)**

- Title: **ORDERS TREND**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-025.png)

**Chart này giúp kiểm tra:**

- Revenue tăng là do số đơn hàng tăng hay do giá trị đơn hàng tăng?

- Có giai đoạn orders tăng nhưng revenue không tăng tương ứng không?

- Business tăng trưởng theo volume hay theo giá trị đơn hàng?

#### IV. TẠO REFUND RATE TREND LINE CHART

Visual này dùng để theo dõi tỷ lệ refund theo thời gian.

Vẽ Refund Rate Trend theo cấu hình sau:

- Visual type: **Line chart**

- X-axis: **transaction_date**

- Value: **refund_rate(Average)**

- Title: **REFUND RATE TREND**

![](/images/5-Workshop/5.12-Dashboard-1-Executive-Overview/image-026.png)

Chart này cho biết tỷ lệ refund thay đổi theo thời gian.

Nếu refund rate tăng sau một giai đoạn cụ thể, nguyên nhân có thể liên quan đến:

- Chất lượng sản phẩm

- Sai kỳ vọng của khách hàng

- Lỗi vận chuyển

- Chiến dịch bán hàng không đúng target

- Một category hoặc brand cụ thể có vấn đề

Dashboard này giúp người xem nhanh chóng đánh giá tình hình tổng quan của ecommerce business, bao gồm doanh thu, số đơn hàng, giá trị đơn hàng trung bình và tỷ lệ refund.

#### VIII. Dashboard hoàn chỉnh filter theo Tháng 4/2023

<iframe 
  src="/files/Dashboard_1.pdf" 
  width="100%" 
  height="700px"
  style="border: 1px solid #ccc;">
</iframe>

Hoặc tải file tại đây: [Download PDF](/files/Dashboard_1.pdf)
