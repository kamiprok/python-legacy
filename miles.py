# app to calculate miles to kilometers and vice versa

speed = int(input('Enter a number: '))

if 0 < speed < 1001:
    print(f'{speed} miles is around {round(speed/0.6124)} kilometers')
    print(speed, 'kilometers is around', round(speed * 0.6124), 'miles')
elif speed == 0:
    print('You are not moving anyway...')
elif speed < 0:
    print("You can't go that slow...")
elif speed > 1001:
    print('You are going too fast!')
else:
    print('error')


