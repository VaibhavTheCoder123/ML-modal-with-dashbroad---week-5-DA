import pandas as pd



# ==========================
# KPI FUNCTIONS
# ==========================

def get_kpis(df):

    """
    Return dashboard KPI values.
    """

    if df.empty:

        return {
            "total_sales": 0,
            "total_profit": 0,
            "total_orders": 0,
            "total_customers": 0,
            "total_products": 0,
            "average_discount": 0,
            "average_shipping_days": 0,
            "profit_margin": 0
        }


    total_sales = df["sales"].sum()

    total_profit = df["profit"].sum()


    return {

        "total_sales": total_sales,

        "total_profit": total_profit,

        "total_orders":
            df["order_id"].nunique(),

        "total_customers":
            df["customer_id"].nunique(),

        "total_products":
            df["product_name"].nunique(),

        "average_discount":
            df["discount"].mean()
            if "discount" in df.columns
            else 0,

        "average_shipping_days":
            df["shipping_days"].mean()
            if "shipping_days" in df.columns
            else 0,

        "profit_margin":
            (total_profit / total_sales) * 100
            if total_sales != 0
            else 0
    }



# ==========================
# SALES ANALYSIS
# ==========================

def sales_by_year(df):

    return (
        df.groupby("order_year", as_index=False)
        ["sales"]
        .sum()
        .sort_values("order_year")
    )



def sales_by_month(df):

    return (
        df.groupby("order_month", as_index=False)
        ["sales"]
        .sum()
        .sort_values("order_month")
    )



def sales_by_category(df):

    return (
        df.groupby("category", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )



def sales_by_subcategory(df):

    return (
        df.groupby("sub_category", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )



def sales_by_segment(df):

    return (
        df.groupby("segment", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )



def sales_by_market(df):

    return (
        df.groupby("market", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )



def sales_by_region(df):

    return (
        df.groupby("region", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )



# ==========================
# PROFIT ANALYSIS
# ==========================


def profit_by_category(df):

    return (
        df.groupby("category", as_index=False)
        ["profit"]
        .sum()
        .sort_values(
            "profit",
            ascending=False
        )
    )



def monthly_profit(df):

    return (
        df.groupby("order_month", as_index=False)
        ["profit"]
        .sum()
        .sort_values("order_month")
    )



def yearly_profit(df):

    return (
        df.groupby("order_year", as_index=False)
        ["profit"]
        .sum()
        .sort_values("order_year")
    )



# ==========================
# TOP PERFORMANCE
# ==========================


def top_products(df, n=10):

    return (
        df.groupby("product_name", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
        .head(n)
    )



def top_customers(df, n=10):

    return (
        df.groupby("customer_name", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
        .head(n)
    )



def top_countries(df, n=10):

    return (
        df.groupby("country", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
        .head(n)
    )



# ==========================
# SHIPPING
# ==========================


def shipping_analysis(df):

    if "shipping_days" not in df.columns:

        return pd.DataFrame()


    return (
        df.groupby("ship_mode", as_index=False)
        ["shipping_days"]
        .mean()
        .sort_values(
            "shipping_days"
        )
    )



# ==========================
# CUSTOMER ANALYSIS
# ==========================


def customer_segments(df):

    return (

        df.groupby("segment")
        .agg(

            Customers=(
                "customer_id",
                "nunique"
            ),

            Sales=(
                "sales",
                "sum"
            ),

            Profit=(
                "profit",
                "sum"
            )
        )

        .reset_index()

    )



# ==========================
# SUMMARY
# ==========================


def executive_summary(df):

    kpi = get_kpis(df)


    return {

        "Sales":
            kpi["total_sales"],

        "Profit":
            kpi["total_profit"],

        "Orders":
            kpi["total_orders"],

        "Customers":
            kpi["total_customers"],

        "Products":
            kpi["total_products"],

        "Profit Margin":
            kpi["profit_margin"]

    }



# ==========================
# DATASET INFO
# ==========================


def dataset_overview(df):

    return {

        "Rows":
            len(df),

        "Columns":
            len(df.columns),

        "Missing Values":
            int(df.isna().sum().sum()),

        "Duplicate Rows":
            int(df.duplicated().sum())

    }



# ==========================
# FILTER SYSTEM
# ==========================


def filter_dataframe(
        df,
        years=None,
        markets=None,
        categories=None,
        segments=None
):

    filtered = df.copy()



    if years:

        filtered = filtered[
            filtered["order_year"]
            .isin(years)
        ]


    if markets:

        filtered = filtered[
            filtered["market"]
            .isin(markets)
        ]


    if categories:

        filtered = filtered[
            filtered["category"]
            .isin(categories)
        ]


    if segments:

        filtered = filtered[
            filtered["segment"]
            .isin(segments)
        ]


    return filtered



# ==========================
# LOCATION ANALYSIS
# ==========================


def state_sales(df):

    return (
        df.groupby("state", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )



def city_sales(df):

    return (
        df.groupby("city", as_index=False)
        ["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
    )