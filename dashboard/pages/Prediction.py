import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Profit Prediction", layout="wide")

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL = BASE_DIR / "models" / "best_model.pkl"

model = joblib.load(MODEL)

st.title("🤖 Profit Prediction")

col1, col2 = st.columns(2)

with col1:

    sales = st.number_input(
        "Sales",
        min_value=0.0,
        value=500.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=2
    )

    discount = st.slider(
        "Discount",
        0.0,
        1.0,
        0.1
    )

    shipping_cost = st.number_input(
        "Shipping Cost",
        min_value=0.0,
        value=25.0
    )

    shipping_days = st.slider(
        "Shipping Days",
        0,
        20,
        3
    )

with col2:

    category = st.selectbox(
        "Category",
        [
            "Furniture",
            "Office Supplies",
            "Technology"
        ]
    )

    sub_category = st.text_input(
        "Sub Category",
        "Phones"
    )

    segment = st.selectbox(
        "Segment",
        [
            "Consumer",
            "Corporate",
            "Home Office"
        ]
    )

    market = st.selectbox(
        "Market",
        [
            "Asia Pacific",
            "Europe",
            "US",
            "LATAM",
            "Africa"
        ]
    )

    ship_mode = st.selectbox(
        "Ship Mode",
        [
            "Standard Class",
            "Second Class",
            "First Class",
            "Same Day"
        ]
    )

if st.button("Predict Profit"):

    sample = pd.DataFrame(
        {
            "sales":[sales],
            "quantity":[quantity],
            "discount":[discount],
            "shipping_cost":[shipping_cost],
            "shipping_days":[shipping_days],
            "category":[category],
            "sub_category":[sub_category],
            "segment":[segment],
            "market":[market],
            "ship_mode":[ship_mode]
        }
    )

    prediction = model.predict(sample)[0]

    st.success(
        f"Predicted Profit : ${prediction:,.2f}"
    )