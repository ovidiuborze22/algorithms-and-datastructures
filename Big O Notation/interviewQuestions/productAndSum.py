# What is the runtime of the code below

def foo(array):
    sum = 0 # ------------------------------------------------> O(1)
    product = 1 # --------------------------------------------> O(1)

    for i in array: # ----------------------------------------> O(n)
        sum += i # -------------------------------------------> O(1)

    for i in array: # ----------------------------------------> O(n)
        product *= i # ---------------------------------------> O(1)
    return "Sum = "+str(sum)+", Product = "+str(product)# ----> O(1)

# Time Complexity : O(n)

# Driver code
if __name__ == '__main__':
    array =[1,2,3,4,5]
    print(foo(array))