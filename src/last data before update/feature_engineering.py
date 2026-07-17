from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "cleaned" / "global_superstore_clean.csv"
OUTPUT_PATH = BASE_DIR / "data" / "cleaned" / "global_superstore_features.csv"


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.month
    df["order_day"] = df["order_date"].dt.day
    df["order_weekday"] = df["order_date"].dt.day_name()
    df["order_quarter"] = df["order_date"].dt.quarter

    df["shipping_days"] = (
        df["ship_date"] - df["order_date"]
    ).dt.days

    df["profit_margin"] = (
        df["profit"] / df["sales"].replace(0, 1)
    )

    df["sales_per_quantity"] = (
        df["sales"] / df["quantity"]
    )

    df["high_profit"] = (
        df["profit"] > df["profit"].median()
    ).astype(int)

    return df


def main():
    df = pd.read_csv(DATA_PATH, parse_dates=["order_date", "ship_date"])

    df = create_features(df)

    df.to_csv(OUTPUT_PATH, index=False)

    print("Feature engineering completed.")
    print(f"Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()