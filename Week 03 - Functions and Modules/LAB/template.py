"""
RECORD CHECK - my version
=========================

Name  : Muhammad Amir
Lane  : AI / Data Science
Date  : 09/11/2026

Run it: python template.py
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the complete record check report."""
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


# ==================================================================== INPUT

over_count = 0

while True:

    label = input("\nDataset name (or quit): ")

    if label.lower() == "quit":
        break

    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    # ================================================================= PROCESS

    difference, percent = check(value, limit)
    status = status_of(percent)

    # ================================================================= OUTPUT

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_count += 1


# ================================================================= SUMMARY

print()
print("=" * 34)
print(f"  OVER LIMIT RECORDS: {over_count}")
print("=" * 34)
