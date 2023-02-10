# Recursive Range

def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)

print(recursiveRange(6)) # 21
print(recursiveRange(10)) # 55 