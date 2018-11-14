"""Problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem"""

def split_and_join(line):
    # Split the string by whitespace
    line = line.split()
    
    # Join the string with a hyphen
    line = "-".join(line)
    
    return(line)
    