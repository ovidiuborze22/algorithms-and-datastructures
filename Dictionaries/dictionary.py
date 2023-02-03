# Dictionaries

#  Update / add an element to the dictionary
myDict = {'name': 'Edy', 'age': 26}
myDict['age'] = 28
myDict['address'] = 'London'
print(myDict)

#  Traverse through a dictionary
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

#  Searching a dictionary
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 27))

#  Delete or remove a dictionary
myDict.pop('address')
print(myDict)
#popitem()
# clear()
# del myDict['age']