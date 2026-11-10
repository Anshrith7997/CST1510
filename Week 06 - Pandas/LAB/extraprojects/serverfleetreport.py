
import pandas as pd
import matplotlib.pyplot as plt

# This script checks server usage and identifies servers at risk.
# It also compares regions and saves a report of overloaded servers.

df = pd.read_csv("servers.csv")

print(df.head())
print(df.dtypes)
print("Number of servers:", len(df))
print("Number of columns:", len(df.columns))

df["percent"] = (df["used"] / df["total"]) * 100

print("Servers at or above 90%:")
print(len(df[df["percent"] >= 90]))

print("Average usage per region:")
print(df.groupby("region")["percent"].mean())

print("Server most at risk:")
print(df.sort_values("percent", ascending=False).head(1))

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 90
    else "WARNING" if x >= 75
    else "OK"
)

print(df[["region", "percent", "status"]])

df["region"].value_counts().plot(kind="bar")

plt.title("Servers per Region")
plt.xlabel("Region")
plt.ylabel("Number of Servers")
plt.tight_layout()
plt.savefig("servers_chart.png")
plt.show()

df[df["status"] == "OVER LIMIT"].to_csv(
    "servers_at_risk.csv", index=False
)
