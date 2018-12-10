# first
class Animal(object):
    pass

# feature
class Runnable(object):
    def run(self):
        print('running ...')
class Flyable(object):
    def fly(self):
        print('Flying ...')
class CarnivourousMixIn(object):
    def hunt(self):
        print('Hunting ...')
class H
# second
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
# third
class Dog(Mammal, Runnable, CarnivourousMixIn):
    pass
class Bat(Mammal, Flyable):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
