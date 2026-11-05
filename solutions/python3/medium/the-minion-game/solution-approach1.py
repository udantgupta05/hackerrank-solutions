# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Problem     The Minion Game
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-05, 08:32 p.m.
# ──────────────────────────────────────────────────

def minion_game(string):
    vowels = 'AEIOU'
    kevin = stuart = 0
    length = len(string)
    list(range(length))
    
    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        
        else:
            stuart += length -i
            
    if kevin > stuart:
        print(f'Kevin {kevin}')
    
    elif kevin < stuart:
        print(f'Stuart {stuart}')
        
    else:
        print('Draw')
    
    
    
    

