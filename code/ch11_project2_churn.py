"""Chapter 11: Project 2, Quokka Fitness membership churn."""
import pandas as pd

m = pd.read_csv("../data/quokka_members.csv", parse_dates=["join_date"])

# 11.1 First look
print(m.shape)
print(f"Overall cancellation rate: {m['cancelled'].mean():.1%}")

# 11.2 Rate by one feature at a time
def rate_by(col):
    t = m.groupby(col)["cancelled"].agg(members="count",
                                        cancel_rate="mean")
    t["cancel_rate"] = (t["cancel_rate"] * 100).round(1)
    return t.sort_values("cancel_rate", ascending=False)

for col in ["plan", "contract", "attends_classes", "age_band"]:
    print(rate_by(col), "\n")

# 11.3 Visits in the last 90 days, banded
m["visit_band"] = pd.cut(m["visits_last_90d"],
                         bins=[-1, 5, 10, 15, 20, 100],
                         labels=["0-5", "6-10", "11-15", "16-20", "21+"])
print(rate_by("visit_band").sort_index(), "\n")

# 11.4 The risk table: contract x visit band
risk = m.pivot_table(index="visit_band", columns="contract",
                     values="cancelled", aggfunc="mean", observed=True)
print((risk * 100).round(0))
# always check the counts
print(pd.crosstab(m["visit_band"], m["contract"]))

# 11.5 Who to call first: no contract, 10 or fewer visits
target = m[(m["contract"] == "No contract")
           & (m["visits_last_90d"] <= 10)
           & (m["cancelled"] == 0)]
print(len(target), "active members in the high-risk group")
print(f"Monthly fees at stake: ${target['monthly_fee'].sum():,}")

# 11.6 The one chart for the write-up
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rates = m.groupby("visit_band", observed=True)["cancelled"].mean() * 100
fig, ax = plt.subplots(figsize=(7, 3))
bars = ax.bar(rates.index.astype(str), rates.values, color="0.35")
ax.bar_label(bars, fmt="%.0f%%", padding=2)
ax.set_title("Cancellation rate by gym visits in the last 90 days", loc="left")
ax.set_xlabel("Visits in last 90 days")
ax.set_ylim(0, rates.max() * 1.15)
ax.set_yticks([])
ax.spines[["top", "right", "left"]].set_visible(False)
fig.tight_layout()
fig.savefig("churn_by_visits.png", dpi=200)
