# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base functions
#             Pass the base function as an argument of the decorator

#             @add_sprinkles
 
def add_spinkles(func):
    def wrapper():
        print("You add sprinkles")
        func()
    return wrapper

@add_spinkles
def get_ice_cream():
    print("Here is your ice cream")        


get_ice_cream()    