# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Problem     Text Wrap
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-04, 06:42 p.m.
# ──────────────────────────────────────────────────



def wrap(string, max_width):
    answer = textwrap.fill(string, max_width)
    return answer

