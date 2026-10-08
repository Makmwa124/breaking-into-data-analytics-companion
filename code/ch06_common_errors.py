"""Chapter 6: three errors you will meet in your first week of pandas, and what they mean."""
import pandas as pd

sales = pd.read_csv("../data/bramblewood_sales.csv")

# 6.5 KeyError: a column name that does not exist (here, a capital letter)
try:
    sales["Revenue"]
except KeyError as e:
    print("KeyError:", e)

# 6.6 Dates read as text: comparisons work only by accident
print(sales["order_date"].dtype)
try:
    sales["order_date"].dt.year
except AttributeError as e:
    print("AttributeError:", e)

# 6.7 SettingWithCopyWarning-style trap avoided with .copy()
outdoor = sales[sales["product_id"].str.startswith("P4")].copy()
outdoor["revenue"] = (outdoor["units"] * outdoor["unit_price"]
                      * (1 - outdoor["discount"]))
print(len(outdoor), "Outdoor lines (raw file, before de-duplicating)")
