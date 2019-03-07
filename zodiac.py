i = input('Podaj miesiąc urodzenia: ')

if i.lower() == 'styczen' or i.lower() == 'styczeń' or i.lower() == '1':
    j = int(input('Podaj dzień urodzenia: '))
    if j < 15:
        print('Jesteś 1')
    elif 15 < j < 31:
        print('Jesteś 2')
    else:
        print('zły dzień')
elif i.lower() == 'luty' or i.lower() == 'lutym' or i.lower() == '2':
    j = int(input('Podaj dzień urodzenia: '))
    if j < 15:
        print('Jesteś 2')
    elif 15 < j < 28:
        print('Jesteś 3')
    else:
        print('zły dzień')
else:
    print('zły miesiąc')

