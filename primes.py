prime = int(input('Podaj liczbe: '))
#print('Liczba: ', prime)

for i in range(2, prime):
    if (prime % i) == 0:
        print(prime, 'nie pierwsza')
        break

else:
    print(prime, 'pierwsza')
