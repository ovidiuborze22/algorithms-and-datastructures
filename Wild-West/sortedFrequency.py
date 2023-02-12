# Divide and Conquer - sortedFrequency

import math

def sortedFrequency(arr, num):
    # TODO
    left = 0
    right = len(arr) - 1
 
    while left <= right:
        middle = math.floor((left + right) / 2)
        if arr[middle] == num:
            leftCount = middle
            rightCount = middle
            while arr[leftCount] == num and leftCount >= 0:
                leftCount -= 1
 
            while rightCount < len(arr) and arr[rightCount]  == num :
                rightCount += 1
                
 
            return rightCount - leftCount - 1
 
        if arr[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
 
    return -1

print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2)) # 4
print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 3)) # 1
print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4)) # -1
print(sortedFrequency([], 4)) # -1