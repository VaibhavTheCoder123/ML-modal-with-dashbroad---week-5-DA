import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Customers", layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "cleaned" /
    "global_superstore_features.csv"
)

st.title("👤 Customer Dashboard")

segment = (
    df.groupby("segment")["sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    segment,
    values="sales",
    names="segment",
    title="Customer Segment"
)

st.plotly_chart(fig, use_container_width=True)

top = (
    df.groupby("customer_name")["sales"]
    .sum()
    .nlargest(20)
    .reset_index()
)

fig = px.bar(
    top,
    x="customer_name",
    y="sales",
    title="Top Customers"
)

st.plotly_chart(fig, use_container_width=True)

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
    title="Customers by Country"
)

st.plotly_chart(fig, use_container_width=True)