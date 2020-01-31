import numpy as np


np.random.seed(1)
secret = 'ripkkairkkkapkrpoampormpipmprompkkaakokoraakkroaakpakkrikmakokioraaipkaipmpkriamkkpakmkkmakoaikokrpi'


for i in range(8):
    index = np.random.randint(100)
    print(secret[index], end='')

