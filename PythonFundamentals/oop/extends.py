class Animal(object):
    def run(self):
        print("Animal is running...")
class Dog(Animal):
    def run(self):
        print("Dog is running")
    pass
class Cat(Animal):
    pass
dog = Dog()
dog.run()
cat = Cat()
cat.run()
isinstance(dog, Dog)
isinstance(dog, Animal)
isinstance(dog, object)
def run_twice(animal): # just to make sure animal has run() method
    animal.run()
    animal.run()

run_twice(dog)
run_twice(cat)
