# How to calculate power of a number using recursion

def power(base,exp):
    if exp == 0:
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))

print(power(4,2))