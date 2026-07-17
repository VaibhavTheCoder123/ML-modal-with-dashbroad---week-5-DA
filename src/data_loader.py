from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from src.config import FEATURE_DATA_FILE, MODEL_FILE

# ==========================
# LOAD DATASET
# ==========================

@st.cache_data(show_spinner=False)
def load_data():

    """
    Load Global Superstore dataset.

    Returns
    -------
    pandas.DataFrame
    """

    data_path = Path(FEATURE_DATA_FILE)


    if not data_path.exists():

        raise FileNotFoundError(
            f"""
            Dataset not found.

            Expected location:
            {data_path}

            Check FEATURE_DATA_FILE inside constants.py
            """
        )


    df = pd.read_csv(
        data_path,
        encoding="utf-8"
    )


    # Convert date columns

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


    return df



# ==========================
# LOAD MACHINE LEARNING MODEL
# ==========================

@st.cache_resource(show_spinner=False)
def load_model():

    """
    Load trained ML model.

    Returns
    -------
    sklearn model
    """


    model_path = Path(MODEL_FILE)


    if not model_path.exists():

        raise FileNotFoundError(
            f"""
            Model file not found.

            Expected location:
            {model_path}

            Train the model first.
            """
        )


    model = joblib.load(model_path)


    return model



# ==========================
# DATASET INFORMATION
# ==========================

def get_dataset_shape():

    """
    Return dataset rows and columns.
    """

    df = load_data()

    return df.shape



def get_feature_columns():

    """
    Return dataset columns.
    """

    df = load_data()

    return list(df.columns)



def dataset_summary():

    """
    Return dataset summary.
    """

    df = load_data()


    return {

        "Rows": len(df),

        "Columns": len(df.columns),

        "Missing Values": int(
            df.isna().sum().sum()
        ),

        "Duplicate Rows": int(
            df.duplicated().sum()
        )
    }



# ==========================
# VALIDATION
# ==========================

def validate_dataset(required_columns=None):

    """
    Check required columns exist.
    """


    df = load_data()


    if required_columns is None:

        return True



    missing_columns = [

        col
        for col in required_columns
        if col not in df.columns

    ]


    if missing_columns:

        raise ValueError(

            "Missing required columns: "
            +
            ", ".join(missing_columns)

        )


    return True



# ==========================
# CACHE CONTROL
# ==========================

def reload_data():

    """
    Clear dataset cache.
    """

    load_data.clear()

    return load_data()



def reload_model():

    """
    Clear model cache.
    """

    load_model.clear()

    return load_model()



# ==========================
# TESTING
# ==========================

if __name__ == "__main__":


    df = load_data()


    print("=" * 60)

    print("Global Superstore Data Loader")

    print("=" * 60)

    print(
        f"Rows      : {len(df):,}"
    )

    print(
        f"Columns   : {len(df.columns)}"
    )

    print(
        f"Missing   : {df.isna().sum().sum()}"
    )

    print(
        f"Duplicate : {df.duplicated().sum()}"
    )

    print("=" * 60)