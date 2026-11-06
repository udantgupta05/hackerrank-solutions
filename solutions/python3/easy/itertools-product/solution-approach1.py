# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-06, 06:01 p.m.
# ──────────────────────────────────────────────────

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in list(product(a,b)):
    print(i, end = ' ')
