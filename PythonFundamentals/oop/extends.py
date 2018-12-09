class Animal(object):
    def run(self):
        print("Animal is running...")
    def __len__(self):
        return 10
class Dog(Animal):
    def run(self):
        print("Dog is running")
    pass
    def __len__(self):
        return 100
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

print(dog.__len__())
run_twice(dog)
run_twice(cat)
type(dog) == Dog
type(dog) == Animal
