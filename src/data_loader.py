from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    BASE_DIR
    / "data"
    / "cleaned"
    / "global_superstore_features.csv"
)

MODEL_FILE = (
    BASE_DIR
    / "models"
    / "best_model.pkl"
)


@lru_cache(maxsize=1)
def load_data():

    df = pd.read_csv(DATA_FILE)

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    return df


@lru_cache(maxsize=1)
def load_model():
    return joblib.load(MODEL_FILE)