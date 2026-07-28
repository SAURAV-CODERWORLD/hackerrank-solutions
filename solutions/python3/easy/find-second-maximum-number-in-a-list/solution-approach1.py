# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-28, 11:42 a.m.
# ──────────────────────────────────────────────────

n = int(input())
arr = list(map(int, input().split()))

highest = max(arr)

while highest in arr:
    arr.remove(highest)

print(max(arr))
