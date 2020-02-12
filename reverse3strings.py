# slicing

string1 = 'python1'
reversedString1 = string1[::-1]
print(reversedString1)

# loop

string2 = 'python2'
reversedString2 = []
newString2 = ''
index = len(string2)
while index > 0:
    reversedString2 += string2[index - 1]
    index = index - 1
print(reversedString2)
for element in reversedString2:
    newString2 += element
print(newString2)

# join

string3 = 'python3'
reversedString3 = ''.join(reversed(string3))
print(reversedString3)
