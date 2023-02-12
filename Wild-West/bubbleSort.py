# Bubble Sort

def bubbleSort(arr, comparator=None):
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


print(bubbleSort([4,20,12,10,7,8])) # [4, 7, 8, 10, 12, 20]
print(bubbleSort([0, -9, 7, 3])) # [-9, 0, 3, 7]
print(bubbleSort([1,2,3]))  # [1, 2, 3]
print(bubbleSort([]))  #[]
 
