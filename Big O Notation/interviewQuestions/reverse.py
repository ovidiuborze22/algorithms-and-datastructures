# What is the runtime of the code below

def reverse(array):
    for i in range(0,int(len(array)/2)): # -------------> O(N/2) --> O(n)
        other = len(array)-i-1# ------------------------> O(1)
        temp = array[i] # ------------------------------> O(1)
        array[i] = array[other]# -----------------------> O(1)
        array[other] = temp # --------------------------> O(1)
    print(array) # -------------------------------------> O(1)

# arrayA = [1,2,3,4,5]
# arrayB = [2,6,7,8]
# print(reverse(arrayA))

# Time Complexity : O(N)