# Singly Linked List - Pop

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
    
    def pop(self):
        if self.head == None:
            return "Undefined"
        removeNode = Node
        if self.head == self.tail:
            removeNode = self.head
            self.head = None
            self.tail = None
        else:
            currentNode = self.head
            while not(currentNode.next == self.tail):
                currentNode = currentNode.next
            removeNode = currentNode.next
            currentNode.next = None
            self.tail = currentNode
        
        self.length -= 1
        return removeNode

singlyLinkedList = SinglyLinkedList()

print("----- Push method -----")
print(singlyLinkedList.push(5))  # Success
print(singlyLinkedList.length)   # 1
print(singlyLinkedList.head.val) # 5
print(singlyLinkedList.tail.val) # 5

print(singlyLinkedList.push(10))    # Success
print(singlyLinkedList.length)      # 2
print(singlyLinkedList.head.val)    # 5
print(singlyLinkedList.head.next.val)  # 10
print(singlyLinkedList.tail.val)    # 10
 
print("----- Pop method -----")
print(singlyLinkedList.pop().val) # 10
print(singlyLinkedList.tail.val)  # 5
print(singlyLinkedList.length)    # 1
print(singlyLinkedList.pop().val) # 5
print(singlyLinkedList.length)    # 0
print(singlyLinkedList.pop())     # Undefined