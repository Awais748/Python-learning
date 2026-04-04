# @property = Decorator used to define a method as a property (it can accessed like an attributes)
#            Benefit:Add additional logic when read write, or delete attributes
#            Gives you getter, setter, and deleter method


# class Student:
#     def __init__(self, name, gpa):
#         self._name = name
#         self._gpa = gpa

#     @property
#     def gpa(self):
#         return self._gpa

#     @gpa.setter
#     def gpa(self, value):
#         if 0 <= value <= 4:
#             self._gpa = value
#         else:
#             print("Invalid GPA!")

# s1 = Student("Awais", 3.5)
# s1.gpa = 3.8   
# print(s1.gpa)

# s1.gpa = 5    