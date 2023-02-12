# Singly Linked List - Set

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
    
    def set(self, index, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            currentNode = self.head
            for i in range(index):
                currentNode = currentNode.next
                
                if currentNode == None:
                    return False
            currentNode.val = value
        return True

singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(1))
print(singlyLinkedList.push(2))
 
print(singlyLinkedList.set(0,10))  # True
print(singlyLinkedList.set(1,20))  # True
print(singlyLinkedList.length)    # 2
print(singlyLinkedList.head.val)  # 10
 
print(singlyLinkedList.set(10,10)) # False
print(singlyLinkedList.set(2,100)) # False
 
print(singlyLinkedList.head.next.val) # 20