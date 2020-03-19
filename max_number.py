# Write a function that returns the maximum of two numbers

numbers = input('write 2 numbers:\n')

numbers2 = numbers.split(' ')
print(numbers2)

numbers3 = []
for x in numbers2:
    x = int(x)
    print(x)
    print(type(x))
    numbers3.append(x)

print(numbers2)
print(type(numbers2))
print(numbers3)
print(type(numbers2))
print(type(numbers2[0]))
print(type(numbers3[0]))


if numbers3[0] > numbers3[1]:
    print('the larger number is', numbers3[0])
elif numbers3[0] < numbers3[1]:
    print('the larger number is', numbers3[1])
else:
    print('the numbers are equal')


# Write a function that returns the maximum of two numbers
# CORRECT VERSION

numbers7 = input('Gimme the nums:\n').split(" ")
print(max([int(x) for x in numbers7]))
