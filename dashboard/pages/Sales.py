import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Sales Dashboard", layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "cleaned" /
    "global_superstore_features.csv"
)

df["order_date"] = pd.to_datetime(df["order_date"])

st.title("📈 Sales Dashboard")

sales = df.groupby("order_year")["sales"].sum().reset_index()

fig = px.line(
    sales,
    x="order_year",
    y="sales",
    markers=True,
    title="Yearly Sales"
)

st.plotly_chart(fig, use_container_width=True)

monthly = (
    df.groupby("order_month")["sales"]
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

category = (
    df.groupby("category")["sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    category,
    values="sales",
    names="category",
    title="Category Sales"
)

st.plotly_chart(fig, use_container_width=True)

region = (
    df.groupby("region")["sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    region,
    x="region",
    y="sales",
    title="Region Sales"
)

st.plotly_chart(fig, use_container_width=True)

market = (
    df.groupby("market")["sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    market,
    x="market",
    y="sales",
    title="Market Sales"
)

st.plotly_chart(fig, use_container_width=True)