
#Polymorphism means one method or interface can have different behaviors depending on the object
class Animal:  # Create parent class
    def sound(self):  # Create sound method
        print("Animal makes a sound")  # Default sound


class Dog(Animal):  # Dog inherits Animal
    def sound(self):  # Override the sound method
        print("Dog says: Bow Bow")  # Dog's behavior


class Cat(Animal):  # Cat inherits Animal
    def sound(self):  # Override the sound method
        print("Cat says: Meow")  # Cat's behavior


dog = Dog()  # Create Dog object
cat = Cat()  # Create Cat object

dog.sound()  # Call sound() for Dog
cat.sound()  # Call sound() for Cat

print(isinstance(Animal, Dog))