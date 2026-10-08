"""Chapter 8: compare each month with the same month last year."""
import pandas as pd

s = pd.read_csv("../data/bramblewood_sales.csv",
                parse_dates=["order_date"]).drop_duplicates()
s["revenue"] = s.units * s.unit_price * (1 - s.discount)
t = s.pivot_table(index=s.order_date.dt.month,
                  columns=s.order_date.dt.year,
                  values="revenue", aggfunc="sum").round(0)
t.index.name = "month"
t["yoy_pct"] = ((t[2025] / t[2024] - 1) * 100).round(1)
print(t)
