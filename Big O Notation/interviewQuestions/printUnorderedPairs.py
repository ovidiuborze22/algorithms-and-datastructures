# What is the runtime of the code below

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(array[i] + "," + array[j])

# 1.Counting the iterations             2. Average work
# 1st ----> n-1                         Outer loop - N times
# 2nd ----> n-2                         Inner loop?
#      .                                    1st ----> 10 -
#      .                                    2nd ----> 9   -
#      1                                          .         - = 5 ----> 10/2
#                                                 .       -     n ----> n/2
# (n-1)+(n-2)+(n-3)+...+2+1                       1     -
# =1+2+...+(n-3)+(n-2)+(n-1)
# =n(n-1)/2                                 n*n/2=n^2/2 ----> O(N^2)            
# =n^2/2 + n
# =n^2
# Time complexity: O(N^2)
