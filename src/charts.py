import plotly.express as px
import plotly.graph_objects as go


def yearly_sales(df):
    data = (
        df.groupby("order_year")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        data,
        x="order_year",
        y="sales",
        markers=True,
        title="Yearly Sales Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        hovermode="x unified"
    )

    return fig


def monthly_sales(df):
    data = (
        df.groupby("order_month")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="order_month",
        y="sales",
        title="Monthly Sales"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig


def sales_by_category(df):
    data = (
        df.groupby("category")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        data,
        names="category",
        values="sales",
        hole=0.45,
        title="Sales by Category"
    )

    fig.update_layout(height=450)

    return fig


def sales_by_segment(df):
    data = (
        df.groupby("segment")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="segment",
        y="sales",
        title="Sales by Segment"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig


def region_sales(df):
    data = (
        df.groupby("region")["sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="region",
        y="sales",
        title="Sales by Region"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig


def market_sales(df):
    data = (
        df.groupby("market")["sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="market",
        y="sales",
        title="Sales by Market"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig


def top_products(df, top_n=10):
    data = (
        df.groupby("product_name")["sales"]
        .sum()
        .nlargest(top_n)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="product_name",
        y="sales",
        title=f"Top {top_n} Products"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_tickangle=-35
    )

    return fig


def top_customers(df, top_n=10):
    data = (
        df.groupby("customer_name")["sales"]
        .sum()
        .nlargest(top_n)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="customer_name",
        y="sales",
        title=f"Top {top_n} Customers"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_tickangle=-35
    )

    return fig


def discount_profit(df):
    fig = px.scatter(
        df,
        x="discount",
        y="profit",
        color="category",
        title="Discount vs Profit"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def profit_distribution(df):
    fig = px.histogram(
        df,
        x="profit",
        nbins=40,
        title="Profit Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig