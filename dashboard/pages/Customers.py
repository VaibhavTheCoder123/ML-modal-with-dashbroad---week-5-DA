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
    page_title="Customer Dashboard",
    page_icon="👤",
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

<h1>👤 Customer Dashboard</h1>

<p>
Analyze customer segments, top customers,
geographical distribution and customer purchasing behaviour.
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
    "👥 Customers",
    kpi["total_customers"]
)

c2.metric(
    "📦 Orders",
    kpi["total_orders"]
)

c3.metric(
    "💰 Sales",
    f"${kpi['total_sales']:,.0f}"
)

c4.metric(
    "📈 Profit",
    f"${kpi['total_profit']:,.0f}"
)

st.divider()

# ==========================================================
# CUSTOMER SEGMENTS
# ==========================================================

st.markdown("## 👥 Customer Segments")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        charts.sales_by_segment(df),
        use_container_width=True
    )

with col2:

    segment = analytics.customer_segments(df)

    fig = px.pie(
        segment,
        values="Sales",
        names="segment",
        hole=0.45,
        title="Sales Contribution by Segment"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# TOP CUSTOMERS
# ==========================================================

st.markdown("## ⭐ Top Customers")

st.plotly_chart(
    charts.top_customers(df, 20),
    use_container_width=True
)

st.divider()

# ==========================================================
# CUSTOMER DISTRIBUTION
# ==========================================================

st.markdown("## 🌍 Customers by Country")

country = (
    df.groupby("country")["customer_id"]
    .nunique()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

fig = px.bar(
    country,
    x="country",
    y="customer_id",
    title="Top 15 Countries by Customers"
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
# CUSTOMER TABLE
# ==========================================================

st.markdown("## 📋 Top Customer Details")

st.dataframe(
    analytics.top_customers(df, 20),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# EXPORT
# ==========================================================

st.markdown("## ⬇️ Export Customer Report")

csv = analytics.top_customers(df, 100).to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Customer Report",
    data=csv,
    file_name="customer_dashboard.csv",
    mime="text/csv",
    use_container_width=True
)