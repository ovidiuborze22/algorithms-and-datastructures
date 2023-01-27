# Big O Notation

array = [1, 2, 3, 4, 5]

######  Constant time complexity  #######
print('######  Constant time complexity  #######')
print(array[0])

######  Linear time complexity  #######
print('######  Linear time complexity  #######')
for element in array:
     print(element)

######  Logarithmic time complexity  #######
print('######  Logarithmic time complexity  #######')
for index in range(0,len(array),3):
     print(array[index])