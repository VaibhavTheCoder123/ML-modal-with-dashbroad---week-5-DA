from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from config import CLEAN_FILE, PLOT_DIR


df = pd.read_csv(CLEAN_FILE)

df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])


def save_plot(name):
    plt.tight_layout()
    plt.savefig(PLOT_DIR / name, dpi=300)
    plt.close()


print("Generating Visualizations...")


# 1 Sales Trend

sales = df.groupby(df["order_date"].dt.year)["sales"].sum()

plt.figure(figsize=(8,5))
sales.plot(marker="o")
plt.title("Yearly Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
save_plot("01_yearly_sales.png")


# 2 Monthly Sales

monthly = df.groupby(df["order_date"].dt.month)["sales"].sum()

plt.figure(figsize=(8,5))
monthly.plot(marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
save_plot("02_monthly_sales.png")


# 3 Quarterly Sales

quarter = df.groupby(df["order_date"].dt.quarter)["sales"].sum()

plt.figure(figsize=(8,5))
quarter.plot(kind="bar")
plt.title("Quarterly Sales")
save_plot("03_quarterly_sales.png")


# 4 Category Sales

cat = df.groupby("category")["sales"].sum().sort_values()

plt.figure(figsize=(8,5))
cat.plot(kind="bar")
plt.title("Sales by Category")
save_plot("04_category_sales.png")


# 5 Category Profit

cat = df.groupby("category")["profit"].sum().sort_values()

plt.figure(figsize=(8,5))
cat.plot(kind="bar")
plt.title("Profit by Category")
save_plot("05_category_profit.png")


# 6 Sub Category Sales

sub = df.groupby("sub_category")["sales"].sum().sort_values()

plt.figure(figsize=(12,6))
sub.plot(kind="bar")
plt.title("Sales by Sub Category")
save_plot("06_subcategory_sales.png")


# 7 Region Sales

region = df.groupby("region")["sales"].sum().sort_values()

plt.figure(figsize=(8,5))
region.plot(kind="bar")
plt.title("Sales by Region")
save_plot("07_region_sales.png")


# 8 Market Sales

market = df.groupby("market")["sales"].sum().sort_values()

plt.figure(figsize=(8,5))
market.plot(kind="bar")
plt.title("Sales by Market")
save_plot("08_market_sales.png")


# 9 Segment Sales

segment = df.groupby("segment")["sales"].sum()

plt.figure(figsize=(6,6))
segment.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales by Segment")
save_plot("09_segment_sales.png")


# 10 Ship Mode

ship = df.groupby("ship_mode")["sales"].sum()

plt.figure(figsize=(8,5))
ship.plot(kind="bar")
plt.title("Sales by Ship Mode")
save_plot("10_ship_mode.png")


# 11 Top Products

products = (
    df.groupby("product_name")["sales"]
    .sum()
    .nlargest(10)
)

plt.figure(figsize=(12,5))
products.plot(kind="bar")
plt.title("Top 10 Products")
save_plot("11_top_products.png")


# 12 Top Customers

customers = (
    df.groupby("customer_name")["sales"]
    .sum()
    .nlargest(10)
)

plt.figure(figsize=(12,5))
customers.plot(kind="bar")
plt.title("Top Customers")
save_plot("12_top_customers.png")


# 13 Top Countries

country = (
    df.groupby("country")["sales"]
    .sum()
    .nlargest(10)
)

plt.figure(figsize=(10,5))
country.plot(kind="bar")
plt.title("Top Countries")
save_plot("13_top_countries.png")


# 14 Top Cities

city = (
    df.groupby("city")["sales"]
    .sum()
    .nlargest(10)
)

plt.figure(figsize=(10,5))
city.plot(kind="bar")
plt.title("Top Cities")
save_plot("14_top_cities.png")


# 15 Profit Distribution

plt.figure(figsize=(8,5))
plt.hist(df["profit"], bins=50)
plt.title("Profit Distribution")
save_plot("15_profit_distribution.png")


# 16 Sales Distribution

plt.figure(figsize=(8,5))
plt.hist(df["sales"], bins=50)
plt.title("Sales Distribution")
save_plot("16_sales_distribution.png")


# 17 Discount vs Profit

plt.figure(figsize=(8,5))
plt.scatter(df["discount"], df["profit"], alpha=0.25)
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Discount vs Profit")
save_plot("17_discount_profit.png")


# 18 Shipping Time

days = (
    pd.to_datetime(df["ship_date"])
    - pd.to_datetime(df["order_date"])
).dt.days

plt.figure(figsize=(8,5))
plt.hist(days, bins=20)
plt.title("Shipping Days")
save_plot("18_shipping_days.png")


# 19 Correlation

corr = df[
    [
        "sales",
        "quantity",
        "discount",
        "profit",
        "shipping_cost"
    ]
].corr()

plt.figure(figsize=(7,6))
plt.imshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(j, i, round(corr.iloc[i, j], 2), ha="center")

plt.colorbar()

plt.title("Correlation Matrix")

save_plot("19_correlation.png")


# 20 Order Priority

priority = df.groupby("order_priority")["sales"].sum()

plt.figure(figsize=(8,5))
priority.plot(kind="bar")
plt.title("Order Priority")
save_plot("20_order_priority.png")


print("\n20 Visualizations Saved Successfully")