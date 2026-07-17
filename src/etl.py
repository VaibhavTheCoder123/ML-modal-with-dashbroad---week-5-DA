from pathlib import Path

import pandas as pd

from config import RAW_FILE, CLEAN_FILE
from utils import (
    standardize_columns,
    convert_dates,
    clean_missing,
    remove_duplicates,
    remove_invalid_rows
)


def dataset_summary(df):
    print("\n==============================")
    print("DATASET SUMMARY")
    print("==============================")

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nData Types")
    print(df.dtypes)

    print("\nStatistics")
    print(df.describe(include="all"))


def run_etl():

    print("Loading Dataset...")

    df = pd.read_csv(RAW_FILE, encoding="latin1")

    dataset_summary(df)

    print("\nCleaning Dataset...")

    df = standardize_columns(df)

    df = convert_dates(df)

    df = clean_missing(df)

    df = remove_duplicates(df)

    df = remove_invalid_rows(df)

    print("\nSaving Clean Dataset...")

    df.to_csv(CLEAN_FILE, index=False)

    print("\nETL Completed Successfully")
    print(f"\nSaved At:\n{CLEAN_FILE}")


if __name__ == "__main__":
    run_etl()