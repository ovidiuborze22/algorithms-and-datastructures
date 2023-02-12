# Max Binary Heap - Insert

class MaxHeap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
    
 
 
def heapifyTreeInsert(rootNode, index):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex)
    
def insertNode(rootNode, nodeValue):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full"
    rootNode.customList[rootNode.heapSize+1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize)
 
    return "The value has been successfully inserted"
 
newHeap = MaxHeap(5)
insertNode(newHeap,4)
insertNode(newHeap,5)
insertNode(newHeap,2)
insertNode(newHeap,1)
insertNode(newHeap,6)
print(insertNode(newHeap,10)) # The Binary Heap is full
print(newHeap.customList)   # [None, 6, 5, 2, 1, 4]