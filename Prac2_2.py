"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
AIM : TO LEARN AND STUDY TUPLE IN PYTHON
"""

# a. Write a Python program to create a tuple with different data types.

tup = (1, 45.23, 'Bhargav', True)
print(tup)


# b. Write a Python program to create a tuple with numbers and print one item.

tup1 = (6, 30, 41, 85)
print(tup1[1])


# c. Write a Python program to add an item in a tuple.

tup1 += (97,)
print(tup1)


# d. Write a Python program to convert a tuple to a string.

tup2 = ('My', 'name', 'is', 'Bhargav')
var = ''.join(tup2)  # join method to connect a tuple to a string variable
print(var)


# e. Write a Python program to find the length of a tuple.

print(len(tup))
