import math


p1 = input('Podaj srednice 1 pizzy: ')
c1 = input('Podaj cene 1 pizzy: ')
p2 = input('Podaj srednice 2 pizzy: ')
c2 = input('Podaj cene 2 pizzy: ')

p1 = int(p1)
p2 = int(p2)
c1 = int(c1)
c2 = int(c2)

pole_p1 = math.pi * ((p1/2)**2)
pole_p2 = math.pi * ((p2/2)**2)
pole_p1 = round(pole_p1, 2)
pole_p2 = round(pole_p2, 2)

wartosc_p1 = pole_p1 / c1
wartosc_p2 = pole_p2 / c2
wartosc_p1 = round(wartosc_p1, 2)
wartosc_p2 = round(wartosc_p2, 2)

print(f'Pole pizzy 1 = {pole_p1}cm^2')
print(f'Pole pizzy 2 = {pole_p2}cm^2')
print(f'Za 1zl masz {wartosc_p1}cm^2 pizzy 1')
print(f'Za 1zl masz {wartosc_p2}cm^2 pizzy 2')

roznica1 = wartosc_p1 - wartosc_p2
roznica2 = wartosc_p2 - wartosc_p1
roznica1 = round(roznica1, 2)
roznica2 = round(roznica2, 2)

if wartosc_p1 > wartosc_p2:
    print(f'Pizza 1 bardziej sie oplaca o {roznica1}cm^2 za zlotowke')
elif wartosc_p2 > wartosc_p1:
    print(f'Pizza 2 bardziej sie oplaca o {roznica2}cm^2 za zlotowke')
elif wartosc_p1 == wartosc_p1:
    print('Obie pizze sa tyle samo warte')
else:
    print('Cos poszlo nie tak')
input('Press key to exit')
