"""
ID : 20CE001
NAME : BHARGAV BIPINBHAI BAKRANIA
GITHUB REPOSITORY LINK : https://github.com/bhargavbakrania03/python_programs/blob/main/Prac8.py
"""


class StackStructure:
    list = []

    # insertion and deletion methods for stack
    def push(self, data):
        self.list.append(data)

    def pop(self):
        if len(self.list) > 0: # if stack is not empty
            return self.list.pop()
        else:
            return "No elements in the stack to pop !"

    # to know the size of the stack
    def stackSize(self):
        return len(self.list)

    # printing the stack
    def printStack(self):
        print(self.list)

    # traversal methods
    def has_next(self):
        return bool(len(self.list))

    def next(self):
        return self.pop()

    # to know the top element of stack
    def peek(self):
        if len(self.list) > 0:  # if length of the stack is 0
            return self.list[-1]  # then peek the top element
        else:
            return "No Elements are there in stack."  # else print error element

    # to print the top element of stack
    def printPeek(self):
        print(self.peek())


s1 = StackStructure()
s1.push(5)
s1.push(7)
s1.push(2)
s1.push(26)
s1.push(41)
s1.push(14)
s1.pop()
s1.printStack()
s1.peek()
s1.printPeek()
