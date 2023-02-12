# Binary Search Tree - Insert

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

bsTree = BST() 
print(bsTree.insert(15))
print(bsTree.insert(20))
print(bsTree.insert(10))
print(bsTree.insert(12))
print(bsTree.root.data) # 15
print(bsTree.root.right.data) # 20
print(bsTree.root.left.right.data) # 12