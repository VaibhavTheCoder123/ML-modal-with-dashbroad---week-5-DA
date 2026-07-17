from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "cleaned" / "global_superstore_features.csv"

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

target = "profit"

features = [
    "sales",
    "quantity",
    "discount",
    "shipping_cost",
    "category",
    "sub_category",
    "segment",
    "market",
    "ship_mode",
]

X = df[features]
y = df[target]

categorical = [
    "category",
    "sub_category",
    "segment",
    "market",
    "ship_mode",
]

numeric = [
    "sales",
    "quantity",
    "discount",
    "shipping_cost",
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical,
        ),
        (
            "num",
            "passthrough",
            numeric,
        ),
    ]
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        random_state=42,
        n_estimators=150,
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42,
    ),
}

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

best_score = -999
best_model = None

for name, model in models.items():

    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(X_train, y_train)

    pred = pipeline.predict(X_test)

    score = r2_score(y_test, pred)

    print(f"{name}: {score:.4f}")

    if score > best_score:
        best_score = score
        best_model = pipeline

joblib.dump(best_model, MODEL_DIR / "best_model.pkl")

print("\nBest Model Saved")