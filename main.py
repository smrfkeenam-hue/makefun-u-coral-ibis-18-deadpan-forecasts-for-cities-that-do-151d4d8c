# main.py — deadpan forecast for the city that does not exist.
# One line, 142 characters: forecast format first, joke second.
# Writes one text to /output/entry.txt, no trailing newline.
import os

# The concrete detail that makes Zorblax feel real: 41 degrees, 70%,
# sideways rain, one goat on the roof since Tuesday.
ENTRY = "Zorblax: high of 41 degrees, 70% chance of sideways rain, and one goat still stuck on the roof since Tuesday. Bring an umbrella. And a ladder."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
