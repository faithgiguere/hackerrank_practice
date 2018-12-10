"""Problem: https://www.hackerrank.com/challenges/py-check-subset/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""

# Number of total test cases
num_cases = int(input())

for _ in range(num_cases):
    # Number of elements in first set
    num_A = int(input())
    A = set(map(int, input().split()))
    # Number of elements in second set
    num_B = int(input())
    B = set(map(int, input().split()))

    # Print whether or not  A is a subset of B (A intersects B)
    print(A == A.intersection(B))
    