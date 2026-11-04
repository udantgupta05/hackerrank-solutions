# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Problem     Designer Door Mat
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-04, 07:04 p.m.
# ──────────────────────────────────────────────────

N, M = map(int, input().split())

for i in range(1,N,2):
    print(('.|.'*i).center(M, '-'))
    
print(('WELCOME').center(M, '-'))
    
for i in range(N-2,0,-2):
    print(('.|.'*i).center(M, '-'))
