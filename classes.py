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


class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year

    def welcome(self):
        print(f'Welcome our {self.year} student {self.name}, age {self.age}.')


p1 = Person('John', 18)
print(p1.name, p1.age)
p1.myFunction()
p2 = Student('Adam', 19, 'sophmore')
print(p2.name, p2.age, p2.year)
p2.welcome()


class Vehicle:
    def __init__(self, name, rank, battle_rating):
        self.name = name
        self.rank = rank
        self.battle_rating = battle_rating


class Tank(Vehicle):
    def __init__(self, name, rank, battle_rating, crew):
        super().__init__(name, rank, battle_rating)
        self.crew = crew

    def desc(self):
        print(f'Tank {self.name}, Rank {self.rank}, BR: {self.battle_rating}, crew of {self.crew}')


class Plane(Vehicle):
    def __init__(self, name, rank, battle_rating, alt):
        super().__init__(name, rank, battle_rating)
        self.alt = alt

    def desc(self):
        print(f'Plane {self.name}, Rank {self.rank}, BR: {self.battle_rating}, max altitude of {self.alt}')


t1 = Tank('M4 Sherman', 4, 5.7, 6)
t2 = Tank('Pz 4', '3', '3.7', '5')

p1 = Plane('P-51', 3, 3.7, 6500)
p2 = Plane('109 F2', '4', '4.3', '7000')

t1.desc()
t2.desc()

p1.desc()
p2.desc()
