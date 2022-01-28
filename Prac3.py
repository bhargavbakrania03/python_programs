"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/edit/main/Prac3.py
"""

# Find Captain Room Number

rep_room = int(input())  # total number of repeated rooms
room_no = list(map(int, input().split(' ')))  # input for room number
captain = []
error = 0

for i in range(len(room_no)):
    temp = room_no.count(i)
    if temp == 1:
        c_room = i  # storing captain's room in its variable
        captain.append(i)
    elif temp != rep_room:
        error = 1

if error == 1:
    print('Please enter proper groups !')
else:
    print(c_room)

