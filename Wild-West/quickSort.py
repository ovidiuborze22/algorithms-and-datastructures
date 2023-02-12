# Sorting with pivot - quickSort

def pivot (arr, comparator=None, start=0):
    # TODO
    if callable(comparator)==False:
        def comparator(a,b):
            if a < b:
                return -1
            if a > b:
                return 1
            return 0
    pivotIndex = start
    for i in range(start+1,len(arr)):
        if comparator(arr[start], arr[i]) > 0:
            pivotIndex += 1
            [arr[i], arr[pivotIndex]] = [arr[pivotIndex], arr[i]]
    if pivotIndex != start:
        [arr[pivotIndex], arr[start]] = [arr[start], arr[pivotIndex]]
    
    return pivotIndex

def quickSort(arr, comparator=None, start = 0, end=0):
    # TODO
    if start < end:
        pivotIndex = pivot(arr, comparator, start)
        quickSort(arr, comparator, start, pivotIndex - 1)
        quickSort(arr, comparator, pivotIndex + 1, end)
    return arr

arr1 = [5,4,9,10,2,20,8,7,3]
arr2 = [8,4,2,5,0,10,11,12,13,16]
arr3 = ['LilBub', 'Garfield', 'Blue', 'Grumpy']
 
def strLength(a,b):
    return len(a)-len(b)
 
print(pivot(arr1)) # 3
print(pivot(arr2)) # 4
print(pivot(arr3, strLength)) # 1
print(quickSort(arr2, end=len(arr2)-1)) # [0, 2, 4, 5, 8, 10, 11, 12, 13, 16]