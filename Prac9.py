"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK :
"""


class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

class Exam(Student):
    sub1 = 0
    sub2 = 0
    sub3 = 0
    sub4 = 0
    sub5 = 0
    sub6 = 0

    def marks_input(self):
        self.sub1 = int(input('\nEnter marks of subject-1 : '))
        self.sub2 = int(input('Enter marks of subject-2 : '))
        self.sub3 = int(input('Enter marks of subject-3 : '))
        self.sub4 = int(input('Enter marks of subject-4 : '))
        self.sub5 = int(input('Enter marks of subject-5 : '))
        self.sub6 = int(input('Enter marks of subject-6 : '))

    def marks(self):
        print("\n----- Subject Marks -----\nSubject 1 : ", self.sub1)
        print("Subject 2 : ", self.sub2)
        print("Subject 3 : ", self.sub3)
        print("Subject 4 : ", self.sub4)
        print("Subject 5 : ", self.sub5)
        print("Subject 6 : ", self.sub6)
        print("------------x------------")

class Result(Exam):
    percent = 0
    total_marks = 0

    def total(self):
        self.total_marks = self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5 + self.sub6
        print("\n---------------x---------------")
        print(">>> Total Marks : ", self.total_marks, " <<<")

    def percentage(self):
        self.percent = self.total_marks / 6
        print(">>> Percentage : ", round(self.percent, 2), " % <<<")
        print("---------------x---------------")


print('-----Enter the details of Student-----')
name = input("Enter the name of Student : ")
roll_no = int(input("Enter the roll no of Student : "))

r1 = Result(roll_no, name)
r1.marks_input()
r1.marks()
r1.total()
r1.percentage()
