"""Returns permutations of given word to the provided number of letters."""

from itertools import permutations

word, num = input().split()
# Convert num from str to int
num = int(num)
# Get permutations of word in alphabetical order
p = permutations(sorted(word),num)
l = list(p)
# Convert each tuple in the list to a string
for t in l:
    print(''.join(t))