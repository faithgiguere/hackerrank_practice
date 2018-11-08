"""Problem: https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen"""

def count_substring(string, sub_string):
    # Number of times sub_string is in string
    count = 0
    
    # Check how many times sub_string is equal to string of same number of characters 
    for i in range(len(string) - len(sub_string) + 1):
        # If section of string equals sub_string, increase count
        if string[i:(i + len(sub_string))] == sub_string:
            count += 1
    
    return count