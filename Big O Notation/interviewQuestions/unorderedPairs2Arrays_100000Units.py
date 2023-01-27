# What is the runtime of the code below

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):# -------------------------------> O(ab)
            for k in range(0,100000):# ------------------------------> ?
                print(str(arrayA[i]) + "," + str(arrayB[j]))# -------> O(1)


# arrayA = [1,2,3,4,5]
# arrayB = [2,6,7,8]
# print(printUnorderedPairs(arrayA,arrayB))

# a = len(arrayA)
# b = len(arrayB) => O(ab)

# 100,000 units of work is still constant ? = O(1)
# Time complexity : O(ab)