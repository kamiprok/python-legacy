def fizzbuzz(x, y):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(x+y)
        elif i % 3 == 0:
            print(x)
        elif i % 5 == 0:
            print(y)
        else:
            print(i)


fizzbuzz('Fizz', 'Buzz')
