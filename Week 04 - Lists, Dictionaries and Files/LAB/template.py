"""
RECORD CHECK  -  my version
===========================

Name  :  Muhammad Amir
Lane  :  AI / Data Science
Date  : 09/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Calculate difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the record check report."""
    print("Record:", label)
    print("Value:", value)
    print("Limit:", limit)
    print("Difference:", difference)
    print("Percentage:", round(percent, 2), "%")
    print("Status:", status)
    print("-" * 30)

# ====================================================================== STORE
records = [
    {"label": "survey_2026", "value": 1187, "limit": 1200},
    {"label": "survey_2025", "value": 950, "limit": 1000},
    {"label": "survey_2024", "value": 1250, "limit": 1200}
]

# =============================================================== PROCESS + OUTPUT
for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )
