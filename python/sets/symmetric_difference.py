"""Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem"""

# Number of values in each set and sets - convert strings to sets of ints
n = int(input())
first_set = set(map(int,input().split()))
m = int(input())
second_set = set(map(int,input().split()))

# Numbers in first set not in second
first_diff = first_set.difference(second_set)
# Numbers in second set not in first
second_diff = second_set.difference(first_set)
# Symmetric difference (numbers in one set but not the other)
sym_diff = first_diff.union(second_diff)
# Sort combined set
sorted_sym_diff = sorted(sym_diff)
# Print each in ascending order
for number in sorted_sym_diff:
    print(number)
