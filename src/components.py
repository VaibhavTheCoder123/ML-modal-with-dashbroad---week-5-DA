import streamlit as st

from src import analytics
from src import charts



# =========================
# KPI CARDS
# =========================

def show_kpis(df):

    kpi = analytics.get_kpis(df)


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "💰 Total Sales",
            f"${kpi['total_sales']:,.2f}"
        )


    with col2:
        st.metric(
            "📈 Total Profit",
            f"${kpi['total_profit']:,.2f}"
        )


    with col3:
        st.metric(
            "📦 Total Orders",
            kpi["total_orders"]
        )


    with col4:
        st.metric(
            "👤 Customers",
            kpi["total_customers"]
        )



# =========================
# EXECUTIVE SUMMARY
# =========================

def show_summary(df):

    summary = analytics.executive_summary(df)


    st.subheader("Executive Summary")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Sales",
            f"${summary['Sales']:,.2f}"
        )

        st.metric(
            "Orders",
            summary["Orders"]
        )


    with col2:

        st.metric(
            "Profit",
            f"${summary['Profit']:,.2f}"
        )

        st.metric(
            "Customers",
            summary["Customers"]
        )


    with col3:

        st.metric(
            "Products",
            summary["Products"]
        )

        st.metric(
            "Profit Margin",
            f"{summary['Profit Margin']:.2f}%"
        )



# =========================
# DATASET INFO
# =========================

def show_dataset_info(df):

    info = analytics.dataset_overview(df)


    st.subheader("Dataset Overview")


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Rows",
        info["Rows"]
    )


    col2.metric(
        "Columns",
        info["Columns"]
    )


    col3.metric(
        "Missing Values",
        info["Missing Values"]
    )


    col4.metric(
        "Duplicate Rows",
        info["Duplicate Rows"]
    )



# =========================
# FILTERS
# =========================

def dashboard_filters(df):

    st.sidebar.header("Filters")


    years = st.sidebar.multiselect(
        "Year",
        sorted(df["order_year"].dropna().unique())
    )


    markets = st.sidebar.multiselect(
        "Market",
        sorted(df["market"].dropna().unique())
    )


    categories = st.sidebar.multiselect(
        "Category",
        sorted(df["category"].dropna().unique())
    )


    segments = st.sidebar.multiselect(
        "Segment",
        sorted(df["segment"].dropna().unique())
    )


    return analytics.filter_dataframe(
        df,
        years=years if years else None,
        markets=markets if markets else None,
        categories=categories if categories else None,
        segments=segments if segments else None
    )



# =========================
# CHARTS
# =========================

def show_charts(df):

    st.subheader("Sales Analysis")


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



# =========================
# TABLES
# =========================

def show_tables(df):

    st.subheader("Top Products")

    st.dataframe(
        analytics.top_products(df),
        use_container_width=True
    )


    st.subheader("Top Customers")

    st.dataframe(
        analytics.top_customers(df),
        use_container_width=True
    )


    st.subheader("Category Profit")

    st.dataframe(
        analytics.profit_by_category(df),
        use_container_width=True
    )


    st.subheader("Shipping Analysis")

    st.dataframe(
        analytics.shipping_analysis(df),
        use_container_width=True
    )



# =========================
# COMPLETE DASHBOARD
# =========================

def dashboard_view(df):

    st.title("📊 Sales Analytics Dashboard")


    show_kpis(df)

    st.divider()


    show_summary(df)

    st.divider()


    show_dataset_info(df)

    st.divider()


    show_charts(df)

    st.divider()


    show_tables(df)