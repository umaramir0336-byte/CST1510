
"""
RECORD CHECK - AI / Data Science

Name  : Muhammad Amir
Lane  : AI / Data Science
Date  : 09/11/2026

Run it: python template.py
"""

# ==================================================================== INPUT
# 1. Ask for the three values

label = input("Dataset name: ")
value = float(input("Rows loaded: "))
limit = float(input("Rows expected: "))


# ================================================================== PROCESS
# 2. Calculate difference and percentage

difference = limit - value
percent = (value / limit) * 100

# 3. Decide status

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Loaded      : {value:>10.2f}")
print(f"  Expected    : {limit:>10.2f}")
print(f"  Missing     : {difference:>10.2f}")
print(f"  Percent     : {percent:>10.2f} %")
print(f"  Status      : {status:>10}")

print("=" * 34)
