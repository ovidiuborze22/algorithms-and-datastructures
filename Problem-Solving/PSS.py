# A Recipe for Problem Solving 

# STEP 1 - Understand the problem
# STEP 2 - Examples
# STEP 3 - Break it Down
# STEP 4 - Solve or Simplify
# STEP 5 - Look Back and Refactor

# STEP 1 - Understand the problem

# 1. Can we restate the problem in our own words?
# 2. What are the inputs that go into the problem?
# 3. What are the outputs that come from the problem?
# 4. Can the outputs be determined from the inputs? In other words
#    do we have enough information to solve this problem?
# 5. What should I label the important piece of data that are the part of a problem

# Step 1 
# Write a function that takes two numbers and returns their sum

# 1. Implement addition
# 2. Integer? Float? Or?
# 3. Integer? Float? Or?
# 4. Yes
# 5 Add, Sum

# STEP 2 - Examples 

# 1. Start with simple examples
# 2. Progress to more complex examples
# 3. Explore examples with empty
# 4. Explore the examples with invalid inputs

# Write a function which takes in a string and returns count of each character in a string

# 1. simple examples
# charCount("bbbb")
# {b: 4}
# charCount("hello")
# {h:1, e:1, l:2, o:1}

# 2. complex examples
# "My name is Ovidiu"

# 3. empty
# charCount("")

# 4. invalid input
# charCount(1)

# STEP 3 - Break it Down
# Write a function which takes in a string and returns count of each character in a string

#charCount("My name is Ovidiu")
    # {m:2,
    #  y:1,
    #  n:1,
    #  a:1,
    #  e:1,
    #  i:3,
    #  s:1,
    #  o:1,
    #  v:1,
    #  d:1,
    #  u:1}

# def charCount(strn):
    # declare an object to return at the end
    # loop over the string
        # if the char is letter and it is in out object add one to the value
        # if the char is letter and it is not in our object add that char to our obeject with the value of one
    # return an object

# STEP 4 - Solve or Simplify

# Write a function which takes in a string and returns count of each character in a string

#charCount("My name is Ovidiu")
    # {m:2,
    #  y:1,
    #  n:1,
    #  a:1,
    #  e:1,
    #  i:3,
    #  s:1,
    #  o:1,
    #  v:1,
    #  d:1,
    #  u:1}

# def charCount(strn):
#     # declare an object to return at the end
#     result = {}
#     # loop over the string
#     for i in strn.lower():
#         # if the char is lowercase letter and it is in out object add one to the value
#         if i in result:
#             result[i] +=1
#         # if the char is lowercase letter and it is not in our object add that char to our obeject with the value of one
#         else:
#             result[i] = 1
#     # return an object
#     return result

# print("Simple example:")
# print(charCount("hello"))

# print("\nMore complex example:")
# print(charCount("My name is Ovidiu"))

# STEP 5 - Look Back and Refactor

# * Can we check the result?
# * Can we drive the result differently?
# * Can we understand it at a glance?
# * Can we use the result or method for some other problem
# * Can you improve the performance of your solution
# * How other people solve this problem

def charCount(strn):
    # declare an object to return at the end
    result = {}
    # loop over the string
    for i in strn.lower():
        # if the char is lowercase letter and it is in out object add one to the value
        if isinstance(i, str) and not (i.isspace()):
            if i in result:
                result[i] +=1
            # if the char is lowercase letter and it is not in our object add that char to our obeject with the value of one
            else:
                result[i] = 1
    # return an object
    return result

print("Simple example:")
print(charCount("hello"))

print("\nMore complex example:")
print(charCount("My name is Ovidiu"))
