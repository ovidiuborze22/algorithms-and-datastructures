# Singly Linked List - Get

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
    
    def get(self, index):
        # TODO
        if index < 0 or index >= self.length:
            return None
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.next
        return currentNode

singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))  # Success
print(singlyLinkedList.push(10))  # Success
print(singlyLinkedList.push(15))  # Success
print(singlyLinkedList.push(20))  # Success
 

print(singlyLinkedList.get(0).val)    # 5
print(singlyLinkedList.get(1).val)    # 10
print(singlyLinkedList.get(2).val)    # 15
print(singlyLinkedList.get(3).val)    # 20
print(singlyLinkedList.get(4))    # None