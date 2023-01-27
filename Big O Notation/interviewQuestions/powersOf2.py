# What is the runtime of the code below

def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2
        print(curr)
        return curr

powersOf2(50)

# Time Complexity : O(logN)