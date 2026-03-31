# object  = A bundle of related attributes (data) and methods(function)
#           Ex. phone, cup, book
#          you need a "class" to create an objects


# class = (blue print) used to design the structure and layput of an object 



# class Car:
#     def __init__(self , model , year , color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale


# car1 = Car("Mustang", 2020, "Red", True)
# car2 = Car("Camaro", 2021, "Yellow", False)         

# print(car1.model)
# print(car1.year)    
# print(car1.color)
# print(car1.for_sale)


# class Student:
#     def __init__(self, name, marks, grade):
#         self.name = name
#         self.marks = marks
#         self.grade = grade

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)
#         print("Grade:", self.grade)


# student1 = Student("Awais", 85, "A")
# student2 = Student("Ali", 70, "B")

# student1.display()
# print("-----")
# student2.display()



# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print("Withdrawn:", amount)

#     def show_balance(self):
#         print("Current Balance:", self.balance)


# acc1 = BankAccount("Awais", 1000)

# acc1.deposit(500)
# acc1.withdraw(300)
# acc1.show_balance()