# Stringify Numbers

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
 

def stringifyNumbers(obj):
    # TODO
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj

print(stringifyNumbers(obj))
 
{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}