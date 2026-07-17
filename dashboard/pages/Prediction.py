import sys
from pathlib import Path

import pandas as pd
import streamlit as st
import joblib

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
from src.data_loader import load_data, load_model

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Profit Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ==========================================================
# LOAD DATA & MODEL
# ==========================================================

try:

    df = load_data()

except Exception as e:

    st.error(f"Unable to load dataset.\n\n{e}")

    st.stop()

try:

    model = load_model()

except Exception:

    MODEL_PATH = (
        ROOT_DIR /
        "models" /
        "best_model.pkl"
    )

    model = joblib.load(MODEL_PATH)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown(
"""
<div class="hero">

<h1>🤖 AI Profit Prediction</h1>

<p>

Predict the expected profit of a retail order using the
trained Machine Learning model. Adjust business parameters
such as sales, discount, shipping and product category to
understand their impact on profitability.

</p>

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# INPUT SECTION
# ==========================================================

st.markdown("## 📝 Order Information")

left, right = st.columns(2)

with left:

    sales = st.number_input(
        "Sales ($)",
        min_value=0.0,
        value=500.0,
        step=50.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=2
    )

    discount = st.slider(
        "Discount",
        min_value=0.0,
        max_value=1.0,
        value=0.10,
        step=0.01
    )

    shipping_cost = st.number_input(
        "Shipping Cost ($)",
        min_value=0.0,
        value=25.0,
        step=5.0
    )

    shipping_days = st.slider(
        "Shipping Days",
        min_value=0,
        max_value=20,
        value=3
    )

with right:

    category = st.selectbox(
        "Category",
        sorted(
            df["category"]
            .dropna()
            .unique()
        )
    )

    sub_category = st.selectbox(
        "Sub Category",
        sorted(
            df[
                df["category"] == category
            ]["sub_category"]
            .dropna()
            .unique()
        )
    )

    segment = st.selectbox(
        "Customer Segment",
        sorted(
            df["segment"]
            .dropna()
            .unique()
        )
    )

    market = st.selectbox(
        "Market",
        sorted(
            df["market"]
            .dropna()
            .unique()
        )
    )

    ship_mode = st.selectbox(
        "Ship Mode",
        sorted(
            df["ship_mode"]
            .dropna()
            .unique()
        )
    )

st.divider()

# ==========================================================
# BUSINESS PREVIEW
# ==========================================================

st.markdown("## 📊 Current Order Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Sales",
    f"${sales:,.2f}"
)

c2.metric(
    "Quantity",
    quantity
)

c3.metric(
    "Discount",
    f"{discount:.0%}"
)

c4.metric(
    "Shipping Cost",
    f"${shipping_cost:,.2f}"
)

st.divider()

# ==========================================================
# PREDICT BUTTON
# ==========================================================

predict = st.button(
    "🚀 Predict Profit",
    use_container_width=True
)

if predict:

    sample = pd.DataFrame(
        {
            "sales": [sales],
            "quantity": [quantity],
            "discount": [discount],
            "shipping_cost": [shipping_cost],
            "shipping_days": [shipping_days],
            "category": [category],
            "sub_category": [sub_category],
            "segment": [segment],
            "market": [market],
            "ship_mode": [ship_mode]
        }
    )

    prediction = float(
        model.predict(sample)[0]
    )

    st.divider()

    st.markdown(
        "## 📈 Prediction Results"
    )

    r1, r2, r3 = st.columns(3)

    with r1:

        st.metric(
            "Predicted Profit",
            f"${prediction:,.2f}"
        )

    score = max(
        0,
        min(
            100,
            prediction / 10
        )
    )

    with r2:

        st.metric(
            "Profit Score",
            f"{score:.0f}/100"
        )

    with r3:

        if prediction < 0:

            risk = "High Risk"

        elif prediction < 100:

            risk = "Low Profit"

        elif prediction < 500:

            risk = "Moderate"

        else:

            risk = "Excellent"

        st.metric(
            "Prediction Status",
            risk
        )

            # ==========================================================
    # PROFIT SCORE
    # ==========================================================

    st.progress(score / 100)

    st.caption(
        f"Overall Profitability Score : {score:.0f}/100"
    )

    st.divider()

    # ==========================================================
    # BUSINESS RECOMMENDATION
    # ==========================================================

    st.markdown("## 💡 AI Business Recommendation")

    if prediction < 0:

        st.error(
            """
### ⚠ High Risk Order

This order is expected to generate a **loss**.

#### Suggestions

- Reduce discount offered
- Increase selling price
- Lower shipping cost
- Increase order quantity
- Review product pricing
- Consider changing shipping method
"""
        )

    elif prediction < 100:

        st.warning(
            """
### 🟡 Low Profit Order

The order is profitable but with a small margin.

#### Suggestions

- Slightly reduce discount
- Bundle products together
- Increase average order value
- Reduce logistics cost
"""
        )

    elif prediction < 500:

        st.info(
            """
### 🔵 Healthy Profit

This order is expected to perform well.

#### Suggestions

- Current pricing strategy is acceptable
- Keep inventory available
- Continue targeted promotions
- Monitor discount levels
"""
        )

    else:

        st.success(
            """
### 🟢 Excellent Profitability

This order is highly profitable.

#### Suggestions

- Prioritize similar customers
- Increase marketing for this segment
- Keep products well stocked
- Use this strategy for future campaigns
"""
        )

    st.divider()

    # ==========================================================
    # ORDER SUMMARY
    # ==========================================================

    st.markdown("## 📋 Order Summary")

    summary = pd.DataFrame(
        {
            "Feature": [
                "Sales",
                "Quantity",
                "Discount",
                "Shipping Cost",
                "Shipping Days",
                "Category",
                "Sub Category",
                "Segment",
                "Market",
                "Ship Mode",
                "Predicted Profit"
            ],

            "Value": [
                f"${sales:,.2f}",
                quantity,
                f"{discount:.0%}",
                f"${shipping_cost:,.2f}",
                shipping_days,
                category,
                sub_category,
                segment,
                market,
                ship_mode,
                f"${prediction:,.2f}"
            ]
        }
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ==========================================================
    # ORDER HEALTH
    # ==========================================================

    st.markdown("## 📊 Business Health Analysis")

    h1, h2, h3 = st.columns(3)

    with h1:

        if discount <= 0.15:
            st.success("✅ Discount Level")
        elif discount <= 0.30:
            st.warning("⚠ Medium Discount")
        else:
            st.error("❌ High Discount")

    with h2:

        if shipping_days <= 3:
            st.success("✅ Fast Shipping")
        elif shipping_days <= 7:
            st.warning("⚠ Normal Shipping")
        else:
            st.error("❌ Slow Shipping")

    with h3:

        if shipping_cost <= 30:
            st.success("✅ Shipping Cost")
        elif shipping_cost <= 60:
            st.warning("⚠ Medium Cost")
        else:
            st.error("❌ Expensive Shipping")

    st.divider()

    # ==========================================================
    # MODEL INFORMATION
    # ==========================================================

    st.markdown("## 🤖 Model Information")

    c1, c2 = st.columns(2)

    with c1:

        st.info(
            """
### Machine Learning Model

- Trained on Global Superstore Dataset
- Regression Model
- Predicts Expected Profit
- Supports Numerical & Categorical Features
"""
        )

    with c2:

        st.info(
            """
### Input Features

- Sales
- Quantity
- Discount
- Shipping Cost
- Shipping Days
- Category
- Sub Category
- Segment
- Market
- Ship Mode
"""
        )

    st.divider()

    # ==========================================================
    # DOWNLOAD REPORT
    # ==========================================================

    report = summary.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Prediction Report",
        data=report,
        file_name="prediction_report.csv",
        mime="text/csv",
        use_container_width=True
    )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "© 2026 StoreScope • AI-Powered Retail Intelligence Dashboard"
)