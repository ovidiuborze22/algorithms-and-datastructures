# Stack Push

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
 
    def push(self,data):
        self.first = Node(data, self.first)
 
        if self.size==0:
            self.last = self.first
        self.size += 1
        return self.size

stack = Stack()
print(stack.push(10)) #1
print(stack.first.data) #10
print(stack.last.data) #10
print(stack.push(100)) #2
print(stack.first.data) #100
print(stack.last.data) #10
print(stack.push(1000)) #3
print(stack.first.data) #1000
print(stack.last.data) #10