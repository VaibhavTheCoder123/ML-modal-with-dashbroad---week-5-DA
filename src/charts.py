import plotly.express as px


# ==========================================================
# StoreScope Chart Theme
# ==========================================================

PRIMARY = "#1565C0"
SECONDARY = "#b92b27"

COLOR_SEQUENCE = [
    "#1565C0",
    "#2979FF",
    "#42A5F5",
    "#64B5F6",
    "#90CAF9",
    "#b92b27",
    "#C62828",
    "#D84315",
    "#EF5350",
    "#FF7043",
]

CHART_HEIGHT = 450


# ==========================================================
# Common Layout
# ==========================================================
def apply_layout(fig, height=450):

    fig.update_layout(

        template="plotly_dark",

        height=height,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(255,255,255,0.03)",

        font=dict(
            color="white",
            family="Poppins"
        ),

        title_font=dict(
            size=22,
            color="white"
        ),

        hovermode="x unified",

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    fig.update_xaxes(
        gridcolor="rgba(255,255,255,.08)"
    )

    fig.update_yaxes(
        gridcolor="rgba(255,255,255,.08)"
    )

    return fig

# ==========================================================
# Empty Chart
# ==========================================================

def empty_chart(title):

    fig = px.scatter(title=title)

    fig.update_layout(

        template="plotly_white",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white"),

        height=CHART_HEIGHT

    )

    return fig


# ==========================================================
# Yearly Sales
# ==========================================================

def yearly_sales(df):

    if df.empty:
        return empty_chart("Yearly Sales Trend")

    data = (
        df.groupby(
            "order_year",
            as_index=False
        )["sales"]
        .sum()
    )

    fig = px.line(

        data,

        x="order_year",

        y="sales",

        markers=True,

        title="Yearly Sales Trend",

        color_discrete_sequence=[PRIMARY]

    )

    fig.update_traces(

        line=dict(width=4),

        marker=dict(size=8)

    )

    return apply_layout(fig)


# ==========================================================
# Monthly Sales
# ==========================================================

def monthly_sales(df):

    if df.empty:
        return empty_chart("Monthly Sales")

    data = (
        df.groupby(
            "order_month",
            as_index=False
        )["sales"]
        .sum()
    )

    fig = px.bar(

        data,

        x="order_month",

        y="sales",

        title="Monthly Sales",

        color_discrete_sequence=[PRIMARY]

    )

    return apply_layout(fig)


# ==========================================================
# Sales by Category
# ==========================================================

def sales_by_category(df):

    if df.empty:
        return empty_chart("Sales by Category")

    data = (
        df.groupby(
            "category",
            as_index=False
        )["sales"]
        .sum()
    )

    fig = px.pie(

        data,

        names="category",

        values="sales",

        hole=.55,

        title="Sales by Category",

        color_discrete_sequence=COLOR_SEQUENCE

    )

    return apply_layout(fig)


# ==========================================================
# Sales by Segment
# ==========================================================

def sales_by_segment(df):

    if df.empty:
        return empty_chart("Sales by Segment")

    data = (
        df.groupby(
            "segment",
            as_index=False
        )["sales"]
        .sum()
    )

    fig = px.bar(

        data,

        x="segment",

        y="sales",

        title="Sales by Segment",

        color_discrete_sequence=[SECONDARY]

    )

    return apply_layout(fig)

# ==========================================================
# Region Sales
# ==========================================================

def region_sales(df):

    if df.empty:
        return empty_chart("Sales by Region")

    data = (
        df.groupby(
            "region",
            as_index=False
        )["sales"]
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

        title="Sales by Region",

        color="sales",

        color_continuous_scale=[
            PRIMARY,
            SECONDARY
        ]
    )

    fig.update_layout(
        coloraxis_showscale=False
    )

    return apply_layout(fig)


# ==========================================================
# Market Sales
# ==========================================================

def market_sales(df):

    if df.empty:
        return empty_chart("Sales by Market")

    data = (
        df.groupby(
            "market",
            as_index=False
        )["sales"]
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

        title="Sales by Market",

        color="sales",

        color_continuous_scale=[
            PRIMARY,
            SECONDARY
        ]
    )

    fig.update_layout(
        coloraxis_showscale=False
    )

    return apply_layout(fig)


# ==========================================================
# Top Products
# ==========================================================

def top_products(df, top_n=10):

    if df.empty:
        return empty_chart("Top Products")

    data = (
        df.groupby(
            "product_name",
            as_index=False
        )["sales"]
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

        title=f"Top {top_n} Products",

        color="sales",

        color_continuous_scale=[
            PRIMARY,
            SECONDARY
        ]
    )

    fig.update_layout(

        xaxis_tickangle=-35,

        coloraxis_showscale=False

    )

    return apply_layout(fig, 520)


# ==========================================================
# Top Customers
# ==========================================================

def top_customers(df, top_n=10):

    if df.empty:
        return empty_chart("Top Customers")

    data = (
        df.groupby(
            "customer_name",
            as_index=False
        )["sales"]
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

        title=f"Top {top_n} Customers",

        color="sales",

        color_continuous_scale=[
            PRIMARY,
            SECONDARY
        ]
    )

    fig.update_layout(

        xaxis_tickangle=-35,

        coloraxis_showscale=False

    )

    return apply_layout(fig, 520)


# ==========================================================
# Profit by Category
# ==========================================================

def profit_by_category(df):

    if df.empty:
        return empty_chart("Profit by Category")

    data = (
        df.groupby(
            "category",
            as_index=False
        )["profit"]
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

        title="Profit by Category",

        color="profit",

        color_continuous_scale=[
            PRIMARY,
            SECONDARY
        ]
    )

    fig.update_layout(
        coloraxis_showscale=False
    )

    return apply_layout(fig)


# ==========================================================
# Discount vs Profit
# ==========================================================

def discount_profit(df):

    if df.empty:
        return empty_chart("Discount vs Profit")

    fig = px.scatter(

        df,

        x="discount",

        y="profit",

        color="category",

        title="Discount vs Profit",

        color_discrete_sequence=COLOR_SEQUENCE,

        opacity=0.75

    )

    fig.update_traces(

        marker=dict(
            size=9,
            line=dict(
                width=1,
                color="white"
            )
        )

    )

    return apply_layout(fig, 520)


# ==========================================================
# Profit Distribution
# ==========================================================

def profit_distribution(df):

    if df.empty:
        return empty_chart("Profit Distribution")

    fig = px.histogram(

        df,

        x="profit",

        nbins=40,

        title="Profit Distribution",

        color_discrete_sequence=[PRIMARY]

    )

    return apply_layout(fig)


# ==========================================================
# Monthly Profit
# ==========================================================

def monthly_profit(df):

    if df.empty:
        return empty_chart("Monthly Profit")

    data = (
        df.groupby(
            "order_month",
            as_index=False
        )["profit"]
        .sum()
    )

    fig = px.line(

        data,

        x="order_month",

        y="profit",

        markers=True,

        title="Monthly Profit",

        color_discrete_sequence=[SECONDARY]

    )

    fig.update_traces(
        line=dict(width=4)
    )

    return apply_layout(fig)


# ==========================================================
# Yearly Profit
# ==========================================================

def yearly_profit(df):

    if df.empty:
        return empty_chart("Yearly Profit")

    data = (
        df.groupby(
            "order_year",
            as_index=False
        )["profit"]
        .sum()
    )

    fig = px.line(

        data,

        x="order_year",

        y="profit",

        markers=True,

        title="Yearly Profit",

        color_discrete_sequence=[SECONDARY]

    )

    fig.update_traces(
        line=dict(width=4)
    )

    return apply_layout(fig)