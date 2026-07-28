-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
-- Problem     Revising the Select Query I
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-07-28, 12:03 p.m.
-- ──────────────────────────────────────────────────

SELECT *
FROM CITY
WHERE CountryCode = 'USA'
  AND Population > 100000;
