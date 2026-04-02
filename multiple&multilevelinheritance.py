# multiple inheritance = inherit from more than one parent class
#                        C(A,B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                        C(B)<-(A) <- A



# class Prey:
#     def flee(self):
#         print("This is a animal fleeing")

# class Predator:
#     def hunt(self):
#         print("This is a animal hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey , Predator):
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

#  hawk.hunt()
# fish.hunt()
# fish.flee()



class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Car is charging")

class Flying:
    def fly(self):
        print("This vehicle can fly")

class FlyingCar(Car, Flying):
    pass


tesla = ElectricCar()
future_car = FlyingCar()

tesla.start()
tesla.drive()
tesla.charge()

print("-----")

future_car.start()
future_car.drive()
future_car.fly()