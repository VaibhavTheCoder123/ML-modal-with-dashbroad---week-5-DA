import streamlit as st
from pathlib import Path

from src import analytics
from src import charts


# ==========================================================
# SIDEBAR
# ==========================================================

def dashboard_filters(df):

    logo = (
        Path(__file__).resolve().parent.parent
        / "dashboard"
        / "assets"
        / "logo.png"
    )

    if logo.exists():
        st.sidebar.image(str(logo), width=180)

    st.sidebar.markdown("## 🎯 Dashboard Filters")
    st.sidebar.markdown("---")

    year_list = sorted(
        df["order_year"].dropna().unique()
    )

    years = st.sidebar.multiselect(
        "Year",
        year_list,
        default=year_list
    )

    market_list = sorted(
        df["market"].dropna().unique()
    )

    markets = st.sidebar.multiselect(
        "Market",
        market_list,
        default=market_list
    )

    category_list = sorted(
        df["category"].dropna().unique()
    )

    categories = st.sidebar.multiselect(
        "Category",
        category_list,
        default=category_list
    )

    segment_list = sorted(
        df["segment"].dropna().unique()
    )

    segments = st.sidebar.multiselect(
        "Segment",
        segment_list,
        default=segment_list
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        f"{len(df):,} Records Loaded"
    )

    filtered = analytics.filter_dataframe(
        df,
        years=years,
        markets=markets,
        categories=categories,
        segments=segments
    )

    return filtered


# ==========================================================
# KPI CARDS
# ==========================================================

def show_kpis(df):

    kpi = analytics.get_kpis(df)

    st.subheader("📊 Key Performance Indicators")

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
        "📦 Orders",
        f"{kpi['total_orders']:,}"
    )

    c4.metric(
        "👤 Customers",
        f"{kpi['total_customers']:,}"
    )


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def show_summary(df):

    summary = analytics.executive_summary(df)

    st.subheader("📈 Executive Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Sales",
            f"${summary['Sales']:,.0f}"
        )

        st.metric(
            "Orders",
            f"{summary['Orders']:,}"
        )

    with col2:

        st.metric(
            "Profit",
            f"${summary['Profit']:,.0f}"
        )

        st.metric(
            "Customers",
            f"{summary['Customers']:,}"
        )

    with col3:

        st.metric(
            "Products",
            f"{summary['Products']:,}"
        )

        st.metric(
            "Profit Margin",
            f"{summary['Profit Margin']:.2f}%"
        )


# ==========================================================
# DATASET INFO
# ==========================================================

def show_dataset_info(df):

    info = analytics.dataset_overview(df)

    with st.expander(
        "📁 Dataset Information",
        expanded=False
    ):

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Rows",
            f"{info['Rows']:,}"
        )

        c2.metric(
            "Columns",
            info["Columns"]
        )

        c3.metric(
            "Missing",
            info["Missing Values"]
        )

        c4.metric(
            "Duplicates",
            info["Duplicate Rows"]
        )


# ==========================================================
# SALES CHARTS
# ==========================================================

def show_charts(df):

    st.subheader("📈 Sales Performance")

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            charts.yearly_sales(df),
            use_container_width=True
        )

    with right:

        st.plotly_chart(
            charts.monthly_sales(df),
            use_container_width=True
        )

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            charts.sales_by_category(df),
            use_container_width=True
        )

    with right:

        st.plotly_chart(
            charts.sales_by_segment(df),
            use_container_width=True
        )

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            charts.region_sales(df),
            use_container_width=True
        )

    with right:

        st.plotly_chart(
            charts.market_sales(df),
            use_container_width=True
        )

    left, right = st.columns(2)

    with left:

        st.plotly_chart(
            charts.profit_by_category(df),
            use_container_width=True
        )

    with right:

        st.plotly_chart(
            charts.discount_profit(df),
            use_container_width=True
        )

    st.plotly_chart(
        charts.profit_distribution(df),
        use_container_width=True
    )

# ==========================================================
# TABLES
# ==========================================================

def show_tables(df):

    st.subheader("📋 Detailed Analysis")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📦 Products",
            "👥 Customers",
            "💰 Profit",
            "🚚 Shipping"
        ]
    )

    with tab1:

        st.markdown("### Top Selling Products")

        st.dataframe(
            analytics.top_products(df),
            use_container_width=True,
            hide_index=True
        )

    with tab2:

        st.markdown("### Top Customers")

        st.dataframe(
            analytics.top_customers(df),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Top Countries")

        st.dataframe(
            analytics.top_countries(df),
            use_container_width=True,
            hide_index=True
        )

    with tab3:

        st.markdown("### Profit by Category")

        st.dataframe(
            analytics.profit_by_category(df),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Customer Segments")

        st.dataframe(
            analytics.customer_segments(df),
            use_container_width=True,
            hide_index=True
        )

    with tab4:

        st.markdown("### Shipping Analysis")

        st.dataframe(
            analytics.shipping_analysis(df),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Discount Analysis")

        st.dataframe(
            analytics.discount_analysis(df),
            use_container_width=True,
            hide_index=True
        )


# ==========================================================
# DATA PREVIEW
# ==========================================================

def show_dataset_preview(df):

    st.subheader("📄 Dataset Preview")

    preview_rows = st.slider(
        "Rows to Display",
        min_value=5,
        max_value=100,
        value=20,
        step=5
    )

    st.dataframe(
        df.head(preview_rows),
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# DOWNLOAD
# ==========================================================

def download_section(df):

    st.subheader("⬇ Export Data")

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(

        label="Download Filtered Dataset",

        data=csv,

        file_name="storescope_filtered_data.csv",

        mime="text/csv",

        use_container_width=True
    )


# ==========================================================
# FOOTER
# ==========================================================

def footer():

    st.markdown("---")

    col1, col2 = st.columns([3, 1])

    with col1:

        st.caption(
            "© 2026 StoreScope • Retail Intelligence Dashboard"
        )

    with col2:

        st.caption(
            "Built with ❤️ Streamlit + Plotly"
        )


# ==========================================================
# COMPLETE DASHBOARD
# ==========================================================

def dashboard_view(df):

    if df.empty:

        st.warning(
            "⚠ No records found for the selected filters."
        )

        return

    show_kpis(df)

    st.markdown("<br>", unsafe_allow_html=True)

    show_summary(df)

    st.markdown("<br>", unsafe_allow_html=True)

    show_dataset_info(df)

    st.markdown("<br>", unsafe_allow_html=True)

    show_charts(df)

    st.markdown("<br>", unsafe_allow_html=True)

    show_tables(df)

    st.markdown("<br>", unsafe_allow_html=True)

    show_dataset_preview(df)

    st.markdown("<br>", unsafe_allow_html=True)

    download_section(df)

    footer()