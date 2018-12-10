"""Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?h_r=next-challenge&h_v=zen"""

# Number of students subscribed to English newspapers and their rolls
num_english = int(input())
english_rolls = set(map(int, input().split()))

# Number of students subscribed to French newspapers and their rolls
num_french = int(input())
french_rolls = set(map(int, input().split()))

# Find students subscribed to English newspaper only
english = english_rolls.difference(french_rolls)

# Print number of students subscribed
print(len(english))
