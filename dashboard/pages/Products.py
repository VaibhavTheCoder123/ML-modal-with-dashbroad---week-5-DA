import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Products", layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "cleaned" /
    "global_superstore_features.csv"
)

st.title("📦 Product Dashboard")

category = (
    df.groupby("category")["profit"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category,
    x="category",
    y="profit",
    title="Profit by Category"
)

st.plotly_chart(fig, use_container_width=True)

sub = (
    df.groupby("sub_category")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

fig = px.bar(
    sub,
    x="sub_category",
    y="sales",
    title="Top Sub Categories"
)

st.plotly_chart(fig, use_container_width=True)

products = (
    df.groupby("product_name")["sales"]
    .sum()
    .nlargest(15)
    .reset_index()
)

fig = px.bar(
    products,
    x="product_name",
    y="sales",
    title="Top Products"
)

st.plotly_chart(fig, use_container_width=True)