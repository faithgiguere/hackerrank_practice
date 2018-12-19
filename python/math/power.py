"""Problem: https://www.hackerrank.com/challenges/python-power-mod-power/problem"""

# Read in the three values
a, b, m = (int(input()) for _ in range(3))

# Print a^b and a^b mod m
print(pow(a,b))
print(pow(a,b,m))
