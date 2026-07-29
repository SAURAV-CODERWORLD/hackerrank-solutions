# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Problem     Finding the percentage
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-30, 01:49 a.m.
# ──────────────────────────────────────────────────

# Number of students
n = int(input())

# Empty dictionary
students = {}

# Take details of each student
for i in range(n):

    # Read the entire line
    data = input().split()

    # First value is the student's name
    name = data[0]

    # Remaining values are the marks
    marks = list(map(float, data[1:]))

    # Store in dictionary
    students[name] = marks

# Read the name of the student whose average is required
query = input()

# Check if student exists
if query in students:
    average = sum(students[query]) / len(students[query])
    print(f"{average:.2f}")
else:
    print("Student not found")
