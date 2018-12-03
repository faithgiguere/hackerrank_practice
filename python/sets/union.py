"""Problem: https://www.hackerrank.com/challenges/py-set-union/problem"""

# Number of students subscribed to English newspaper
english = int(input())
# English student roll numbers
e_rolls = set(input().split())
# Number of students subscribed to French newspaper
french = int(input())
# French student roll numbers
f_rolls = set(input().split())

# Print number of unique students enrolled
print(len(f_rolls.union(e_rolls)))
