"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK :
"""

# You are given a string and your task is to swap cases. In other words, convert
# all lowercase letters to uppercase letters and vice versa.

input_str = input()

for i in input_str:
    if i.islower():  # checking whether the selected character is in lowercase or not
        print(i.upper(), end='')  # converting that character in uppercase
    elif i.isupper():  # checking whether the selected character is in uppercase or not
        print(i.lower(), end='')  # converting that character in lowercase
    else:
        print(i, end='')  # printing other special characters as it is
