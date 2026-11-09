"""
RECORD CHECK  -  my version
===========================

Name  :  Muhammad Amir
Lane  :  AI / Data Science
Date  :  09/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean and parse one raw record into a dictionary."""
    parts = raw_line.strip().split(",")

    record = {}

    record["label"] = parts[0].strip().lower()

    for piece in parts[1:]:
        key, value = piece.split("=", 1)
        key = key.strip().lower()
        value = value.strip()

        try:
            record[key] = float(value)
        except ValueError:
            record[key] = value.lower()

    return record


def status_of(record):
    """Return the status of a survey rating record."""
    rating = record.get("rating", 0)

    if rating >= 4:
        return "HIGH"
    elif rating >= 3:
        return "MEDIUM"
    else:
        return "LOW"


# ====================================================================== INPUT
raw_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "survey_2027, RATING=2, AGE=21",
    "  SURVEY_2028 , rating = 5 , age = 25 ",
    "Survey_2029, rating=3, age=22",
    " survey_2030 , RATING=1 , AGE=20 "
]


# =============================================================== PROCESS + OUTPUT
flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    print(record, status)

    if status == "HIGH":
        flagged_count += 1

print("\nSUMMARY")
print("Total records:", len(raw_records))
print("Flagged records:", flagged_count)
