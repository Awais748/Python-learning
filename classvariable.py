# class variable = shared among all istances of class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class



# class Car:
#     company = "Ford"   # class variable

#     def __init__(self, model, year):
#         self.model = model
#         self.year = year


# car1 = Car("Mustang", 2020)
# car2 = Car("Fiesta", 2018)

# print(car1.company)
# print(car2.company)



# class Student:
#     school_name = "Superior College"   # class variable

#     def __init__(self, name):
#         self.name = name


# s1 = Student("Awais")
# s2 = Student("Ali")

# print(s1.name, "studies at", s1.school_name)
# print(s2.name, "studies at", s2.school_name)


# class BankAccount:
#     interest_rate = 0.05   # class variable (5%)

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance


# acc1 = BankAccount("Awais", 1000)
# acc2 = BankAccount("Ali", 2000)

# print(acc1.interest_rate)
# print(acc2.interest_rate)