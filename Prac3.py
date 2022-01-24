"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK :
"""

# Find Captain Room Number

rep_room = int(input())  # total number of repeated rooms
room_no = list(map(int, input().split(' ')))  # input for room number

for i in range(len(room_no)):
    temp = room_no.count(i)
    if temp == 1:
        captain_room = i  # storing captain's room in its variable

print(captain_room)
