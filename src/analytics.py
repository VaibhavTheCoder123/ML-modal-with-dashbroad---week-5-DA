from formatter import currency


def get_kpis(df):

    return {

        "sales":df["sales"].sum(),

        "profit":df["profit"].sum(),

        "orders":df["order_id"].nunique(),

        "customers":df["customer_id"].nunique(),

        "avg_discount":df["discount"].mean(),

        "avg_shipping":df["shipping_days"].mean(),

        "margin":(
            df["profit"].sum()/df["sales"].sum()
        )*100

    }