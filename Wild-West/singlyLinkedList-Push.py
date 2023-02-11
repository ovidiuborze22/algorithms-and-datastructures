# Singly Linked List - Push

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
       # YOUR CODE HERE
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"

singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))  # Success
print(singlyLinkedList.length)   # 1
print(singlyLinkedList.head.val) # 5
print(singlyLinkedList.tail.val) # 5
 
print(singlyLinkedList.push(10))    # Success
print(singlyLinkedList.length)      # 2
print(singlyLinkedList.head.val)    # 5
print(singlyLinkedList.head.next.val)  # 10
print(singlyLinkedList.tail.val)    # 10