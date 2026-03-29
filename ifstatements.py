# if = Do some only if some condition is True 
# Else do something else


age = int(input("Enter you age:"))

if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You have not been born yet!")

else:print("You must be 18+ to sign up")



# Example 2: Check if number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print("This number is positive.")
elif number < 0:
    print("This number is negative.")
else:
    print("This number is zero.")


# Example 3: Find the largest of three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest.")
else:
    print(f"{num3} is the largest.")


# Example 4: Simple grade checker
marks = int(input("Enter your marks out of 100: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")# Day 2 - If Statements
