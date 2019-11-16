import math

print('Guess the number')
print('\n1. 0 - 100')
print('2. 0 - 1 000')
print('3. 0 - 10 000')
diff = input("\nChoose difficulty: ")

if diff == '1':
    num = input('\n Enter number: ')
    num = (int(num))
    if 0 < num < 100:
        x = 50
        while True:
            print(f'Check if number is {x}')
            if x == num:
                print(f'Your number is: {x}')
                break
            elif x > num:
                x = x / 2
                x = math.floor(x)
                print(f'Smaller. Checking for {x}')
            elif x < num:
                x = x + x / 2
                x = math.floor(x)
                print(f'Bigger. Checking for {x}')

