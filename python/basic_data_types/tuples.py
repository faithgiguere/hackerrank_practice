"""Problem: https://www.hackerrank.com/challenges/python-tuples/problem"""

if __name__ == '__main__':
    n = int(input())
    # Read in numbers and convert from strings to ints
    integer_list = map(int, input().split())
    
    # Convert list to tuple
    t = tuple(integer_list)
    
    print(hash(t))