"""Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""

from collections import Counter

# Size of each family
K = int(input())
# Room numbers per person
rooms = map(int, input().split())
# Frequency of each room number
room_count = Counter(rooms)
# Print minimum which is captain's room (only single-occurance room)
print(min(room_count, key=room_count.get))
