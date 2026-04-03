# Duck Typing is a concept in Python where the type of an object
# does not matter. What matters is whether
# the object has the required method or behavior.

# class Dog:
#     def sound(self):
#         print("Dog barks")


# class Cat:
#     def sound(self):
#         print("Cat meows")


# def make_sound(animal):
#     animal.sound()


# d = Dog()
# c = Cat()

# make_sound(d)
# make_sound(c)

# class File:
#     def read(self):
#         print("Reading from file")


# class Network:
#     def read(self):
#         print("Reading from network")


# def start_reading(source):
#     source.read()

# f = File()
# n = Network()

# start_reading(f)
# start_reading(n)