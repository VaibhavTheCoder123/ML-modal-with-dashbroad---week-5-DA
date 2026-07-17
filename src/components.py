import streamlit as st


def sidebar():

    with st.sidebar:

        st.image("dashboard/assets/logo.png", width=110)

        st.markdown("# StoreScope")

        st.caption(
            "Business Intelligence Platform"
        )

        st.divider()

        st.markdown("### 📊 Dashboard")

        st.success(
            """
Model

Gradient Boosting

R² Score : 0.672
"""
        )

        st.divider()

        st.caption(
            "Developed by Vaibhav Jain"
        )   