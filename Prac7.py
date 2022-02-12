"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK :
"""

# Lapindrome is defined as a string which when split in the middle, gives two
# halves having the same characters and same frequency of each character. If there
# 1,2
# Page 3 of 3
# are odd number of characters in the string, we ignore the middle character and
# check for lapindrome. For example gaga is a lapindrome, since the two halves ga
# and ga have the same characters with same frequency. Also, abccab, rotor and
# xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
# The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.

num = int(input())  # taking the number of strings user want to enter
lap = []
pt1 = []
pt2 = []

for i in range(num):
    ip_str = input()  # taking the string input from user
    lap.append(ip_str)
    length = len(ip_str)  # storing the length of string in a variable
    if length % 2 == 0:  # if the length of string is even then apply this case to divide the string
        pt1.append(ip_str[0:int((length/2))])
        pt2.append(ip_str[int(length/2):int(length)])
    else:  # if the length of string is odd then apply this case to divide the string
        pt1.append(ip_str[0:int((length / 2))])
        pt2.append(ip_str[int(length / 2)+1:int(length)])

for i in range(num):
    pt1[i] = sorted(pt1[i])  # sorting the alphabets in the pt1 list
    pt2[i] = sorted(pt2[i])  # sorting the alphabets in the pt2 list
    if pt1[i] == pt2[i]:  # if both the strings are same, then print 'YES'
        print('YES')
    else:  # if both the strings are different, then print 'NO'
        print('NO')
