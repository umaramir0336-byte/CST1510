
"""
RECORD CHECK - AI / Data Science

Name  : Muhammad Amir
Lane  : AI / Data Science
Date  : 09/11/2026

Run it: python template.py
"""

# ==================================================================== INPUT
# 1. Ask the user for three values.

label = input("Dataset name: ")
first = float(input("Rows loaded: "))
second = float(input("Rows expected: "))


# ================================================================== PROCESS
# 2. Calculate the difference and percentage.

difference = second - first
percent = (first / second) * 100


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Loaded      : {first:>10.2f}")
print(f"  Expected    : {second:>10.2f}")
print(f"  Missing     : {difference:>10.2f}")
print(f"  Percent     : {percent:>10.2f} %")

print("=" * 34)
