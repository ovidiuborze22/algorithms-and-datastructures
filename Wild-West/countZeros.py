# Divide and Conquer - countZeros

import math

def countZeroes(customList):
    # TODO
    left = 0
    right = len(customList)-1
    while left <= right:
        middle = math.floor((left + right)/2)
        if customList[middle] == 1:
            left = middle + 1
        else:
            right = middle - 1
    return len(customList) - left

print(countZeroes([1,1,1,1,0,0])) # 2
print(countZeroes([1,0,0,0,0])) # 4
print(countZeroes([0,0,0])) # 3
print(countZeroes([1,1,1,1])) # 0