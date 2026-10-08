"""Chapter 12: Project 3, Riverbend Community Health operations dashboard.
These are the numbers your Power BI cards and visuals should show (see ch12_dax_measures.dax)."""
import pandas as pd

a = pd.read_csv("../data/riverbend_appointments.csv",
                parse_dates=["appt_date"])

# 12.1 Headline KPIs for 2025
print(f"Appointments        {len(a):,}")
print(f"No-show rate        {a['no_show'].mean():.1%}")
print(f"Median wait days    {a['wait_days'].median():.0f}")
print(f"Waits over 14 days  {(a['wait_days'] > 14).mean():.1%}")

# 12.2 By service
svc = a.groupby("service").agg(appointments=("appointment_id", "count"),
                               no_show_pct=("no_show", "mean"),
                               median_wait=("wait_days", "median"))
svc["no_show_pct"] = (svc["no_show_pct"] * 100).round(1)
print(svc.sort_values("appointments", ascending=False))

# 12.3 Does a long wait predict a no-show?
a["wait_band"] = pd.cut(a["wait_days"], bins=[-1, 7, 14, 28, 365],
                        labels=["0-7", "8-14", "15-28", "29+"])
wb = (a.groupby("wait_band", observed=True)["no_show"]
        .agg(["count", "mean"]))
wb["mean"] = (wb["mean"] * 100).round(1)
print(wb.rename(columns={"count": "appointments", "mean": "no_show_pct"}))

# 12.4 Median wait by clinic and service
print(a.pivot_table(index="clinic", columns="service",
                    values="wait_days", aggfunc="median"))
