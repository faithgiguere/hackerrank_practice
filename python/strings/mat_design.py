"""Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem"""

# Read in values for mat size
n, m = map(int,input().split())

# Pattern is .|. centered in -'s
top_design = [('.|.'*(2*i + 1)).center(m,'-') for i in range(n//2)]
# Center line
center = ['WELCOME'.center(m,'-')]
# Bottom half is top design reversed
bottom_design = top_design[::-1]

print('\n'.join(top_design + center + bottom_design))
