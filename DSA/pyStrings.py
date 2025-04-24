from copy import deepcopy
import re
from collections import deque

str1 = "Python"
print(str1)

*_, = str1 
print(_)

str1 = "Python2"

a = ['a',['b','c'], 'd']
b  = a
print(a, b)
b[1][0] = 'x'
print(a, b)


# def StringsOperations():

#     def __init__(self):
#         pass
    
#     def stringToCharArray(self, str1):
#         *_, = str1
#         return _
    
# strops = StringsOperations()
# print(strops.stringToCharArray("Python"))


str1 = "ab-cd"

print(str1[::-1])

str2 = "a-bC-dEf=ghIj!!"



# Find all special characters and their indices
special_chars = [(match.start(), match.group()) for match in re.finditer(r"[^a-zA-Z0-9\s]", str2)]

print(special_chars)
clean_str = re.sub(r"[^a-zA-Z0-9\s]", "", str2)
print(clean_str[::-1])

deque_str = deque(re.findall(r'[a-zA-Z]', str2))

print(deque_str.pop())


def reverse_letters(text):
    # Extract letters
    letters = deque(re.findall(r'[a-zA-Z]', text))
    
    # Replace letters in reversed order while keeping other characters unchanged
    result = ''.join(letters.pop() if char.isalpha() else char for char in text)
    
    return result

# # Example usage
# text = "Hello, World! 123"
# reversed_text = reverse_letters(text)
# print(reversed_text)