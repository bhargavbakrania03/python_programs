"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/edit/main/Prac6.py
"""

# You are given n words. Some words may repeat. For each word, output its
# number of occurrences. The output order should correspond with the input order
# of appearance of the word. See the sample input/output for clarification

num = int(input())  # input the number of words(limit)
words = []

for i in range(num):
    element = input()
    words.append(element)  # adding an element in the list

count = 0
occurrence = ''  # variable to store occurrence of the words in order
temp = []
for i in words:
    if i not in temp:
        temp.append(i)  # adding the element in a temporary list to count
        occurrence += ''.join(str(words.count(i)) + ' ')  # appending element's occurrence in a string variable to print
        count += 1  # counting total number of distinct elements in words list

print(count)  # printing the total count of distinct words
print(occurrence)  # printing the occurrence of distinct words in order
