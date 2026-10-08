"""Chapter 7: the same numbers the DAX measures return, calculated in pandas so you can check your report.
Expected card values when the report is filtered to 2025."""
import pandas as pd

s = pd.read_csv("../data/bramblewood_sales.csv",
                parse_dates=["order_date"]).drop_duplicates()
p = pd.read_csv("../data/bramblewood_products.csv")
s = s.merge(p, on="product_id")
s["line_revenue"] = s.units * s.unit_price * (1 - s.discount)
s["line_cost"] = s.units * s.unit_cost
y = s.order_date.dt.year
rev25, rev24 = s.line_revenue[y == 2025].sum(), s.line_revenue[y == 2024].sum()
cost25 = s.line_cost[y == 2025].sum()
orders25 = s.order_id[y == 2025].nunique()
print(f"Total Revenue        {rev25:,.0f}")
print(f"Revenue LY           {rev24:,.0f}")
print(f"Revenue YoY %        {(rev25 - rev24) / rev24:.1%}")
print(f"Gross Margin %       {(rev25 - cost25) / rev25:.1%}")
print(f"Orders               {orders25:,}")
print(f"Average Order Value  {rev25 / orders25:,.2f}")
