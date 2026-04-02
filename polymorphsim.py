# Polymorphism = same method name, different behavior

class Cat:
    def sound(self):
        print("Cat meows")

class Dog:
    def sound(self):
        print("Dog barks")

class Cow:
    def sound(self):
        print("Cow moos")


# Function that works with all objects
def animal_sound(animal):
    animal.sound()


# Objects
cat = Cat()
dog = Dog()
cow = Cow()

# Same function, different outputs
animal_sound(cat)
animal_sound(dog)
animal_sound(cow)