"""Problem: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem"""

# Read in the four values
a, b, c, d = (int(input()) for _ in range(4))

result = a**b + c**d
print(result)
