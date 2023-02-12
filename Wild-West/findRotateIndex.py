# Divide and Conquer - findRotatedIndex
import math
 
def findRotatedIndex(arr, num):
    left = 0
    right = len(arr) - 1
    if right>0 and arr[left] >= arr[right]:
        middle = math.floor((left + right) / 2)
        while (arr[middle] <= arr[middle + 1]):
            if arr[left] <= arr[middle]:
                left = middle + 1
            else:
                right = middle - 1
            middle = math.floor((left + right) / 2)
            if middle+1 > len(arr)-1:
                break
        
 
        if (num >= arr[0] and num <= arr[middle]):
            left = 0
            right = middle
        else:
            left = middle + 1
            right = len(arr) - 1
    
    while (left <= right):
        middle = math.floor((left + right) / 2)
        if (num == arr[middle]):
            return middle
        if (num > arr[middle]):
            left = middle + 1
        else:
            right = middle - 1
    return -1

print(findRotatedIndex([3, 4, 1, 2], 4)) # 1
print(findRotatedIndex([4, 6, 7, 8, 9, 1, 2, 3, 4], 8)) # 3
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(findRotatedIndex([37, 44, 66, 102, 10, 22], 14)) # -1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1
print(findRotatedIndex([11, 12, 13, 14, 15, 16, 3, 5, 7, 9], 16)) # 5
print(findRotatedIndex([11, 12, 13, 17, 39], 17)) # 3
print(findRotatedIndex([11], 11)) # 0
print(findRotatedIndex([], 11)) # -1
print(findRotatedIndex([4, 4, 4, 4, 4], 5)) # -1