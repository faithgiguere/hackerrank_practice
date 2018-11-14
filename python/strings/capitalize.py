"""Problem: https://www.hackerrank.com/challenges/capitalize/problem"""

def solve(s):
    # Put words in string into list
    s = s.split(' ')
    # Capitalize each word and rejoin list as string
    return(' '.join(word.capitalize() for word in s))
