"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/edit/main/Prac5.py
"""

# You are given a string and your task is to swap cases. In other words, convert
# all lowercase letters to uppercase letters and vice versa.

input_str = input()
output_str = '';
error = 0

for i in input_str:
    if i.islower():  # checking whether the selected character is in lowercase or not
        output_str += output_str.join(i.upper())  # converting that character in uppercase and storing it in a variable
    elif i.isupper():  # checking whether the selected character is in uppercase or not
        output_str += output_str.join(i.lower())  # converting that character in lowercase and storing it in a variable
    elif i == ' ':
        output_str += output_str.join(i)  # inserting other special characters as it is
    elif i.isdigit():
        print('Error! String expected, got a number except characters')
        error = 1
        break
    else:
        print('Special characters are not allowed !!')
        error = 1
        break

if error != 1:
    print(output_str)
