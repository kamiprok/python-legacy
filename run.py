import re

name = str(input('Enter string: '))
reversed_name = name[::-1]
print(reversed_name)

a = name.replace(' ', '')
b = reversed_name.replace(' ', '')

a = re.sub("[^a-zA-Z]+", "", a)
b = re.sub("[^a-zA-Z]+", "", b)
a = a.lower()
b = b.lower()
print(a)
print(b)

if a == b:
    print(name, 'is palindrome')
else:
    print(name, 'is NOT palindrome')
