"""Problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem"""

import string

def print_rangoli(size):
    # Lowercase letters of alphabet
    alphabet = string.ascii_lowercase
    # Number of characters per line 
    # (letters + dashes in middle line)
    length = (size * 2 - 1) + (size * 2 - 2)
    
    # Will hold bottom half of rectangle
    bottom = []
    for i in range(size):
        # Letters in order
        line = "-".join(alphabet[i:size])
        # Join letters in reverse with letters in order to get bottom half
        bottom.append((line[::-1]+line[1:]).center(length, "-"))
        # Reverse bottom to get top half
        top = bottom[:0:-1]
    # Print the two halves top on bottom
    print('\n'.join(top + bottom))
