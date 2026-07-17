import sys
from pathlib import Path

import streamlit as st
import plotly.express as px

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
from src import charts

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Product Dashboard",
    page_icon="📦",
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
# HERO SECTION
# ==========================================================

st.markdown(
    """
<div class="hero">

<h1>📦 Product Dashboard</h1>

<p>
Analyze product performance, category profitability,
sub-category trends and top-selling products across
the Global Superstore dataset.
</p>

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# CATEGORY ANALYSIS
# ==========================================================

st.markdown("## 📊 Category Performance")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        charts.profit_by_category(df),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        charts.sales_by_category(df),
        use_container_width=True
    )

st.divider()

# ==========================================================
# TOP SUB-CATEGORIES
# ==========================================================

st.markdown("## 🏷️ Top Selling Sub-Categories")

subcategory = analytics.sales_by_subcategory(df).head(15)

fig = px.bar(
    subcategory,
    x="sub_category",
    y="sales",
    title="Top 15 Sub-Categories"
)

fig.update_layout(
    xaxis_tickangle=-35,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# TOP PRODUCTS
# ==========================================================

st.markdown("## ⭐ Top Selling Products")

st.plotly_chart(
    charts.top_products(df, 15),
    use_container_width=True
)

st.divider()

# ==========================================================
# PRODUCT TABLE
# ==========================================================

st.markdown("## 📋 Best Performing Products")

st.dataframe(
    analytics.top_products(df, 20),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# DOWNLOAD
# ==========================================================

st.markdown("## ⬇️ Export Product Data")

csv = analytics.top_products(df, 100).to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Product Report",
    data=csv,
    file_name="product_dashboard.csv",
    mime="text/csv",
    use_container_width=True
)