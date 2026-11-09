
"""
RECORD CHECK - Week 6 version
================================
Run it with: python record_check.py

Week 1   input, calculate, print
Week 2   it can make decisions
Week 3   it is built from functions
Week 4   it reads many records from a file
Week 5   it becomes a reusable component
Week 6   it does the whole job in a few lines
"""

import pandas as pd
from pathlib import Path

# Read records.csv from the DEMO folder
file_path = Path(__file__).parent / "records.csv"

df = pd.read_csv(file_path)

# Calculate percentage
df["percent"] = (df["value"] / df["limit"]) * 100

# Calculate status using lambda
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

# Print the DataFrame
print(df)

# Filter over-limit records
over_limit = df[df["status"] == "OVER LIMIT"]

print(f"\nChecked {len(df)} records. {len(over_limit)} were over limit.")

# Display status counts
print("\nBy status:")
print(df["status"].value_counts())

# Save report.csv in the DEMO folder
output_path = Path(__file__).parent / "report.csv"

df.to_csv(output_path, index=False)

print("\nSaved report.csv")
