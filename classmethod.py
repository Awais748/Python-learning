# class method = Allow operations related to the class itself
#                Take (cls) as the first paramter, which represents the class itsself



# class student:

#     count = 0

#     def __init__(self , name , gpa):
#         self.name = name 
#         self.gpa = gpa
#         student.count +=1


#     def get_info(self):

#         return f"{self.name} {self.gpa}"
    
#     @classmethod
#     def get_count(cls):
#         return f"Total # of students: {cls.count}"
    
# student1 = student("awais",3.5)

# print(student.get_count())



class Employee:

    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

    def show_name(self):
        return f"Employee: {self.name}"

    @classmethod
    def show_total(cls):
        return f"Total Employees: {cls.total_employees}"


e1 = Employee("Awais")
e2 = Employee("Ali")
e3 = Employee("Ahmed")

print(Employee.show_total())