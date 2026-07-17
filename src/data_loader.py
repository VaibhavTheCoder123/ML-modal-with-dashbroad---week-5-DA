from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from src.constants import FEATURE_DATA_FILE, MODEL_FILE


@st.cache_data(show_spinner=False)
def load_data():
    """
    Load the engineered dataset.

    Returns
    -------
    pandas.DataFrame
    """

    data_path = Path(FEATURE_DATA_FILE)

    if not data_path.exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{data_path}"
        )

    df = pd.read_csv(data_path)

    date_columns = [
        "order_date",
        "ship_date"
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df.copy()


@st.cache_resource(show_spinner=False)
def load_model():
    """
    Load trained machine learning model.

    Returns
    -------
    sklearn Pipeline
    """

    model_path = Path(MODEL_FILE)

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found:\n{model_path}"
        )

    return joblib.load(model_path)


def get_dataset_shape():
    """
    Return dataset shape.
    """

    df = load_data()

    return df.shape


def get_feature_columns():
    """
    Return feature column names.
    """

    df = load_data()

    return list(df.columns)


def reload_data():
    """
    Clear Streamlit cache and reload dataset.
    """

    load_data.clear()

    return load_data()


def reload_model():
    """
    Clear Streamlit cache and reload model.
    """

    load_model.clear()

    return load_model()


def validate_dataset(required_columns=None):
    """
    Validate dataset columns.

    Parameters
    ----------
    required_columns : list, optional

    Returns
    -------
    bool
    """

    df = load_data()

    if required_columns is None:
        return True

    missing = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            "Missing columns: "
            + ", ".join(missing)
        )

    return True


def dataset_summary():
    """
    Return dataset summary information.

    Returns
    -------
    dict
    """

    df = load_data()

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


if __name__ == "__main__":

    data = load_data()

    print("=" * 60)
    print("StoreScope Data Loader")
    print("=" * 60)
    print(f"Rows      : {len(data):,}")
    print(f"Columns   : {len(data.columns)}")
    print(f"Duplicates: {data.duplicated().sum()}")
    print(f"Missing   : {data.isna().sum().sum()}")
    print("=" * 60)