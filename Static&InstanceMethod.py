# Static method = A method that belong to a class rather than any object from that class (instance)
#                 usually used for general ytility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = best for utility functions that do not neeed acess to class data


# class employe:
#     def __init__ (self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manaager", "Cashier", "Cook" , "Janitor"]
#         return position in valid_positions
    

# print(employe.is_valid_position("Cook"))     


# class Temperature:

#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return (c * 9/5) + 32

#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f - 32) * 5/9


# print(Temperature.celsius_to_fahrenheit(30))
# print(Temperature.fahrenheit_to_celsius(86))


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     # Instance method
#     def deposit(self, amount):
#         self.balance += amount
#         return f"{self.name} new balance: {self.balance}"

#     # Static method
#     @staticmethod
#     def is_valid_amount(amount):
#         return amount > 0


# acc1 = BankAccount("Awais", 1000)

# print(acc1.deposit(500))              # instance method
# print(BankAccount.is_valid_amount(200))  # static method