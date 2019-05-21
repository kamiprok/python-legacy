def funkcja_args(*args):
    print(*args)


funkcja_args('coś', 1, 5)


def funkcja_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


funkcja_kwargs(name="John", surname="Smith")
