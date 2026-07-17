import streamlit as st


def sidebar_filters(df):

    st.sidebar.header("Filters")


    years = sorted(
        df["order_year"].unique()
    )

    selected_year = st.sidebar.multiselect(
        "Year",
        years,
        default=years
    )


    categories = sorted(
        df["category"].unique()
    )

    selected_category = st.sidebar.multiselect(
        "Category",
        categories,
        default=categories
    )


    markets = sorted(
        df["market"].unique()
    )

    selected_market = st.sidebar.multiselect(
        "Market",
        markets,
        default=markets
    )


    return (
        selected_year,
        selected_category,
        selected_market
    )



def show_kpis(kpis):

    c1, c2, c3, c4 = st.columns(4)


    c1.metric(
        "💰 Sales",
        f"${kpis['sales']:,.0f}"
    )


    c2.metric(
        "📈 Profit",
        f"${kpis['profit']:,.0f}"
    )


    c3.metric(
        "📦 Orders",
        kpis["orders"]
    )


    c4.metric(
        "👤 Customers",
        kpis["customers"]
    )