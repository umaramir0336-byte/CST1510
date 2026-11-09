"""
RECORD CHECK  -  my version
===========================

Name  : Muhammad Amir
Lane  :  AI / Data Science
Date  :  09/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    """Store and check one record."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialise a record with its label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage of the limit."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
def load_records(path):
    """Read records from a file and return Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = Record(label, float(value), float(limit))
            records.append(record)

    return records

records = load_records("records_sample.txt")


# ==================================================================== OUTPUT
over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Value      : {record.value}")
    print(f"  Limit      : {record.limit}")
    print(f"  Percentage : {(record.value / record.limit) * 100:.1f}%")
    
    result = record.status()
    print(f"  Status     : {result}")

    if result == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)

print()
print(f"OVER LIMIT records: {over_limit_count} of {len(records)}")
