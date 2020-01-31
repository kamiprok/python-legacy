import time
import os
import random

os.system('cls')


class Colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

    pickColor = [red, blue, green, orange, purple, cyan, lightgrey, darkgrey, lightred, lightgreen, yellow, lightblue, pink, lightcyan]


i = 1
while True:
    # c = random.randint(1, 9)
    # os.system(f'color {c}')
    x = random.choice(Colors.pickColor)
    y = random.choice(Colors.pickColor)
    z = random.choice(Colors.pickColor)
    q = f'{x} hej {y} dejko {z} {i}'
    print(q)
    w = q.split()
    e = w[1] + w[3]
    f = f'{w[1]} {w[3]}'
    r = sorted(e)
    r = r[::-1]
    t = '\n'.join(r)
    print(t)

    g = ''
    k = 0
    for x in f:
        g = g + f[k]
        print(g)
        k += 1
        time.sleep(0.2)

    i += 1
    time.sleep(1)
    # os.system('cls')
