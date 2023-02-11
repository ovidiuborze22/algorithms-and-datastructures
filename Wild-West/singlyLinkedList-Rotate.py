# Singly Linked List - Rotate

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
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
        
    def rotate(self, number):
        # TODO
        index =  (number + self.length) if number < 0 else number
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return "No Rotation"
        prevNode = self.head
        for i in range(index-1):
            prevNode = prevNode.next
        if prevNode == None:
            return "No Rotation"
        self.tail.next = self.head
        self.head = prevNode.next
        self.tail = prevNode
        prevNode.next = None
        return "Success"

singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))  # Success
print(singlyLinkedList.push(10))  # Success
print(singlyLinkedList.push(15))  # Success
print(singlyLinkedList.push(20))  # Success
print(singlyLinkedList.push(25))  # Success
 
print(singlyLinkedList.rotate(3))
 
print(singlyLinkedList.head.val)  # 20
print(singlyLinkedList.head.next.val)   # 25
print(singlyLinkedList.head.next.next.val)  # 5
print(singlyLinkedList.head.next.next.next.val) # 10
print(singlyLinkedList.head.next.next.next.next.val) # 15
print(singlyLinkedList.tail.val) # 15
print(singlyLinkedList.tail.next) # None
 
 
singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))  # Success
print(singlyLinkedList.push(10))  # Success
print(singlyLinkedList.push(15))  # Success
print(singlyLinkedList.push(20))  # Success
print(singlyLinkedList.push(25))  # Success
 
print(singlyLinkedList.rotate(-1))
 
print(singlyLinkedList.head.val)  # 25
print(singlyLinkedList.head.next.val)   # 5
print(singlyLinkedList.head.next.next.val)  # 10
print(singlyLinkedList.head.next.next.next.val) # 15
print(singlyLinkedList.head.next.next.next.next.val) # 20
print(singlyLinkedList.tail.val) # 20
print(singlyLinkedList.tail.next) # None