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