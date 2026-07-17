import pandas as pd

from config import CLEAN_FILE

OUTPUT_FILE = CLEAN_FILE.parent / "global_superstore_features.csv"


def create_features(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.month
    df["order_day"] = df["order_date"].dt.day
    df["order_quarter"] = df["order_date"].dt.quarter
    df["order_weekday"] = df["order_date"].dt.day_name()

    df["shipping_days"] = (
        df["ship_date"] - df["order_date"]
    ).dt.days

    df["profit_margin"] = (
        df["profit"] / df["sales"].replace(0, 1)
    )

    df["sales_per_quantity"] = (
        df["sales"] / df["quantity"]
    )

    return df


def main():

    df = pd.read_csv(
        CLEAN_FILE,
        parse_dates=["order_date", "ship_date"]
    )

    df = create_features(df)

    df.to_csv(OUTPUT_FILE, index=False)

    print("Feature Engineering Completed")
    print(df.head())


if __name__ == "__main__":
    main()