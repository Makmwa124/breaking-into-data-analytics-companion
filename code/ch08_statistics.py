"""Chapter 8: the statistics you will actually use."""
import pandas as pd
from statsmodels.stats.proportion import (proportions_ztest,
                                          proportion_confint)

s = pd.read_csv("../data/bramblewood_sales.csv").drop_duplicates()
s["revenue"] = s.units * s.unit_price * (1 - s.discount)

# 8.1 Mean versus median
print(s["revenue"].describe(percentiles=[.25, .5, .75, .9]).round(2))

# 8.2 Two proportions: do members on a 12-month contract cancel less?
m = pd.read_csv("../data/quokka_members.csv")
g = m.groupby("contract")["cancelled"].agg(["sum", "count", "mean"])
print(g.round(3))
stat, p = proportions_ztest(g["sum"], g["count"])
print(f"z = {stat:.2f}, p = {p:.2g}")
for name, row in g.iterrows():
    lo, hi = proportion_confint(row["sum"], row["count"], method="wilson")
    print(f"{name:12s} {row['mean']:.1%}  (95% CI {lo:.1%} to {hi:.1%})")

# 8.3 Correlation
print(round(m["visits_last_90d"].corr(m["tenure_months"]), 2))
