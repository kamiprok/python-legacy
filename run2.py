# prints multiples of 2 and adds
import time
import math


x = 2
y = 1024
tab = ['k', 'M', 'G', 'T']

while True:
    if x < 1024:
        print(x)
        x = x*2
        time.sleep(0.3)
    elif y <= x < y**2:
        i = x/y
        i = math.floor(i)
        print(f'{i}{tab[0]}')
        x = x*2
        time.sleep(0.3)
    elif y**2 <= x < y**3:
        i = x/y**2
        i = math.floor(i)
        print(f'{i}{tab[1]}')
        x = x*2
        time.sleep(0.3)
    elif y ** 3 <= x < y ** 4:
        i = x / y ** 3
        i = math.floor(i)
        print(f'{i}{tab[2]}')
        x = x * 2
        time.sleep(0.3)
    elif y ** 4 <= x < y ** 5:
        i = x / y ** 4
        i = math.floor(i)
        print(f'{i}{tab[3]}')
        x = x * 2
        time.sleep(0.3)
    elif x == y ** 5:
        i = x / y ** 4
        i = math.floor(i)
        print(f'{i}{tab[3]}')
        print('Finished')
        break


