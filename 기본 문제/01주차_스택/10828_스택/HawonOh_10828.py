import sys


class Stack:
    def __init__ (self):
        self.data = []

    def push (self, item):
        self.data.append(item)

    def pop(self):
        #if Stack is not empty
        if not self.empty():
            #pop and return 
            return self.data.pop(-1)
        else:
            return -1

    def size(self):
        return len(self.data)

    def empty(self):
        if len(self.data)==0:
            return 1
        else:
            return 0

    def top(self):
        if not self.empty():
            return self.data[-1]
        else:
            return -1
            

# take input from the users, then create Stack and stack it up.
stack = Stack()
result = []

iteration = int(input())

for i in range(iteration):
    statement = sys.stdin.readline().split()

    if statement[0] == 'push':
        result.append(stack.push(statement[1]))

    elif statement[0] == 'pop':
        result.append(stack.pop())

    elif statement[0] == 'size':
        result.append(stack.size())

    elif statement[0] == 'empty':
        result.append(stack.empty())

    elif statement[0] == 'top':
        result.append(stack.top())

# print all the results
for i in range(len(result)):
    temp = result[i]
    
    if not temp == None:
        print(temp)



