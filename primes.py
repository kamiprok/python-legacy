while True:
    prime = int(input('Podaj liczbe: '))
    #print('Liczba: ', prime)

    if 0 < prime < 2147483647:
        for i in range(2, prime):
            if (prime % i) == 0:
                print(prime, 'nie pierwsza')
                break

        else:
            print(prime, 'pierwsza')

    else:
        print('poza zakresem')