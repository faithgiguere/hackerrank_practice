"""Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem"""

def average(array):
    # Get distinct values, divide by number of distinct values
    return sum(set(array))/len(set(array))
    