import plotly.express as px



# ==========================
# COMMON SETTINGS
# ==========================

CHART_HEIGHT = 450


def apply_layout(fig, height=CHART_HEIGHT):

    fig.update_layout(
        template="plotly_white",
        height=height,
        hovermode="x unified"
    )

    return fig



def empty_chart(title):

    fig = px.scatter(
        title=title
    )

    fig.update_layout(
        template="plotly_white",
        height=CHART_HEIGHT
    )

    return fig



# ==========================
# SALES TREND
# ==========================


def yearly_sales(df):

    if df.empty:
        return empty_chart("Yearly Sales Trend")


    data = (
        df.groupby("order_year", as_index=False)
        ["sales"]
        .sum()
    )


    fig = px.line(
        data,
        x="order_year",
        y="sales",
        markers=True,
        title="Yearly Sales Trend"
    )


    return apply_layout(fig)



def monthly_sales(df):

    if df.empty:
        return empty_chart("Monthly Sales")


    data = (
        df.groupby("order_month", as_index=False)
        ["sales"]
        .sum()
    )


    fig = px.bar(
        data,
        x="order_month",
        y="sales",
        title="Monthly Sales"
    )


    return apply_layout(fig)



# ==========================
# CATEGORY / SEGMENT
# ==========================


def sales_by_category(df):

    if df.empty:
        return empty_chart("Sales by Category")


    data = (
        df.groupby("category", as_index=False)
        ["sales"]
        .sum()
    )


    fig = px.pie(
        data,
        names="category",
        values="sales",
        hole=0.45,
        title="Sales by Category"
    )


    return apply_layout(fig)



def sales_by_segment(df):

    if df.empty:
        return empty_chart("Sales by Segment")


    data = (
        df.groupby("segment", as_index=False)
        ["sales"]
        .sum()
    )


    fig = px.bar(
        data,
        x="segment",
        y="sales",
        title="Sales by Segment"
    )


    return apply_layout(fig)



def region_sales(df):

    if df.empty:
        return empty_chart("Sales by Region")


    data = (
        df.groupby("region", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )


    fig = px.bar(
        data,
        x="region",
        y="sales",
        title="Sales by Region"
    )


    return apply_layout(fig)



def market_sales(df):

    if df.empty:
        return empty_chart("Sales by Market")


    data = (
        df.groupby("market", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )


    fig = px.bar(
        data,
        x="market",
        y="sales",
        title="Sales by Market"
    )


    return apply_layout(fig)



# ==========================
# TOP PERFORMANCE
# ==========================


def top_products(df, top_n=10):

    if df.empty:
        return empty_chart("Top Products")


    data = (
        df.groupby("product_name", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
        .head(top_n)
    )


    fig = px.bar(
        data,
        x="product_name",
        y="sales",
        title=f"Top {top_n} Products"
    )


    fig.update_layout(
        xaxis_tickangle=-35
    )


    return apply_layout(fig, 500)



def top_customers(df, top_n=10):

    if df.empty:
        return empty_chart("Top Customers")


    data = (
        df.groupby("customer_name", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
        .head(top_n)
    )


    fig = px.bar(
        data,
        x="customer_name",
        y="sales",
        title=f"Top {top_n} Customers"
    )


    fig.update_layout(
        xaxis_tickangle=-35
    )


    return apply_layout(fig, 500)



# ==========================
# PROFIT ANALYSIS
# ==========================


def profit_by_category(df):

    if df.empty:
        return empty_chart("Profit by Category")


    data = (
        df.groupby("category", as_index=False)
        ["profit"]
        .sum()
        .sort_values(
            "profit",
            ascending=False
        )
    )


    fig = px.bar(
        data,
        x="category",
        y="profit",
        title="Profit by Category"
    )


    return apply_layout(fig)



def discount_profit(df):

    if df.empty:
        return empty_chart("Discount vs Profit")


    fig = px.scatter(
        df,
        x="discount",
        y="profit",
        color="category",
        title="Discount vs Profit"
    )


    return apply_layout(fig, 500)



def profit_distribution(df):

    if df.empty:
        return empty_chart("Profit Distribution")


    fig = px.histogram(
        df,
        x="profit",
        nbins=40,
        title="Profit Distribution"
    )


    return apply_layout(fig)