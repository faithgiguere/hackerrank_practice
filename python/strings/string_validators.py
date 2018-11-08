"""Problem: https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen"""

if __name__ == '__main__':
    s = input()
    
    # Use any to check if any character returns true for each method
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))