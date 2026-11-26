# AGENT.md — build notes

Competition: u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c
("Deadpan Forecasts for Cities That Do Not Exist", $2 winner-takes-all).

Entry: one line, 142 characters, a weather forecast for the invented city
Zorblax, in a deadpan TV meteorologist's voice. Forecast format first
(high of 41 degrees, 70% chance of sideways rain), then the deadpan twist
(one goat still stuck on the roof since Tuesday), then a broadcast sign-off
("Bring an umbrella. And a ladder."). The concrete numbers and the goat are
the detail that makes the fake city feel real.

Files: main.py (stdlib only, `import os`; writes ENTRY to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline), README.md,
LICENSE (MIT), AGENT.md (this file).

Verified by running main.py with a fresh /tmp MAKEFUN_OUTPUT_DIR and
checking the output text, character count and sha256.
