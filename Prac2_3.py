"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
AIM : TO LEARN AND STUDY SET IN PYTHON
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/edit/main/Prac2_3.py
"""

# a. Write a Python program to add member(s) in a set and clear a set

set1 = {14, 25, 39, 46}
print(set1)
set1.add(64)
print(set1)
set1.clear()
print(set1) # prints set1() as the set1 is empty now


# b. Write a Python program to remove an item from a set if it is present in the set.

set1 = {14, 25, 39, 46}
print('Enter an element to remove : ')
element = input()
if int(element) in set1:  # checks if the entered element exist in the list or not
    set1.discard(int(element))
    print('Element removed successfully')
    print(set1) # prints updated set1
else:
    print('Entered element doesn\'t exist in the set')


# c. Write a Python program to create an intersection, Union, difference of sets.

set1 = {14, 25, 39, 46}
set2 = {1, 24, 46, 57}

print('Intersection of sets : ', set1.intersection(set2))
print('Union of sets : ', set1.union(set2))
print('Difference of sets(from set1) : ', set1.difference(set2))
print('Difference of sets(from set2) : ', set2.difference(set1))


# d. Write a Python program to find maximum and the minimum value in a set.

print('Maximum value of set1 : ', max(set1))
print('Minimum value of set1 : ', min(set1))


# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

dict1 = {0: 4, 1: 8, 2: 4, 3: 7, 4: 9, 5: 4}
list1 = [1, 8, 'c', 4, 1, 21, 9, 66, 1, 74]
tup = (2, 34, 28, 56, 99, 3, 28, 51, 2, 27)

counter = 0
num1 = []
for i in list1:
    temp = list1.count(i)  # counts total occurrence of mentioned number in the list and stores it in the temp variable
    if temp >= counter:  # if temp is greater than counter, then update the temp
        counter = temp
        if i not in num1:  # if the repeated number doesn't exist in the num1 list, then add it
            num1.append(i)

print('Most Common Element in List : ', num1)  # prints the elements occurring more than 1 time in the list
print('Frequency : ', counter)  # prints the count of that variable

counter = 0
num2 = []
for i in tup:
    temp = tup.count(i)  # counts total occurrence of mentioned number in the list and stores it in the temp variable
    if temp >= counter:  # if temp is greater than counter, then update the temp
        counter = temp
        if i not in num2:  # if the repeated number doesn't exist in the num2 list, then add it
            num2.append(i)

print('Most Common Element in Tuple : ', num2)  # prints the elements occurring more than 1 time in the list
print('Frequency : ', counter)  # prints the count of that variable

num3 = []
for i in dict1:
    num3.append(dict1.get(i))

counter = 0
common_num = []
for i in num3:
    temp = num3.count(i)  # counts total occurrence of mentioned number in the list and stores it in the temp variable
    if temp >= counter:  # if temp is greater than counter, then update the temp
        counter = temp
        if i not in common_num: # if the repeated number doesn't exist in the common_num list, then add it
            common_num.append(i)

print('Most Common Element in Dictionary : ', common_num)  # prints the elements occurring more than 1 time in the list
print('Frequency : ', counter)  # prints the count of that variable
