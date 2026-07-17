import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Retail Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATA = BASE_DIR / "data" / "cleaned" / "global_superstore_features.csv"

df = pd.read_csv(DATA)

df["order_date"] = pd.to_datetime(df["order_date"])

st.title("📊 Retail Analytics Dashboard")

st.markdown(
    "Interactive dashboard for Global Superstore Sales Analysis"
)

st.sidebar.header("Filters")

years = sorted(df["order_year"].unique())

selected_year = st.sidebar.multiselect(
    "Year",
    years,
    default=years
)

categories = sorted(df["category"].unique())

selected_category = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)

markets = sorted(df["market"].unique())

selected_market = st.sidebar.multiselect(
    "Market",
    markets,
    default=markets
)

filtered = df[
    (df["order_year"].isin(selected_year))
    &
    (df["category"].isin(selected_category))
    &
    (df["market"].isin(selected_market))
]

sales = filtered["sales"].sum()
profit = filtered["profit"].sum()
orders = filtered["order_id"].nunique()
customers = filtered["customer_id"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Sales", f"${sales:,.0f}")

c2.metric("📈 Profit", f"${profit:,.0f}")

c3.metric("📦 Orders", orders)

c4.metric("👤 Customers", customers)

st.divider()

left, right = st.columns(2)

with left:

    yearly = (
        filtered.groupby("order_year")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        yearly,
        x="order_year",
        y="sales",
        markers=True,
        title="Yearly Sales"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    monthly = (
        filtered.groupby("order_month")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        monthly,
        x="order_month",
        y="sales",
        title="Monthly Sales"
    )

    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)

with left:

    category = (
        filtered.groupby("category")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category,
        values="sales",
        names="category",
        title="Sales by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    segment = (
        filtered.groupby("segment")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        segment,
        x="segment",
        y="sales",
        title="Sales by Segment"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Dataset Preview")

st.dataframe(filtered.head(20), use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Filtered Dataset",
    csv,
    "filtered_data.csv",
    "text/csv"
)