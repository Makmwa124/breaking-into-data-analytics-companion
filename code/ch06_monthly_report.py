"""Chapter 6: automate a monthly store report. Change MONTH and rerun each month."""
import pandas as pd

MONTH = "2025-12"

sales = pd.read_csv("../data/bramblewood_sales.csv",
                    parse_dates=["order_date"]).drop_duplicates()
stores = pd.read_csv("../data/bramblewood_stores.csv")
sales["revenue"] = (sales["units"] * sales["unit_price"]
                    * (1 - sales["discount"]))
sales["month"] = sales["order_date"].dt.strftime("%Y-%m")

this_month = pd.Period(MONTH, freq="M")
last_year = (this_month - 12).strftime("%Y-%m")


def store_summary(month):
    t = sales[sales["month"] == month]
    return t.groupby("store_id").agg(orders=("order_id", "nunique"),
                                     revenue=("revenue", "sum"))


report = store_summary(MONTH).join(store_summary(last_year),
                                   rsuffix="_ly")
report = stores.set_index("store_id")[["store_name"]].join(report)
report["revenue_vs_ly_pct"] = (
    (report["revenue"] / report["revenue_ly"] - 1) * 100)
report = report.round({"revenue": 0, "revenue_ly": 0,
                       "revenue_vs_ly_pct": 1})
cols = ["store_name", "orders", "revenue", "revenue_ly",
        "revenue_vs_ly_pct"]
print(report[cols].to_string())

report.to_excel(f"store_report_{MONTH}.xlsx")
print(f"Saved store_report_{MONTH}.xlsx")
