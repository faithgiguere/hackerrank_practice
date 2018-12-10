"""Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem"""

# Number students subscribed to English newspaper and list of their rolls
num_english = int(input())
english_rolls = set(map(int,input().split()))

# Number students subscribed to French newspaper and list of their rolls
num_french = int(input())
french_rolls = set(map(int, input().split()))

# Find students subscribed to both newspapers
both = english_rolls.intersection(french_rolls)
# Print length of both (gives number of students)
print(len(both))
