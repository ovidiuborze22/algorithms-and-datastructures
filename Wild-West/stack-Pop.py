# stack - Pop

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

    def pop(self):
        # TODO
        if self.first == None:
            return None
        removedNode = self.first
        self.first = removedNode.next 
        self.size -= 1
        if self.size == 0:
            self.last = None
        return removedNode.data

stack = Stack()
stack.push(10)
stack.push(100)
stack.push(1000)
removed = stack.pop()
print(removed) #1000
print(stack.size) #2
stack.pop()
stack.pop()
print(stack.size) #0