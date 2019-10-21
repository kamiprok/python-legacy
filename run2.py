import time
import math

x=2
y=1024
z=y*y
while True:
    if x < 1024:
        print(x)
        x=x*2
        time.sleep(0.3)
    elif y <= x < z:
        x=x/1024
        x = math.floor(x)
        print(f'{x}k')
        x=x*2
        time.sleep(0.3)

