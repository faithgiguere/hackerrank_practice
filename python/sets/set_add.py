"""Problem: https://www.hackerrank.com/challenges/py-set-add/problem"""

# Number of country stamps in list
num_stamps = int(input())

# Number of unique country stamps
count = 0
# Holds unqiue countries
countries = set()

for i in range(num_stamps):
    countries.add(input())

print(len(countries))
