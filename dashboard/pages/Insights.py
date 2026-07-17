import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Business Insights", layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]

DATA = BASE_DIR / "data" / "cleaned" / "global_superstore_features.csv"

df = pd.read_csv(DATA)

st.title("📋 Business Insights")

sales = df["sales"].sum()
profit = df["profit"].sum()
orders = df["order_id"].nunique()
customers = df["customer_id"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Sales", f"${sales:,.0f}")
c2.metric("Profit", f"${profit:,.0f}")
c3.metric("Orders", orders)
c4.metric("Customers", customers)

st.divider()

highest_category = (
    df.groupby("category")["sales"]
    .sum()
    .idxmax()
)

highest_market = (
    df.groupby("market")["sales"]
    .sum()
    .idxmax()
)

highest_product = (
    df.groupby("product_name")["sales"]
    .sum()
    .idxmax()
)

highest_customer = (
    df.groupby("customer_name")["sales"]
    .sum()
    .idxmax()
)

st.subheader("Key Business Insights")

st.success(
    f"""
• Highest Revenue Category : {highest_category}

• Best Performing Market : {highest_market}

• Top Product : {highest_product}

• Highest Revenue Customer : {highest_customer}
"""
)

st.subheader("Recommendations")

st.info(
"""
✅ Increase inventory for top-selling products.

✅ Focus marketing on the highest-performing market.

✅ Improve discounts for low-performing categories.

✅ Reward high-value customers.

✅ Reduce shipping time where possible.

✅ Monitor loss-making products regularly.
"""
)