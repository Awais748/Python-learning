# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 they are automatically called by many of python's built-in operations.
#                 they allow developers to define or customize the behavior of objects


#  Example 1: __init__ and __str__

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Student name is {self.name}"

# s1 = Student("Awais")
# print(s1)


#  Example 2: __len__

# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __len__(self):
#         return len(self.items)

# obj = MyList([1, 2, 3, 4])
# print(len(obj))



#  Example 3: __add__ (Operator Overloading)

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# n1 = Number(5)
# n2 = Number(3)

# print(n1 + n2)
