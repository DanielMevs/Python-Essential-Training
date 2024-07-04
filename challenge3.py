# Python code​​​​​​‌​‌‌​‌​‌‌​‌‌‌‌​‌​​‌‌​‌‌‌​ below

def encodeString(stringVal):
    # Your code goes here.
    left, right = 0, 0
    result = []
    while right < len(stringVal):
        while right < len(stringVal) and (stringVal[right] == stringVal[left]):
            right += 1
        result.append((stringVal[left], right - left))
        left = right
    
    return result


def decodeString(encodedList):
    result = ''
    for char, numChar in encodedList:
        result += char * numChar
    
    return result


print(encodeString('AAAAABBBBAAA'))
print(decodeString([('A', 5), ('B', 4), ('A', 3)]))