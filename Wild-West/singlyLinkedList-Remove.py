# Singly Linked List - Remove

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
        
    def remove(self, index):
        
        if index < 0 or index >= self.length:
            return None
        if self.head is None:
            return None
        else:
            self.length -= 1
            result = self.head
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                return result
            else:
                tempNode = self.head
                indx = 0
                while indx < index - 1:
                    tempNode = tempNode.next
                    indx += 1
                result = tempNode.next
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                return result

singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))  # Success
print(singlyLinkedList.push(10))  # Success
print(singlyLinkedList.push(15))  # Success
print(singlyLinkedList.push(20))  # Success
print(singlyLinkedList.push(25))  # Success
print(singlyLinkedList.remove(2).val) # 15
print(singlyLinkedList.remove(100)) # None
print(singlyLinkedList.length)  # 4
print(singlyLinkedList.head.val)   # 5
print(singlyLinkedList.head.next.val)  # 10
print(singlyLinkedList.head.next.next.val)  # 20