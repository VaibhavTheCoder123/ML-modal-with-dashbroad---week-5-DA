
import pandas as pd


def get_kpis(df):
    """
    Return dashboard KPI values.
    """

    total_sales = df["sales"].sum()
    total_profit = df["profit"].sum()

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": df["order_id"].nunique(),
        "total_customers": df["customer_id"].nunique(),
        "total_products": df["product_name"].nunique(),
        "average_discount": df["discount"].mean(),
        "average_shipping_days": df["shipping_days"].mean(),
        "profit_margin": (
            (total_profit / total_sales) * 100
            if total_sales != 0
            else 0
        )
    }


def sales_by_year(df):

    return (
        df.groupby("order_year", as_index=False)["sales"]
        .sum()
        .sort_values("order_year")
    )


def sales_by_month(df):

    return (
        df.groupby("order_month", as_index=False)["sales"]
        .sum()
        .sort_values("order_month")
    )


def sales_by_category(df):

    return (
        df.groupby("category", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )


def sales_by_subcategory(df):

    return (
        df.groupby("sub_category", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )


def sales_by_segment(df):

    return (
        df.groupby("segment", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )


def sales_by_market(df):

    return (
        df.groupby("market", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )


def sales_by_region(df):

    return (
        df.groupby("region", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )


def profit_by_category(df):

    return (
        df.groupby("category", as_index=False)["profit"]
        .sum()
        .sort_values("profit", ascending=False)
    )


def top_products(df, n=10):

    return (
        df.groupby("product_name", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(n)
    )


def top_customers(df, n=10):

    return (
        df.groupby("customer_name", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(n)
    )


def top_countries(df, n=10):

    return (
        df.groupby("country", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(n)
    )


def shipping_analysis(df):

    return (
        df.groupby("ship_mode", as_index=False)["shipping_days"]
        .mean()
        .sort_values("shipping_days")
    )


def discount_analysis(df):

    return (
        df.groupby("category", as_index=False)
        .agg(
            Average_Discount=("discount", "mean"),
            Average_Profit=("profit", "mean")
        )
    )


def customer_segments(df):

    return (
        df.groupby("segment", as_index=False)
        .agg(
            Customers=("customer_id", "nunique"),
            Sales=("sales", "sum"),
            Profit=("profit", "sum")
        )
    )


def executive_summary(df):

    kpi = get_kpis(df)

    return {
        "Sales": kpi["total_sales"],
        "Profit": kpi["total_profit"],
        "Orders": kpi["total_orders"],
        "Customers": kpi["total_customers"],
        "Products": kpi["total_products"],
        "Profit Margin": kpi["profit_margin"]
    }


def dataset_overview(df):

    return {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isna().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }


def filter_dataframe(
    df,
    years=None,
    markets=None,
    categories=None,
    segments=None
):
    """
    Apply dashboard filters.
    """

    filtered = df.copy()

    if years:
        filtered = filtered[
            filtered["order_year"].isin(years)
        ]

    if markets:
        filtered = filtered[
            filtered["market"].isin(markets)
        ]

    if categories:
        filtered = filtered[
            filtered["category"].isin(categories)
        ]

    if segments:
        filtered = filtered[
            filtered["segment"].isin(segments)
        ]

    return filtered


def monthly_profit(df):

    return (
        df.groupby("order_month", as_index=False)["profit"]
        .sum()
        .sort_values("order_month")
    )


def yearly_profit(df):

    return (
        df.groupby("order_year", as_index=False)["profit"]
        .sum()
        .sort_values("order_year")
    )


def state_sales(df):

    return (
        df.groupby("state", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )


def city_sales(df):

    return (
        df.groupby("city", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )