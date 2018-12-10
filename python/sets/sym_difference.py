"""Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem"""

# Number of students subscribed to English newspapers and their rolls
num_english = int(input())
english_rolls = set(map(int, input().split()))

# Number of students subscribed to French newspapers and their rolls
num_french = int(input())
french_rolls = set(map(int, input().split()))

# Find students subscribed to English newspaper only
either = english_rolls.symmetric_difference(french_rolls)

# Print number of students subscribed
print(len(either))
