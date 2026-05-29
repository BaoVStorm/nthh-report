---
title: "XÂY DỰNG E-COMMERCE ANALYTICS DATA LAKE TRÊN AWS THEO HƯỚNG SERVERLESS"
linkTitle: "5.1. Giới thiệu"
menuTitle: "5.1. Giới thiệu"
date: 2026-05-29
weight: 510
chapter: false
---

## GIỚI THIỆU

Trong thương mại điện tử, dữ liệu được tạo ra từ nhiều hoạt động khác nhau như người dùng xem sản phẩm, click vào nội dung, thêm sản phẩm vào giỏ hàng, hoàn tất giao dịch mua hàng, hoàn tiền hoặc tham gia các chiến dịch marketing. Nếu dữ liệu này chỉ được lưu trữ ở dạng file thô, doanh nghiệp sẽ rất khó khai thác để trả lời các câu hỏi quan trọng như: doanh thu đang tăng hay giảm, khách hàng rơi rụng ở bước nào trong funnel, nguồn traffic nào hiệu quả nhất, sản phẩm nào bán tốt nhất hoặc nhóm A/B testing nào có tỷ lệ chuyển đổi cao hơn.

Workshop **E-commerce Analytics Data Lake on AWS** được xây dựng nhằm mô phỏng một quy trình Data Engineering hoàn chỉnh trên AWS. Dữ liệu đầu vào là bộ **Marketing & E-commerce Analytics Dataset** từ Kaggle, bao gồm ba nhóm dữ liệu chính:

- **events.csv**: chứa dữ liệu hành vi người dùng như view, click, add to cart, bounce và purchase.
- **products.csv**: chứa thông tin sản phẩm như category, brand, base price, launch date và premium flag.
- **transactions.csv**: chứa dữ liệu giao dịch mua hàng, số lượng sản phẩm, discount, gross revenue và refund flag.

Trong workshop này, các dịch vụ AWS được kết hợp để xây dựng một pipeline phân tích dữ liệu theo hướng serverless.

- **Amazon S3** được sử dụng làm Data Lake chính của workshop. Dữ liệu được tổ chức thành nhiều tầng như *Raw Zone*, *Curated Zone*, *Error Zone* và *Athena Results*. Raw Zone lưu dữ liệu CSV ban đầu, Curated Zone lưu dữ liệu đã được xử lý dưới định dạng Parquet, Error Zone lưu các bản ghi lỗi, còn Athena Results dùng để lưu kết quả truy vấn từ Athena.

- **AWS Glue Data Catalog** được sử dụng để lưu metadata của dữ liệu trong S3. Khi dữ liệu nằm trong S3, Glue Data Catalog giúp các dịch vụ như Athena hiểu được schema, tên cột, kiểu dữ liệu và vị trí lưu trữ của từng bảng.

- **AWS Glue Crawler** được sử dụng để tự động quét dữ liệu trong S3 và tạo bảng metadata trong Glue Data Catalog. Project sử dụng hai crawler chính: một crawler cho Raw Zone và một crawler cho Curated Zone. Raw Crawler giúp Athena query được dữ liệu CSV ban đầu, còn Curated Crawler giúp Athena query được dữ liệu Parquet sau ETL.

- **AWS Glue ETL Job** là thành phần xử lý dữ liệu chính. Glue Job đọc dữ liệu CSV từ S3 Raw Zone, thực hiện parse timestamp, cast kiểu dữ liệu, chuẩn hóa text, xử lý giá trị thiếu, validate transaction lỗi và ghi dữ liệu đã xử lý sang S3 Curated Zone dưới định dạng Parquet. Đối với bảng events và transactions, dữ liệu được partition theo year/month/day để tối ưu hiệu năng truy vấn. Các transaction không hợp lệ được tách riêng vào Error Zone để phục vụ kiểm tra và debug.

- **Amazon Athena** được sử dụng để truy vấn dữ liệu trực tiếp trên Amazon S3 bằng SQL. Trong project này, Athena có hai vai trò chính: kiểm tra dữ liệu raw/curated sau từng bước xử lý và tạo các business views phục vụ dashboard. Các Athena Views đóng vai trò là semantic layer, giúp tổng hợp sẵn logic business như revenue, orders, funnel conversion, marketing performance, product performance và A/B testing.

- **Amazon QuickSight** được sử dụng để trực quan hóa dữ liệu từ Athena. Workshop sử dụng QuickSight Direct Query để kết nối trực tiếp với các Athena Views trong database ecommerce_curated. Các dashboard được xây dựng nhằm hỗ trợ phân tích business, bao gồm Executive Overview, Funnel Analytics, Marketing Performance, Product Analytics và A/B Testing.

- **AWS Glue Workflow** được sử dụng để điều phối thứ tự chạy của pipeline. Workflow giúp gom các bước Raw Crawler, Glue ETL Job và Curated Crawler thành một luồng xử lý có thứ tự. Khi Raw Crawler chạy thành công, Glue ETL Job sẽ được kích hoạt. Sau khi Glue ETL Job hoàn tất, Curated Crawler sẽ chạy để cập nhật metadata cho dữ liệu curated.

- **Amazon EventBridge Scheduler** được sử dụng để tự động kích hoạt Glue Workflow theo lịch. Thay vì chạy thủ công từng bước, EventBridge Scheduler gọi API StartWorkflowRun để start workflow theo cron schedule. Điều này giúp pipeline có thể chạy tự động hằng ngày.

- **Amazon EventBridge Rules** được sử dụng để bắt lỗi trong quá trình vận hành pipeline. Các rule được cấu hình để phát hiện trạng thái lỗi như Raw Crawler Failed, Curated Crawler Failed, Glue ETL Job Failed, Timeout hoặc Stopped.

- **Amazon Simple Notification Service** được sử dụng để gửi email notification khi pipeline gặp lỗi. Khi EventBridge Rule phát hiện lỗi từ Glue Job hoặc Glue Crawler, event sẽ được gửi đến SNS Topic và SNS sẽ gửi email cảnh báo đến người vận hành.

- **Amazon CloudWatch Logs** được sử dụng để kiểm tra log của Glue ETL Job. Khi job chạy lỗi hoặc cần debug, CloudWatch Logs giúp kiểm tra chi tiết quá trình đọc dữ liệu, xử lý dữ liệu, ghi output và các lỗi PySpark nếu có.

Về mặt xử lý dữ liệu, pipeline bắt đầu từ bước local preprocessing, trong đó dữ liệu được kiểm tra sơ bộ và đổi tên một số cột để dễ xử lý hơn. Sau đó, các file CSV được upload lên Amazon S3 Raw Zone. Từ tầng raw, Glue Crawler tạo metadata để Athena có thể query dữ liệu ban đầu. Sau khi dữ liệu raw được validate, Glue ETL Job xử lý dữ liệu và ghi kết quả sang Curated Zone dưới định dạng Parquet. Tiếp theo, Curated Crawler cập nhật metadata cho dữ liệu curated. Cuối cùng, Athena Views được tạo để phục vụ QuickSight dashboards.

Các bảng curated chính trong workshop bao gồm:

- **fact_events**: dữ liệu hành vi người dùng đã được làm sạch.
- **dim_products**: dữ liệu sản phẩm đóng vai trò dimension table.
- **fact_transactions**: dữ liệu giao dịch hợp lệ sau khi validate.

Từ các bảng curated này, ta tạo thêm các Athena Views chính như:

- **vw_executive_overview**: phân tích doanh thu, số đơn hàng, average order value và refund rate.
- **vw_daily_event_funnel**: phân tích funnel theo ngày.
- **vw_funnel_summary**: chuẩn bị dữ liệu cho funnel chart.
- **vw_daily_funnel_by_source_device**: phân tích funnel theo traffic source và device.
- **vw_traffic_source_performance**: đánh giá hiệu quả từng nguồn traffic.
- **vw_campaign_performance**: đánh giá hiệu quả campaign marketing.
- **vw_product_revenue**: phân tích doanh thu theo product, category, brand và premium status.
- **vw_ab_testing_summary**: phân tích hiệu quả giữa các experiment group.
- **vw_discount_refund_analysis**: phân tích mối quan hệ giữa discount và refund.

Sau khi semantic layer đã sẵn sàng, **Amazon QuickSight** được dùng để xây dựng các dashboard phân tích. 
- Dashboard Executive Overview giúp theo dõi tình hình kinh doanh tổng quan. 
- Dashboard Funnel Analytics giúp phân tích hành trình người dùng từ view đến purchase. 
- Dashboard Marketing Performance đánh giá hiệu quả traffic source và campaign. 
- Dashboard Product Analytics tập trung vào doanh thu, số lượng bán, hiệu quả category, brand, premium product và refund. 
- Dashboard A/B Testing giúp so sánh hiệu quả giữa các experiment group dựa trên conversion rate, add to cart rate, bounce rate và purchase trend.

### SƠ ĐỒ KIẾN TRÚC TỔNG THỂ

![Overall AWS E-commerce Analytics Data Pipeline](./images/overall-architecture.png)

Sơ đồ tổng thể của project có thể được mô tả theo luồng sau:

Kaggle Marketing & E-commerce Dataset

        |

        v

Local Preprocessing

Rename columns only

        |

        v

Amazon S3 Raw Zone

raw/events/

raw/products/

raw/transactions/

        |

        v

AWS Glue Crawler Raw

Raw metadata catalog

        |

        v

Amazon Athena Raw Validation

Schema checks, null checks, duplicates, abnormal values

        |

        v

AWS Glue Batch ETL Job

Clean, cast, validate, enrich, partition, convert to Parquet

        |

        v
Amazon S3 Curated Zone + Error Zone

curated/fact_events/

curated/dim_products/

curated/fact_transactions/

error/transactions/

        |

        v

AWS Glue Crawler Curated

Curated metadata catalog

        |

        v

Amazon Athena Semantic Views

Business-ready SQL views

        |

        v

Amazon QuickSight Dashboards

Executive, Funnel, Marketing, Product, A/B Testing

        |

        v

Automation & Monitoring

EventBridge Scheduler + Glue Workflow + EventBridge Rules + CloudWatch Logs + SNS Alert

Workshop mô phỏng một pipeline dữ liệu hoàn chỉnh theo hướng Data Engineering. Pipeline bao gồm đầy đủ các bước từ lưu trữ dữ liệu thô, catalog metadata, kiểm tra dữ liệu, ETL, xử lý lỗi, tối ưu định dạng lưu trữ, tạo semantic layer, xây dựng dashboard, tự động hóa lịch chạy và cảnh báo lỗi. Đây là nền tảng quan trọng trong các hệ thống phân tích dữ liệu hiện đại, đặc biệt phù hợp với vai trò Data Engineer hoặc AWS Data Engineer.
