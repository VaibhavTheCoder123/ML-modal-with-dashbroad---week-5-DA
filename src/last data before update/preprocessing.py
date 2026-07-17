import pandas as pd

from config import CLEAN_DATA
from logger import logger
from src.data_loader import load_data


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

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["ship_date"] = pd.to_datetime(df["ship_date"])

    return df


def clean_missing(df):

    object_columns = df.select_dtypes(include="object").columns

    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

    for col in object_columns:

        df[col] = df[col].fillna("Unknown")

    for col in numeric_columns:

        df[col] = df[col].fillna(df[col].median())

    return df


def remove_duplicates(df):

    return df.drop_duplicates()


def preprocess():

    df = load_data()

    df = standardize_columns(df)

    df = convert_dates(df)

    df = clean_missing(df)

    df = remove_duplicates()

    df.to_csv(CLEAN_DATA, index=False)

    logger.info("Clean dataset saved")

    print(df.head())

    print(df.info())


if __name__ == "__main__":

    preprocess()