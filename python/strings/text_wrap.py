"""Problem: https://www.hackerrank.com/challenges/text-wrap/problem"""

def wrap(string, max_width):
    str = ''
    # Add groups of characters into str by length of max_width
    for i in range(0,len(string), max_width):
        str += (string[i:i+max_width]) + '\n'
    
    return str
    