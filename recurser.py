def fun(n):
    for n in range(n, 0, -1):
        if n == 1:
            print(n)
        else:
            print(n * (n-1))


fun(5)
