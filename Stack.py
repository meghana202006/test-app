'''
Program to implement stack using class and object
'''

class Stack:

    def __init__(self , maxSize , top = -1):

        self.maxSize = maxSize

        self.top = top

        self.stack = []

    def displayStack(self):

        print("Stack elements")
        for i in range(self.stack.__len__() - 1, -1 , -1):
            print(self.stack[i])
    
    def __len__(self):
        ctr = 0
        for i in self.stack:
            ctr += 1
        return ctr

    def isEmpty(self):

        return self.stack.__len__() == 0
    
    def push(self , data):
            self.stack.append(data)
            self.top += 1
    
    def isFull(self):

        return self.stack.__len__() == self.maxSize

    def pop(self):

        self.top -= 1
        return self.stack.pop()
        
    def peek(self):

        return self.stack[self.top]
        
    
while(True):

    print("1.Create Stack")
    print("2.Push")
    print("3.Pop")
    print("4.Peek")
    print("5.Display")
    print("6.Exit")

    ch = int(input("Enter your choice:"))

    if(ch == 1):

        size = int(input("Enter the size of stack"))
        newStack = Stack(size)

    elif(ch == 2):
        if(newStack.isFull()):

            print("Stack is overflow")
            
        else:

            data = eval(input("Enter the data to be pushed:"))

            newStack.push(data)

            

    elif(ch == 3):
        if(newStack.isEmpty()):
            print("Stack is underflow")
        else:
            popped_ele = newStack.pop()
            print("ELement popped from stack:",popped_ele)

    elif(ch == 4):

        if(newStack.isEmpty()):
            print("Stack is underflow")
        else:
            peek = newStack.peek()
            print("Peek element:",peek)

    elif(ch == 5):
        if(newStack.isEmpty()):
            print('Stack is Empty')
        else:   
            newStack.displayStack()

    elif(ch == 6):

        print("Exiting the program..")
        break
    else:

        print("Invalid choice please re-enter")



