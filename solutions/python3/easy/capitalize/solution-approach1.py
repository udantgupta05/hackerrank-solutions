# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Problem     Capitalize!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-05, 08:09 p.m.
# ──────────────────────────────────────────────────



# Complete the solve function below.
def solve(s):
    for name in s.split():
        s = s.replace(name, name.capitalize())
    return s

