"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/edit/main/Prac4.py
"""

# Find runner-up from given list

tot_runners = int(input())
runners = list(map(int, input().split(' ')))
error = 0

if len(runners) > tot_runners:  # to check that entered size and number of contestants matches or not
    print('Please enter scores according to the number of contestants !')
    error = 1
else:
    runners.sort()  # sorting the list for our ease
    runners.reverse()  # reversing the list to find the desired element quickly
    for i in runners:
        if i < max(runners):  # finding the first smaller element than maximum element in the list
            print(i)
            break  # terminating the loop after finding desired element
