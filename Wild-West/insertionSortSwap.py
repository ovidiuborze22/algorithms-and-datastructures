# Insertion Sort Swap

def insertionSortSwap(arr, comparator=None):
    # TODO
    if callable(comparator)==False:
        def comparator(a,b):
            if a < b:
                return -1
            if a > b:
                return 1
            return 0
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if comparator(arr[j], arr[j - 1]) < 0:
                [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]]
            else:
                break
    return arr

nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
print(insertionSortSwap(nums))

kit = ['LilBub', 'Garfield', 'Blue', 'Grumpy']
def strComp(a,b):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0
print(insertionSortSwap(kit, strComp))
 
class Kitty:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name +" "+str(self.age)
moreKittyData = [Kitty('LilBub',7),Kitty('Garfield',40),Kitty('Heathcliff',45),Kitty('Blue',1),Kitty('Grumpy',6) ]       
def oldestToYoungest(a,b):
    return b.age - a.age
test = insertionSortSwap(moreKittyData, oldestToYoungest)
for i in test:
    print(i)