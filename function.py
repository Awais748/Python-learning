# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.


# Example 1: Addition
# def add(a, b):
#     return a + b

# print("Addition:", add(5, 3))


# Example 2: Even or Odd
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print("7 is:", check_even_odd(7))


# Example 3: Maximum number
# def find_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print("Max number:", find_max(10, 20))


# Example 4: Full name
# def full_name(first, last):
#     return first + " " + last

# print("Full Name:", full_name("Awais", "Tariq"))


# default arguments = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your funcations more flexible, reduces # of argumnets


  
# def net_price(list_price, discount=10, tax=0.5):
#     return list_price *(1 - discount) * (1 + tax)

# print(net_price(500))


# def counterprogram(count=1):
#     return count + 1

# print(counterprogram())


# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet("Awais")   # custom value
# greet()          # default value


# def user_info(name, age=18):
#     print(f"Name: {name}")
#     print(f"Age: {age}")

# user_info("Awais", 20)  # custom age
# user_info("Ali")        # default age



# Keyword arguments = an argument preceded by an identifier
#                     help with readability order of arguments doesn't matter


# def student(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")

# student(age=19, name="Awais")


# def info(name, city, country):
#     print(name, city, country)

# info("Awais", country="Pakistan", city="Gujranwala")


# def user(name, age=18):
#     print(f"{name} is {age} years old")

# user(name="Ali")
# user(age=20, name="Awais")



# ARBITRARY
#  *args    = allow you to pass multiple non-key argumnets
#  **kwargs = allows you to pass multiple keyword-arguments
#             * unpacking operator

# def total_sum(*args):
#     total = 0             
#     for num in args:       
#         total += num
#     return total          

# print(total_sum(1, 2, 3))   
# print(total_sum(5, 10))    

# def find_max(*args):
#     max_num = args[0]         
#     for num in args:
#         if num > max_num:
#             max_num = num     
#     return max_num

# print(find_max(1,2,3,4,5,6))   
# print(find_max(10, 5, 20, 3)) 


# kwargs

# def print_value(**kwargs):
#      return kwargs

# result = print_value(name="Awais" , age=19, city="gujrat")
# print(result)