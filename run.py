class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print(f'Hello, my name is {p1.name}')


p1 = Person('John', 18)
print(p1.name, p1.age)
p1.myFunction()
