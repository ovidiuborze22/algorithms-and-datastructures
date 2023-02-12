# Stack with Two Queues

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,):
        self.first = None
        self.last = None
        self.size = 0
    
    def enqueue(self,data):
        node = Node(data)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node 
        self.size += 1
        return self.size
    
    def dequeue(self):
        if self.first == None:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.size -= 1
        return temp.value

class Stack:
    def __init__(self):
        # TODO
        self.main = Queue()
        self.helper = Queue()
    
    def push(self, data):
        # TODO
        while self.main.size > 0:
            self.helper.enqueue(self.main.dequeue())
        self.main.enqueue(data)
        while self.helper.size > 0:
            self.main.enqueue(self.helper.dequeue())
        return self
    
    def pop(self):
        # TODO
        return self.main.dequeue()

stack = Stack()
 
print(stack.push(10).push(20).push(30))
print(stack.pop()) # 30
print(stack.pop()) # 20
print(stack.pop()) # 10
print(stack.pop()) # None
print(stack.push(30).push(40).push(50))
print(stack.pop()) # 50
print(stack.push(60))
print(stack.pop()) # 60