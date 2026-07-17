import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from config import MODEL_DIR, CLEAN_DIR

DATA = CLEAN_DIR / "global_superstore_features.csv"

df = pd.read_csv(DATA)

target = "profit"

features = [
    "sales",
    "quantity",
    "discount",
    "shipping_cost",
    "shipping_days",
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
    "shipping_days",
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
    "Decision Tree": DecisionTreeRegressor(
        random_state=42,
        max_depth=15,
    ),
    "Random Forest": RandomForestRegressor(
        random_state=42,
        n_estimators=100,
        max_depth=20,
        n_jobs=-1,
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42,
    ),
    "Extra Trees": ExtraTreesRegressor(
        random_state=42,
        n_estimators=100,
        n_jobs=-1,
    ),
}

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2,
)

results = []

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

    results.append([name, score])

    print(f"{name:<20} {score:.4f}")

    if score > best_score:
        best_score = score
        best_model = pipeline

results = pd.DataFrame(
    results,
    columns=["Model", "R2 Score"],
)

print("\n")
print(results.sort_values("R2 Score", ascending=False))

joblib.dump(
    best_model,
    MODEL_DIR / "best_model.pkl",
)

print("\nBest Model Saved")