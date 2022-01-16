"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
AIM : TO LEARN AND STUDY DICTIONARY IN PYTHON
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/edit/main/Prac2_1.py
"""

# a. Write a Python script to check whether a given key already exists in a dictionary.

d1 = {'First Name': 'Bhargav', 'Middle Name': 'Bipinbhai', 'Surname': 'Bakrania'}
print('Enter a key :-', end=' ')
val = input()
if d1.get(val):
    print('Entered key already exists in dictionary')
else:
    print('Entered key does\'t exist in dictionary')


# b. Write a Python script to merge two Python dictionaries.

dict1 = {0: 15, 1: 14, 2: 13}
dict2 = {3: 12, 4: 11}

dict1.update(dict2)
print(dict1)


# c. Write a Python program to sum all the items in a dictionary.

d3 = {0: 2, 1: 5, 2: 7}
print(sum(d3.values()))


# d. Write a Python script to add a key to a dictionary.

dic = {0: 10, 1: 24}
print('Enter the new key and value : ')
key = input()
value = input()
dic.update({int(key): int(value)})
print('Updated Dictionary :\n', dic)


# e. Write a Python script to concatenate following dictionaries to create a new one.

dic1 = {0: 10, 1: 20}
dic2 = {2: 30, 3: 40}
dic3 = {4: 50, 5: 60}

dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
