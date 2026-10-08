"""Chapter 6: Python for analysts. Run from the code folder: python ch06_python_basics.py"""
import pandas as pd

# 6.1 Load and inspect
sales = pd.read_csv("../data/bramblewood_sales.csv",
                    parse_dates=["order_date"])
products = pd.read_csv("../data/bramblewood_products.csv")
print(sales.shape)
print(sales.duplicated().sum(), "duplicate rows")

# 6.2 Clean and enrich
sales = sales.drop_duplicates()
sales = sales.merge(products, on="product_id", how="left")
sales["revenue"] = (sales["units"] * sales["unit_price"]
                    * (1 - sales["discount"]))
sales["year"] = sales["order_date"].dt.year
print(sales.shape)

# 6.3 Revenue by category and year
by_cat = sales.pivot_table(index="category", columns="year",
                           values="revenue", aggfunc="sum").round(0)
by_cat["growth_pct"] = ((by_cat[2025] / by_cat[2024] - 1) * 100).round(1)
print(by_cat.sort_values(2025, ascending=False))

# 6.4 A chart for the report
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

monthly = sales.set_index("order_date")["revenue"].resample("MS").sum()
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(monthly.index, monthly.values / 1000, color="black")
ax.set_title("Bramblewood online revenue by month ($000)", loc="left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("monthly_revenue.png", dpi=200)
print("Peak month:", monthly.idxmax().strftime("%b %Y"),
      round(monthly.max()))
