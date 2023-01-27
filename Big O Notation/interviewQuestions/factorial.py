# What is the runtime of the code below

def factorial(n):# -------------------------> M(n)
    if n < 0:     #-
        return -1 # -
    elif n == 0:  # ------------------------> O(1)
        return 1  #-
    else:
        return n * factorial(n-1)# ---------> M(n-1)

print(factorial(3))

# n! = 1*2*3*...*n
# 3! = 1*2*3 = 6

# M(n) = O(1)+M(n-1)
# M(0) = O(1)              -
# M(n-1) = O(1)+M((n-1)-1) ----------> M(n)=1+M(n-1)
# M(n-2) = O(1)+M((n-2)-1) -               =1+(1+M((n-1)-1))
#                                          =2+M(n-2)
#                                          =2+1+M((n-2)-1)
#                                          =3+M(n-3)
#                                               .
#                                               .
#                                          =a+M(n-a)
#                                          =n+M(n-n)
#                                          =n+1
#                                          =n
# Time Complexity : O(N)