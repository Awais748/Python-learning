# super() keyword = used to access methods and constructor of the parent class

class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        # calling parent constructor
        super().__init__(name)
        self.breed = breed
        print("Dog constructor called")

    def speak(self):
        # calling parent method
        super().speak()
        print("Dog barks")


# Object
dog1 = Dog("Tommy", "Bulldog")

print(dog1.name)
print(dog1.breed)

dog1.speak()