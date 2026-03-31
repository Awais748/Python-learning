# Inheritance = Allow a class to inherit attributes and method from another class
#               helps with code resubility and exttensibility
#               class Child(Parent)


# class Animal:
#     def __init__(self, name, ):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")    

# class Dog(Animal):
#    pass 

# class Cat(Animal):
#     pass 


# class Mouse(Animal):
#     pass

# dog = Dog("Buddy", "Golden Retriever")
# cat = Cat("Whiskers", "Siamese")
# mouse = Mouse("Jerry", "House Mouse")
# print(dog.name)
# print(cat.name)       
# print(mouse.name)  


# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#         self.is_running = False

#     def start(self):
#         self.is_running = True
#         print(f"{self.brand} vehicle started")

#     def stop(self):
#         self.is_running = False
#         print(f"{self.brand} vehicle stopped")


# class Car(Vehicle):
#     def honk(self):
#         print(f"{self.brand} car is honking 🚗")


# class Bike(Vehicle):
#     def wheelie(self):
#         print(f"{self.brand} bike is doing a wheelie 🏍️")


# class Truck(Vehicle):
#     def load(self):
#         print(f"{self.brand} truck is loading goods 🚚")


# car1 = Car("Toyota")
# bike1 = Bike("Yamaha")
# truck1 = Truck("Volvo")

# car1.start()
# car1.honk()

# bike1.start()
# bike1.wheelie()

# truck1.start()
# truck1.load()