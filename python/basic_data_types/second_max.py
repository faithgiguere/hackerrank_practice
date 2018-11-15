"""Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem"""

if __name__ == '__main__':
    n = int(input())
    # Read integers into array
    arr = map(int, input().split())
    
    # Sort array and remove duplicates
    sorted_arr = sorted((set(arr)))
    
    # Print second highest of sorted values
    print(sorted_arr[-2])
    