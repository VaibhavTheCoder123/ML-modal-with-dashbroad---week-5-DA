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
from src import charts

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📈",
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

<h1>📈 Sales Dashboard</h1>

<p>
Explore yearly trends, monthly performance,
regional distribution, market analysis and
category-wise sales using interactive charts.
</p>

</div>
""",
    unsafe_allow_html=True
)

# ==========================================================
# SALES TRENDS
# ==========================================================

st.markdown("## 📊 Sales Trends")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        charts.yearly_sales(df),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        charts.monthly_sales(df),
        use_container_width=True
    )

st.divider()

# ==========================================================
# CATEGORY ANALYSIS
# ==========================================================

st.markdown("## 🛍️ Category Analysis")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        charts.sales_by_category(df),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        charts.sales_by_segment(df),
        use_container_width=True
    )

st.divider()

# ==========================================================
# GEOGRAPHICAL ANALYSIS
# ==========================================================

st.markdown("## 🌍 Regional Performance")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        charts.region_sales(df),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        charts.market_sales(df),
        use_container_width=True
    )

st.divider()

# ==========================================================
# DATA PREVIEW
# ==========================================================

st.markdown("## 📋 Sales Dataset Preview")

st.dataframe(
    df[
        [
            "order_year",
            "order_month",
            "category",
            "segment",
            "market",
            "region",
            "sales",
            "profit",
        ]
    ].head(20),
    use_container_width=True,
    hide_index=True,
)

# ==========================================================
# DOWNLOAD
# ==========================================================

st.markdown("## ⬇️ Export Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Sales Dataset",
    data=csv,
    file_name="sales_dashboard_data.csv",
    mime="text/csv",
    use_container_width=True,
)