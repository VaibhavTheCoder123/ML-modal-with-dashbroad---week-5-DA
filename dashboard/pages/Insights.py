import sys
from pathlib import Path

import streamlit as st

# ==========================================================
# PROJECT ROOT
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ==========================================================
# IMPORTS
# ==========================================================

from src.utils import load_css
from src.data_loader import load_data
from src import analytics

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ==========================================================
# LOAD DATA
# ==========================================================

try:
    df = load_data()

except Exception as e:

    st.error(f"Unable to load dataset.\n\n{e}")
    st.stop()

# ==========================================================
# HERO
# ==========================================================

st.markdown(
"""
<div class="hero">

<h1>💡 Business Insights</h1>

<p>
Executive overview of business performance,
key findings and strategic recommendations
generated from the Global Superstore dataset.
</p>

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# KPI SECTION
# ==========================================================

kpi = analytics.get_kpis(df)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "💰 Total Sales",
    f"${kpi['total_sales']:,.0f}"
)

c2.metric(
    "📈 Total Profit",
    f"${kpi['total_profit']:,.0f}"
)

c3.metric(
    "📦 Total Orders",
    kpi["total_orders"]
)

c4.metric(
    "👤 Customers",
    kpi["total_customers"]
)

st.divider()

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("## 📊 Key Business Insights")

highest_category = analytics.sales_by_category(df).iloc[0]["category"]

highest_market = analytics.sales_by_market(df).iloc[0]["market"]

highest_region = analytics.sales_by_region(df).iloc[0]["region"]

top_product = analytics.top_products(df, 1).iloc[0]["product_name"]

top_customer = analytics.top_customers(df, 1).iloc[0]["customer_name"]

profit_margin = kpi["profit_margin"]

avg_discount = kpi["average_discount"]

shipping_days = kpi["average_shipping_days"]

st.success(
f"""
### 📈 Performance Highlights

- 🛍️ Highest Revenue Category: **{highest_category}**
- 🌍 Best Performing Market: **{highest_market}**
- 📍 Best Performing Region: **{highest_region}**
- ⭐ Top Selling Product: **{top_product}**
- 👤 Highest Revenue Customer: **{top_customer}**
- 💹 Profit Margin: **{profit_margin:.2f}%**
- 🎯 Average Discount: **{avg_discount:.2%}**
- 🚚 Average Shipping Time: **{shipping_days:.2f} Days**
"""
)

st.divider()

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

st.markdown("## 🚀 Strategic Recommendations")

st.info(
"""
### Growth Strategy

✅ Increase inventory for the highest-selling products.

✅ Invest more marketing budget in the best-performing markets.

✅ Focus promotions on low-performing categories.

✅ Introduce loyalty programs for top-value customers.

✅ Reduce shipping time to improve customer satisfaction.

✅ Review products with low profit margins.

✅ Monitor high-discount products to avoid unnecessary profit loss.

✅ Expand successful product categories into emerging markets.
"""
)

st.divider()

# ==========================================================
# DATA SUMMARY
# ==========================================================

st.markdown("## 📋 Dataset Overview")

summary = analytics.dataset_overview(df)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", summary["Rows"])

c2.metric("Columns", summary["Columns"])

c3.metric("Missing Values", summary["Missing Values"])

c4.metric("Duplicate Rows", summary["Duplicate Rows"])