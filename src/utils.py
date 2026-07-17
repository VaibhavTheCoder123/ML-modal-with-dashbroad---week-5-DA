import pandas as pd


def standardize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def convert_dates(df):
    for col in ["order_date", "ship_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def clean_missing(df):
    object_cols = df.select_dtypes(include="object").columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in object_cols:
        df[col] = df[col].fillna("Unknown")

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    return df


def remove_duplicates(df):
    return df.drop_duplicates()


def remove_invalid_rows(df):
    df = df[df["sales"] >= 0]
    df = df[df["quantity"] > 0]
    return df.reset_index(drop=True)