# Match-case statement (switch): An alternative to using "elif" statements
#                                excute some code if a value matvhes a 'case'
#                                benefits: cleaner and syntax is more readable


# def match_case_example(value):
#     match value:
#         case 1:
#             return "One"
#         case 2:
#             return "Two"
#         case 3:
#             return "Three"
#         case _:
#             return "Unknown"

# day = input("Enter a day: ").lower()

# match day:
#     case "monday":
#         print("Start of the week")
#     case "friday":
#         print("Almost weekend")
#     case "sunday":
#         print("Rest day")
#     case _:
#         print("Just a normal day")


# point = (0, 0)

# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y-axis at {y}")
#     case (x, 0):
#         print(f"X-axis at {x}")
#     case (x, y):
#         print(f"Point at ({x}, {y})")
