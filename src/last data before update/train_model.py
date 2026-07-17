from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "cleaned" / "global_superstore_features.csv"
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

df = pd.read_csv(DATA_PATH)

features = [
    "sales",
    "quantity",
    "discount",
    "shipping_cost",
    "category",
    "sub_category",
    "segment",
    "market"
]

target = "profit"

X = df[features]
y = df[target]

categorical = [
    "category",
    "sub_category",
    "segment",
    "market"
]

numeric = [
    "sales",
    "quantity",
    "discount",
    "shipping_cost"
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
        n_estimators=50,
        random_state=42,
        n_jobs=-1,
        max_depth=20,
    ),
}

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

best_model = None
best_score = float("-inf")

for name, model in models.items():

    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(X_train, y_train)

    prediction = pipeline.predict(X_test)

    score = r2_score(y_test, prediction)

    print(f"{name}: {score:.4f}")

    if score > best_score:
        best_score = score
        best_model = pipeline

joblib.dump(best_model, MODEL_PATH)

print(f"\nBest Model: {best_score:.4f}")
print("Model saved successfully.")