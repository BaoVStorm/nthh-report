import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(18, 26))
ax.set_xlim(0, 18)
ax.set_ylim(0, 26)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')
ax.set_facecolor('#F8F9FA')

# ── Color palette ──────────────────────────────────────────────────────────────
C_STORAGE   = '#1A9E8F'   # teal  – S3
C_STORAGE_L = '#D4F5F0'
C_CATALOG   = '#7B5EA7'   # purple – Glue / Athena
C_CATALOG_L = '#EDE7F6'
C_TRANSFORM = '#E67E22'   # amber – ETL
C_TRANSFORM_L = '#FEF3E2'
C_VIZ       = '#27AE60'   # green – QuickSight
C_VIZ_L     = '#E8F8EE'
C_ERROR     = '#E74C3C'   # coral – Error zone
C_ERROR_L   = '#FDECEA'
C_LOCAL     = '#2C3E50'   # dark  – Local
C_LOCAL_L   = '#ECF0F1'
C_ARROW     = '#546E7A'
C_LABEL_BG  = '#DDE3EA'

# ── Helper functions ───────────────────────────────────────────────────────────
def rounded_box(ax, x, y, w, h, fc, ec, lw=1.8, radius=0.35):
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad=0,rounding_size={radius}",
                         facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3)
    ax.add_patch(box)

def arrow(ax, x1, y1, x2, y2, color=C_ARROW, lw=2.0, style='->', dashed=False):
    ls = (0, (5, 4)) if dashed else 'solid'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=lw, linestyle=ls),
                zorder=4)

def label_text(ax, x, y, txt, fs=9, color='#2C3E50', bold=False, ha='center', va='center'):
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, txt, fontsize=fs, color=color, ha=ha, va=va,
            fontweight=weight, zorder=5)

def layer_label(ax, y_center, text):
    rounded_box(ax, 0.15, y_center - 0.38, 1.55, 0.76, C_LABEL_BG, '#90A4AE', lw=1.2, radius=0.2)
    ax.text(0.925, y_center, text, fontsize=8.5, color='#37474F',
            ha='center', va='center', fontweight='bold', zorder=5)

def icon_circle(ax, cx, cy, r, color):
    circle = plt.Circle((cx, cy), r, color=color, zorder=4)
    ax.add_patch(circle)

# ══════════════════════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════════════════════
rounded_box(ax, 1.9, 24.5, 14.2, 1.1, '#2C3E50', '#1A252F', lw=2, radius=0.4)
ax.text(9.0, 25.1, 'AWS E-Commerce Analytics Pipeline — Overall Architecture',
        fontsize=15, color='white', ha='center', va='center',
        fontweight='bold', zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
# ROW 1 — SOURCE  (y ≈ 22.5)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 22.55, 'SOURCE')

# Kaggle box
rounded_box(ax, 2.1, 22.0, 5.8, 1.1, C_LOCAL_L, C_LOCAL, lw=2, radius=0.3)
icon_circle(ax, 2.75, 22.55, 0.28, C_LOCAL)
ax.text(2.75, 22.55, '📦', fontsize=11, ha='center', va='center', zorder=6)
label_text(ax, 5.0, 22.72, 'Kaggle Dataset', fs=10, bold=True)
label_text(ax, 5.0, 22.35, 'Marketing & E-Commerce Analytics Dataset', fs=8.5, color='#555')

# Arrow →
arrow(ax, 7.9, 22.55, 9.3, 22.55)

# Local Preprocessing box
rounded_box(ax, 9.3, 22.0, 6.4, 1.1, C_LOCAL_L, C_LOCAL, lw=2, radius=0.3)
ax.text(9.9, 22.55, '⚙️', fontsize=13, ha='center', va='center', zorder=6)
label_text(ax, 12.5, 22.72, 'Local Preprocessing', fs=10, bold=True)
label_text(ax, 12.5, 22.35, 'Rename: timestamp → event_timestamp / transaction_timestamp', fs=8, color='#555')

# ══════════════════════════════════════════════════════════════════════════════
# ROW 2 — INGEST  (y ≈ 20.0)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 20.05, 'INGEST')

arrow(ax, 12.5, 22.0, 9.0, 21.15, color=C_STORAGE)

# S3 Raw Zone
rounded_box(ax, 2.1, 19.3, 13.8, 1.5, C_STORAGE_L, C_STORAGE, lw=2.2, radius=0.35)
ax.text(2.75, 20.05, '🪣', fontsize=14, ha='center', va='center', zorder=6)
label_text(ax, 9.0, 20.55, 'Amazon S3 — Raw Zone', fs=11, bold=True, color=C_STORAGE)
label_text(ax, 5.2, 20.05, 'raw/events/  (events.csv)', fs=9, color='#2C3E50')
label_text(ax, 9.0, 20.05, 'raw/products/  (products.csv)', fs=9, color='#2C3E50')
label_text(ax, 13.0, 20.05, 'raw/transactions/  (transactions.csv)', fs=9, color='#2C3E50')
# dividers
for xd in [7.0, 11.0]:
    ax.plot([xd, xd], [19.35, 20.75], color=C_STORAGE, lw=1, ls='--', zorder=4, alpha=0.5)

# ══════════════════════════════════════════════════════════════════════════════
# ROW 3 — CATALOG  (y ≈ 17.3)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 17.35, 'CATALOG')

arrow(ax, 9.0, 19.3, 9.0, 18.45, color=C_CATALOG)

# Glue Crawler Raw
rounded_box(ax, 2.1, 17.0, 4.5, 0.9, C_CATALOG_L, C_CATALOG, lw=2, radius=0.3)
ax.text(2.7, 17.45, '🔍', fontsize=12, ha='center', va='center', zorder=6)
label_text(ax, 4.35, 17.6, 'Glue Crawler Raw', fs=9.5, bold=True, color=C_CATALOG)
label_text(ax, 4.35, 17.25, 'crawler_ecommerce_raw', fs=8, color='#555')

arrow(ax, 6.6, 17.45, 7.5, 17.45, color=C_CATALOG)

# Glue DB Raw
rounded_box(ax, 7.5, 17.0, 3.8, 0.9, C_CATALOG_L, C_CATALOG, lw=2, radius=0.3)
ax.text(8.05, 17.45, '🗄️', fontsize=12, ha='center', va='center', zorder=6)
label_text(ax, 9.4, 17.6, 'Glue Database', fs=9.5, bold=True, color=C_CATALOG)
label_text(ax, 9.4, 17.25, 'ecommerce_raw', fs=8, color='#555')

arrow(ax, 11.3, 17.45, 12.2, 17.45, color=C_CATALOG)

# Athena Raw Validation
rounded_box(ax, 12.2, 17.0, 3.7, 0.9, C_CATALOG_L, C_CATALOG, lw=2, radius=0.3)
ax.text(12.75, 17.45, '🔎', fontsize=12, ha='center', va='center', zorder=6)
label_text(ax, 14.05, 17.6, 'Athena Validation', fs=9.5, bold=True, color=C_CATALOG)
label_text(ax, 14.05, 17.25, 'Schema / Null / Duplicate checks', fs=7.8, color='#555')

# ══════════════════════════════════════════════════════════════════════════════
# ROW 4 — TRANSFORM  (y ≈ 14.9)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 14.95, 'TRANSFORM')

arrow(ax, 9.0, 17.0, 9.0, 15.85, color=C_TRANSFORM)

# Glue ETL Job
rounded_box(ax, 3.5, 14.3, 11.0, 1.3, C_TRANSFORM_L, C_TRANSFORM, lw=2.2, radius=0.35)
ax.text(4.2, 14.95, '⚡', fontsize=14, ha='center', va='center', zorder=6)
label_text(ax, 9.0, 15.35, 'AWS Glue ETL Job  —  etl_ecommerce_raw_to_curated_1', fs=10.5, bold=True, color=C_TRANSFORM)
label_text(ax, 9.0, 14.85, 'PySpark  |  Read CSV → Clean / Cast / Normalize / Validate → Write Parquet  |  Partition by year/month/day', fs=8.5, color='#555')

# ══════════════════════════════════════════════════════════════════════════════
# ROW 5 — STORAGE (Curated + Error)  (y ≈ 12.2)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 12.25, 'STORE')

# Arrow to Curated
arrow(ax, 7.5, 14.3, 6.5, 13.2, color=C_STORAGE)
# Arrow to Error
arrow(ax, 10.5, 14.3, 13.0, 13.2, color=C_ERROR)

# S3 Curated Zone
rounded_box(ax, 2.1, 11.5, 8.5, 1.45, C_STORAGE_L, C_STORAGE, lw=2.2, radius=0.35)
ax.text(2.75, 12.22, '🪣', fontsize=14, ha='center', va='center', zorder=6)
label_text(ax, 6.35, 12.65, 'Amazon S3 — Curated Zone', fs=10, bold=True, color=C_STORAGE)
label_text(ax, 4.0, 12.15, 'fact_events/', fs=8.8, color='#2C3E50')
label_text(ax, 6.35, 12.15, 'dim_products/', fs=8.8, color='#2C3E50')
label_text(ax, 8.7, 12.15, 'fact_transactions/', fs=8.8, color='#2C3E50')
label_text(ax, 6.35, 11.75, 'Parquet  |  Partitioned by year/month/day', fs=8, color='#777')
for xd in [5.1, 7.6]:
    ax.plot([xd, xd], [11.55, 12.85], color=C_STORAGE, lw=1, ls='--', zorder=4, alpha=0.5)

# S3 Error Zone
rounded_box(ax, 11.3, 11.5, 4.6, 1.45, C_ERROR_L, C_ERROR, lw=2.2, radius=0.35)
ax.text(11.9, 12.22, '⚠️', fontsize=13, ha='center', va='center', zorder=6)
label_text(ax, 13.6, 12.65, 'S3 — Error Zone', fs=10, bold=True, color=C_ERROR)
label_text(ax, 13.6, 12.2, 'error/transactions/', fs=8.8, color='#2C3E50')
label_text(ax, 13.6, 11.78, 'Invalid / null product_id records', fs=8, color='#777')

# ══════════════════════════════════════════════════════════════════════════════
# ROW 6 — CATALOG Curated  (y ≈ 9.7)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 9.75, 'CATALOG')

arrow(ax, 6.35, 11.5, 6.35, 10.6, color=C_CATALOG)

# Glue Crawler Curated
rounded_box(ax, 2.1, 9.2, 4.8, 0.9, C_CATALOG_L, C_CATALOG, lw=2, radius=0.3)
ax.text(2.75, 9.65, '🔍', fontsize=12, ha='center', va='center', zorder=6)
label_text(ax, 4.5, 9.8, 'Glue Crawler Curated', fs=9.5, bold=True, color=C_CATALOG)
label_text(ax, 4.5, 9.45, 'crawler_ecommerce_curated', fs=8, color='#555')

arrow(ax, 6.9, 9.65, 7.9, 9.65, color=C_CATALOG)

# Glue DB Curated
rounded_box(ax, 7.9, 9.2, 4.0, 0.9, C_CATALOG_L, C_CATALOG, lw=2, radius=0.3)
ax.text(8.5, 9.65, '🗄️', fontsize=12, ha='center', va='center', zorder=6)
label_text(ax, 9.9, 9.8, 'Glue Database', fs=9.5, bold=True, color=C_CATALOG)
label_text(ax, 9.9, 9.45, 'ecommerce_curated', fs=8, color='#555')

# ══════════════════════════════════════════════════════════════════════════════
# ROW 7 — SERVE  (y ≈ 7.2)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 7.25, 'SERVE')

arrow(ax, 9.9, 9.2, 9.0, 8.15, color=C_CATALOG)

# Athena Semantic Views
rounded_box(ax, 2.1, 6.5, 13.8, 1.45, C_CATALOG_L, C_CATALOG, lw=2.2, radius=0.35)
ax.text(2.75, 7.22, '📊', fontsize=14, ha='center', va='center', zorder=6)
label_text(ax, 9.0, 7.65, 'Amazon Athena — Semantic Views', fs=10.5, bold=True, color=C_CATALOG)
views = ['vw_daily_revenue', 'vw_funnel_analysis', 'vw_campaign_performance', 'vw_ab_testing_summary']
xs = [4.2, 7.5, 10.8, 14.1]
for xv, vn in zip(xs, views):
    rounded_box(ax, xv - 1.3, 6.6, 2.6, 0.65, '#EDE7F6', C_CATALOG, lw=1.2, radius=0.2)
    label_text(ax, xv, 6.925, vn, fs=8, color=C_CATALOG, bold=True)

# ══════════════════════════════════════════════════════════════════════════════
# ROW 8 — VISUALIZE  (y ≈ 4.5)
# ══════════════════════════════════════════════════════════════════════════════
layer_label(ax, 4.55, 'VISUALIZE')

arrow(ax, 9.0, 6.5, 9.0, 5.45, color=C_VIZ)

# QuickSight Dashboards
rounded_box(ax, 2.1, 3.8, 13.8, 1.45, C_VIZ_L, C_VIZ, lw=2.2, radius=0.35)
ax.text(2.75, 4.52, '📈', fontsize=14, ha='center', va='center', zorder=6)
label_text(ax, 9.0, 5.0, 'Amazon QuickSight — Dashboards  (Direct Query via Athena)', fs=10.5, bold=True, color=C_VIZ)
dashboards = ['Revenue\nOverview', 'Funnel\nAnalytics', 'Campaign\nPerformance', 'A/B Testing\nAnalysis']
dash_colors = ['#1A9E8F', '#7B5EA7', '#E67E22', '#27AE60']
xs_d = [4.2, 7.5, 10.8, 14.1]
for xd, dn, dc in zip(xs_d, dashboards, dash_colors):
    rounded_box(ax, xd - 1.3, 3.9, 2.6, 0.75, 'white', dc, lw=1.8, radius=0.2)
    label_text(ax, xd, 4.275, dn, fs=8, color=dc, bold=True)

# ══════════════════════════════════════════════════════════════════════════════
# AUTOMATION BANNER  (y ≈ 1.5)
# ══════════════════════════════════════════════════════════════════════════════
# Dashed border banner
banner = FancyBboxPatch((1.8, 0.5), 14.4, 2.6,
                        boxstyle="round,pad=0,rounding_size=0.3",
                        facecolor='#FFF8E1', edgecolor='#F39C12',
                        linewidth=2, linestyle=(0, (6, 3)), zorder=3)
ax.add_patch(banner)

label_text(ax, 9.0, 2.75, '⚡  Automation & Monitoring Layer', fs=10.5, bold=True, color='#E67E22')

# EventBridge → Glue Workflow → SNS
components = [
    ('EventBridge\nScheduler', 'cron: 09:00 daily', '#F39C12', 3.5),
    ('Glue\nWorkflow', 'Raw Crawler → ETL → Curated Crawler', '#7B5EA7', 7.8),
    ('EventBridge\nRules', 'Detect Job/Crawler failures', '#E74C3C', 11.5),
    ('SNS\nAlerts', 'Email on failure', '#27AE60', 14.8),
]
prev_x = None
for name, sub, color, cx in components:
    rounded_box(ax, cx - 1.4, 0.75, 2.8, 1.3, 'white', color, lw=1.8, radius=0.25)
    label_text(ax, cx, 1.55, name, fs=9, bold=True, color=color)
    label_text(ax, cx, 1.1, sub, fs=7.5, color='#555')
    if prev_x is not None:
        arrow(ax, prev_x + 1.4, 1.4, cx - 1.4, 1.4, color='#F39C12', lw=1.8)
    prev_x = cx

# Arrow from QuickSight down to automation banner (dashed)
arrow(ax, 9.0, 3.8, 9.0, 3.12, color='#90A4AE', lw=1.5, dashed=True)

# ══════════════════════════════════════════════════════════════════════════════
# LEGEND
# ══════════════════════════════════════════════════════════════════════════════
legend_items = [
    (C_STORAGE,   C_STORAGE_L,   'Storage (S3)'),
    (C_CATALOG,   C_CATALOG_L,   'Catalog / Query (Glue, Athena)'),
    (C_TRANSFORM, C_TRANSFORM_L, 'Transform (Glue ETL)'),
    (C_VIZ,       C_VIZ_L,       'Visualize (QuickSight)'),
    (C_ERROR,     C_ERROR_L,     'Error Path'),
]
lx, ly = 2.2, 0.32
for i, (ec, fc, lbl) in enumerate(legend_items):
    bx = lx + i * 3.1
    rounded_box(ax, bx, 0.1, 0.55, 0.32, fc, ec, lw=1.5, radius=0.08)
    label_text(ax, bx + 0.85, 0.26, lbl, fs=7.8, color='#37474F', ha='left')

plt.tight_layout(pad=0.3)
plt.savefig('aws_pipeline_architecture.png', dpi=180, bbox_inches='tight',
            facecolor=fig.get_facecolor())
print("Diagram saved: aws_pipeline_architecture.png")
