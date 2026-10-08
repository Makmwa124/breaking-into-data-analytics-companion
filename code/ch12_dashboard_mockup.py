"""Chapter 12: draw the one-page layout of the Riverbend dashboard (a wireframe with real numbers)."""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

a = pd.read_csv("../data/riverbend_appointments.csv",
                parse_dates=["appt_date"])
fig = plt.figure(figsize=(8, 5))
fig.suptitle("Riverbend Community Health: access and attendance, 2025", x=0.02, ha="left", fontsize=12, weight="bold")
kpis = [("Appointments", f"{len(a):,}"), ("No-show rate", f"{a.no_show.mean():.1%}"),
        ("Median wait", f"{a.wait_days.median():.0f} days"), ("Waits > 14 days", f"{(a.wait_days > 14).mean():.1%}")]
for i, (label, val) in enumerate(kpis):
    ax = fig.add_axes([0.02 + i * 0.245, 0.72, 0.225, 0.14]); ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.06, 0.62, val, fontsize=15, weight="bold", transform=ax.transAxes)
    ax.text(0.06, 0.2, label, fontsize=9, color="0.3", transform=ax.transAxes)
m = a.set_index("appt_date").resample("MS")["no_show"].mean() * 100
ax1 = fig.add_axes([0.06, 0.1, 0.42, 0.5])
ax1.plot(m.index.strftime("%b"), m.values, color="black", marker="o", ms=3)
ax1.set_title("No-show rate by month (%)", loc="left", fontsize=9); ax1.set_ylim(0, 12)
ax1.tick_params(labelsize=7); ax1.spines[["top", "right"]].set_visible(False)
a["wait_band"] = pd.cut(a.wait_days, [-1, 7, 14, 28, 365], labels=["0-7", "8-14", "15-28", "29+"])
wb = a.groupby("wait_band", observed=True)["no_show"].mean() * 100
ax2 = fig.add_axes([0.57, 0.1, 0.4, 0.5])
b = ax2.barh(wb.index.astype(str), wb.values, color="0.4"); ax2.bar_label(b, fmt="%.1f%%", fontsize=7, padding=3)
ax2.set_title("No-show rate by wait (days)", loc="left", fontsize=9); ax2.invert_yaxis()
ax2.set_xticks([]); ax2.tick_params(labelsize=8); ax2.spines[["top", "right", "bottom"]].set_visible(False)
fig.savefig("riverbend_dashboard_mockup.png", dpi=200)
print(m.round(1).to_string())
