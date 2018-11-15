"""Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem"""

if __name__ == '__main__':
    # Read in dimensions of cube and int n
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = []
    
    # Find all coordinates within cube 
    for i in range( x + 1):
        for j in range( y + 1): 
            for k in range (z + 1): 
                # Include coordinates if sum not equal to n
                if ( i + j + k) != n:
                    coordinates.append([i, j, k])
                    
    print(coordinates)
    