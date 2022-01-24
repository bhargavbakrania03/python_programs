"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK :
"""

# Find runner-up from given list

tot_runners = int(input())
runners = list(map(int, input().split(' ')))

runners.sort()  # sorting the list for our ease
runners.reverse()  # reversing the list to find the desired element quickly

for i in runners:
    if i < max(runners):  # finding the first smaller element than maximum element in the list
        print(i)
        break  # terminating the loop after finding desired element
