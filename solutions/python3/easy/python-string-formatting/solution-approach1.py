# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-04, 07:31 p.m.
# ──────────────────────────────────────────────────

def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number+1):
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].rjust(width).upper(),
            bin(i)[2:].rjust(width)
        )
    
