import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split

from config import (
    MODEL_DIR,
    CLEAN_DIR,
    PLOT_DIR,
)

DATA = CLEAN_DIR / "global_superstore_features.csv"

df = pd.read_csv(DATA)

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

target = "profit"

X = df[features]
y = df[target]

_, X_test, _, y_test = train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2,
)

model = joblib.load(
    MODEL_DIR / "best_model.pkl"
)

prediction = model.predict(X_test)

print("R2 :", r2_score(y_test, prediction))
print("MAE:", mean_absolute_error(y_test, prediction))
print("RMSE:", mean_squared_error(y_test, prediction) ** 0.5)

plt.figure(figsize=(7,7))
plt.scatter(
    y_test,
    prediction,
    alpha=0.3,
)

plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Actual vs Predicted")

plt.tight_layout()

plt.savefig(
    PLOT_DIR / "actual_vs_predicted.png",
    dpi=300,
)

plt.close()

residuals = y_test - prediction

plt.figure(figsize=(7,5))

plt.hist(
    residuals,
    bins=40,
)

plt.title("Residual Distribution")

plt.tight_layout()

plt.savefig(
    PLOT_DIR / "residual_distribution.png",
    dpi=300,
)

plt.close()

print("Evaluation Completed")