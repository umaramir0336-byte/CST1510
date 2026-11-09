# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"

key, value = piece.split("=", maxsplit=1)

print(key, value)
