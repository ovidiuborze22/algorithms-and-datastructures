# Binary Search Tree - Find

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
           if(self.root==None):
                  self.root=Node(data)
           else:
                  self._insert(data,self.root)
 
 
    def _insert(self, data, curNode):
           if(curNode.data>data):
                  if(curNode.left==None):
                         curNode.left=Node(data)
 
                  else:
                         self._insert(data,curNode.left)
           else:
                   if(curNode.right==None):
                         curNode.right=Node(data)
                   else:
                         self._insert(data,curNode.right)
    
    def find(self, data):
        # TODO
        currentNode = self.root
        while currentNode:
            if data == currentNode.data:
                return currentNode
            if data < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return None

bsTree = BST() 
bsTree.insert(15)
bsTree.insert(20)
bsTree.insert(10)
bsTree.insert(12)
 
print(bsTree.find(20).data) # 20
print(bsTree.find(20).right) # None
print(bsTree.find(20).left) # None
print(bsTree.find(100)) # None