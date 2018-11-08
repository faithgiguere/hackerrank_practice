"""Problem: https://www.hackerrank.com/challenges/python-lists/problem"""

if __name__ == '__main__':
    N = int(input())
    l = []
    
    for i in range(N):
        # Read in command, split by whitespace
        s = input().split()
        # Command is first in list, remainder are args
        command = s[0]
        arguments = [int(arg) for arg in s[1:]]
        
        # Print is not an attribute, call it separately
        if command == 'print':
            print(l)
        # Otherwise add attribute and args to list
        else:    
            getattr(l, command)(*arguments)