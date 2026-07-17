from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "cleaned" / "global_superstore_features.csv"

OUTPUT_DIR = BASE_DIR / "outputs" / "plots"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])


def save_plot(name):
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / name, dpi=300)
    plt.close()


sales = df.groupby("order_year")["sales"].sum()

plt.figure(figsize=(8,5))
sales.plot(marker="o")
plt.title("Yearly Sales")
plt.ylabel("Sales")
save_plot("yearly_sales.png")


profit = df.groupby("category")["profit"].sum()

plt.figure(figsize=(8,5))
profit.sort_values().plot(kind="bar")
plt.title("Profit by Category")
save_plot("profit_by_category.png")


top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .nlargest(10)
)

plt.figure(figsize=(12,5))
top_products.plot(kind="bar")
plt.title("Top Products")
save_plot("top_products.png")


country_sales = (
    df.groupby("country")["sales"]
    .sum()
    .nlargest(10)
)

plt.figure(figsize=(10,5))
country_sales.plot(kind="bar")
plt.title("Top Countries")
save_plot("top_countries.png")


plt.figure(figsize=(7,5))
plt.scatter(df["discount"], df["profit"], alpha=0.3)
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Discount vs Profit")
save_plot("discount_profit.png")


print("EDA completed.")