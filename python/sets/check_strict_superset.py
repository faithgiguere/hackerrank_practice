"""Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem"""

# Read in set A
A = set(map(int, input().split()))
# Number of other sets
N = int(input())
# Holds result of whether A was a strict superset to all other sets or not
is_strict_superset = False

# Check each of the N sets against set A
for _ in range(N):
    B = set(map(int, input().split()))
    # If B is subset, but not equal to A, A is strict superset
    if B == B.intersection(A) and B != A:
        is_strict_superset = True
    else:
        # Otherwise A is not strict superset
        is_strict_superset = False
        break

print(is_strict_superset)
