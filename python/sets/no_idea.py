"""Problem: https://www.hackerrank.com/challenges/no-idea/problem"""

# Number of ints in array and ints in the two sets
n, m = map(int, input().split())
# Array of numbers to be checked against the sets
numbers = list(map(int, input().split()))
# Sets A (+1 happiness) and B (-1 happiness)
A = set(map(int, input().split()))
B = set(map(int, input().split()))
# Total happiness score
happiness = 0

for number in numbers:
    # If number is in set A, add 1 to happiness
    if number in A:
        happiness += 1
    # If number is in set B, subtract 1 from happiness
    if number in B:
        happiness -= 1

print(happiness)
