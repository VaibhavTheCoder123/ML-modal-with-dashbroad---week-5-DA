from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "cleaned" / "global_superstore_features.csv"

MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

OUTPUT_DIR = BASE_DIR / "outputs" / "plots"

OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

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

target = "profit"

X = df[features]
y = df[target]

_, X_test, _, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = joblib.load(MODEL_PATH)

pred = model.predict(X_test)

print("MAE :", mean_absolute_error(y_test, pred))
print("RMSE :", mean_squared_error(y_test, pred) ** 0.5)
print("R² :", r2_score(y_test, pred))

plt.figure(figsize=(6,6))
plt.scatter(y_test, pred, alpha=0.4)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted Profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "actual_vs_predicted.png", dpi=300)
plt.close()