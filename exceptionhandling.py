# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, typeError, ValueError)
#             1.try, 2.except, 3.finally

# Examples:
# - ZeroDivisionError → when a number is divided by 0
# - TypeError → when incorrect data types are used
# - ValueError → when the value is in the wrong format

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
      print("You can't divide by zero buddy")
except ValueError:
     print("Enter only numbers please")      
finally:
     print("Do some cleanup here ")     