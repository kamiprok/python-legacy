import math
import random

a = 0
b = 99
# x = random.randrange(a, b)
# print(x)
y = input('Pick number from 0 to 99: ')
print(y)
while True:
    x = random.randrange(a, b)
    print(f'x={x}, a={a}, b={b}')
    z = input(f'your number is {x} [yes/higher/lower]:')
    if z == 'h':
        print('going higher')
        a = x
    elif z == 'l':
        print('going lower')
        b = x
    elif z == 'y':
        print('success')
        break

print('end')

