
"""
RECORD CHECK - AI / Data Science

Name  : Muhammad Amir
Lane  : AI / Data Science
Date  : 09/11/2026

Run it: python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==================================================================== LOAD
# 1. Read your data file from the same folder as this Python file

file_path = Path(__file__).parent / "records.csv"

df = pd.read_csv(file_path)


# ================================================================= PROCESS
# 2. Add percent column

df["percent"] = (df["value"] / df["limit"]) * 100

# Add status column using apply() and lambda

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100
    else "WARNING" if x >= 90
    else "OK"
)


# ================================================================== OUTPUT
# 3. Print the DataFrame

print("\nFULL RECORD CHECK")
print(df)

# Filter records that are not OK

print("\nRECORDS NEEDING ATTENTION")
print(df[df["status"] != "OK"])

# Group by status and count

print("\nSTATUS COUNTS")
print(df.groupby("status").size())

# Save full DataFrame to CSV in the LAB folder

output_csv = Path(__file__).parent / "record_check_output.csv"
df.to_csv(output_csv, index=False)

print("\nCSV saved:", output_csv)

# Create bar chart of counts per status

df["status"].value_counts().plot(
    kind="bar",
    title="Record Status Counts"
)

plt.xlabel("Status")
plt.ylabel("Number of Records")
plt.tight_layout()

# Save chart in the LAB folder

output_chart = Path(__file__).parent / "record_status_chart.png"
plt.savefig(output_chart)

print("Chart saved:", output_chart)

plt.show()
