# analyze_retention.py
# Author: 23f3003580@ds.study.iitm.ac.in
# This script analyzes customer retention data for 2024
# and produces a trend visualization with benchmark comparison.

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("customer_retention_2024.csv")

# Compute average
average = df["RetentionRate"].mean()
print(f"Average Retention Rate (2024): {average:.2f}")

# Plot retention trend
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["RetentionRate"], marker="o", label="Retention Rate")
plt.axhline(y=85, color="red", linestyle="--", label="Target Benchmark (85)")
plt.title("Customer Retention Trend (2024)")
plt.xlabel("Month")
plt.ylabel("Retention Rate (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig("customer_retention_trend.png")
plt.show()
