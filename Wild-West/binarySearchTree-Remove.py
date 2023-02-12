# Binary Search Tree - Remove

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
 
class BST:
    def __init__(self):
        self.root = Node(None)
 
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = Node(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = Node(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"
def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current
def removeNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = removeNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = removeNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = removeNode(rootNode.rightChild, temp.data)
    return rootNode

bsTree = BST()
insertNode(bsTree.root, 15)
insertNode(bsTree.root, 20)
insertNode(bsTree.root, 10)
insertNode(bsTree.root, 12)
removeNode(bsTree.root, 12)
print(bsTree.root.rightChild.data) #20
print(bsTree.root.leftChild.data) #10
print(bsTree.root.leftChild.rightChild) #None