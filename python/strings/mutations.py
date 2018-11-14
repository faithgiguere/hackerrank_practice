"""Problem: https://www.hackerrank.com/challenges/python-mutations/problem"""

def mutate_string(string, position, character):
    # Convert string to list
    l = list(string)
    # Replace given position with character provided
    l[position] = character
    # Return as a string
    return "".join(l)
    