# app to calculate miles to kilometers and vice versa

speed = int(input('Enter a number: '))

if 0 < speed < 1001:
    print(speed, 'miles is around', round(speed/0.6124), 'kilometers')
    print(speed, 'kilometers is around', round(speed * 0.6124), 'miles')
else:
    print('error')


