# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.


from pathlib import Path

# Get the LAB directory from this Python file's location
lab_folder = Path(__file__).resolve().parent.parent
file_path = lab_folder / "records_sample.txt"

with open(file_path, "r") as f:
    print(f.read())

