# What is the runtime of the code below

def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0               # branches^depth -------------> O(2^N)
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


allFib(4)

# fib(1) -----> 2^1 steps
# fib(2) -----> 2^2 steps
# fib(3) -----> 2^3 steps -------> Total work = 2^1+2^2+2^3+2^4+...+2^n    
# fib(3) -----> 2^4 steps                     =2^n+1-2
# ...
# fib(n) -----> 2^n steps

# Time Complexity : O(2^N)