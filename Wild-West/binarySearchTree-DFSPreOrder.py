# Binary Search Tree - DFSPreOrder

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
    def depthFirstSearchPreOrder(self, rootNode, data):
        #TODO
        if rootNode == None:
            return data
        # print(rootNode.data)
        data.append(rootNode.data)
        self.depthFirstSearchPreOrder(rootNode.left, data)
        self.depthFirstSearchPreOrder(rootNode.right, data)
        return data

bsTree = BST() 
bsTree.insert(15)
bsTree.insert(20)
bsTree.insert(10)
bsTree.insert(12)
bsTree.depthFirstSearchPreOrder() # [15, 10, 12, 20]