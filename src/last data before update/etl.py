from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "Global_Superstore2.csv"
CLEAN_DATA_DIR = BASE_DIR / "data" / "cleaned"
CLEAN_DATA_PATH = CLEAN_DATA_DIR / "global_superstore_clean.csv"


def extract_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="latin1")


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def convert_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    date_columns = ["order_date", "ship_date"]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    return df


def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    if "postal_code" in df.columns:
        df["postal_code"] = df["postal_code"].fillna(0).astype(int)

    object_columns = df.select_dtypes(include="object").columns

    for column in object_columns:
        df[column] = df[column].fillna("Unknown")

    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    return df


def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["sales"] >= 0]
    df = df[df["quantity"] > 0]
    return df.reset_index(drop=True)


def save_clean_data(df: pd.DataFrame, path: Path) -> None:
    CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def data_summary(df: pd.DataFrame) -> None:
    print("\nDataset Shape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nSummary Statistics")
    print(df.describe(include="all"))

    print("\nMemory Usage (MB)")
    print(round(df.memory_usage(deep=True).sum() / 1024 ** 2, 2))


def run_etl() -> None:
    df = extract_data(RAW_DATA_PATH)

    data_summary(df)

    df = standardize_column_names(df)

    df = convert_date_columns(df)

    df = clean_missing_values(df)

    df = remove_invalid_rows(df)

    save_clean_data(df, CLEAN_DATA_PATH)

    print("\nETL pipeline completed successfully.")
    print(f"Clean dataset saved to:\n{CLEAN_DATA_PATH}")


if __name__ == "__main__":
    run_etl()