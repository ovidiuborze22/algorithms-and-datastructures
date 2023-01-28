# Python Lists

# Accessing/Traversing the list
shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")

# Update/Insert - List 
myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)

# Slice/Delete from a List
sliceList = ['a', 'b', 'c', 'd', 'e', 'f']
print(sliceList[0:2])
print(sliceList[:2])
print(sliceList[1:])
print(sliceList[:])
sliceList[0:2] = ['x', 'y']
sliceList.pop()
print(sliceList)
del sliceList[:2]
print(sliceList)
sliceList.remove('e')
print(sliceList)

#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))