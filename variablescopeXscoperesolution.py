# variable scope = where a vairable is visible and accessible
# 



# def outer():
#     x = "Hello"

#     def inner():
#         print(x)

#     return inner

# func = outer()
# func()   


# def counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# c = counter()
# print(c())  
# print(c()) 
# print(c())  


# def multiplier(n):
#     def multiply(x):
#         return x * n

#     return multiply

# double = multiplier(2)
# print(double(5))  

# triple = multiplier(3)
# print(triple(5))   


# def store_data():
#     data = []

#     def add(item):
#         data.append(item)
#         return data

#     return add

# my_store = store_data()
# print(my_store("A")) 
# print(my_store("B"))  