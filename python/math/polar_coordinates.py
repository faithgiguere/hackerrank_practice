"""Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem"""
import cmath

# Read in complex number
complex_number = complex(input())
# Convert to polar coordinates
polars = cmath.polar(complex_number)
# Print each coordinate on its own line
print(polars[0])
print(polars[1])
