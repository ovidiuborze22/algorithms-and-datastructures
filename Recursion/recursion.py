#### Russian Doll recursive function ###

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)


openRussianDoll(4)


# def recursionMethod(parameters):
#     if  exit from condition satisfied:
#         return some value
#     else:
#         recursionMethod(modified parameters)


def firstMethod():
    secondMethod()
    print("I am the first Method")

def secondMethod():
    thirdMethod()
    print("I am the second Method")

def thirdMethod():
    fourthMethod()
    print("I am the third Method")

def fourthMethod():
    print("I am the fourth Method")


firstMethod()


def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else: 
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)