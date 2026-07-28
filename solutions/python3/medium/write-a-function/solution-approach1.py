# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-28, 11:39 a.m.
# ──────────────────────────────────────────────────

def is_leap(year):
    if year % 400 ==0:
        return True 
    elif year % 100 ==0:
        return False
    elif year % 4 ==0:
        return True
    else:
        return False

