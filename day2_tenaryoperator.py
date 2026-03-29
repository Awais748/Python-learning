#    Condironal expression = A one-line shortcut for the if-else statetment(ternary operator)
#    Print or assign one of two values based on a condition
#    X if condition else Y 


# Example 1: Positive ya Negative check
num = 5

result = "Positive" if num >= 0 else "Negative"

print("Example 1:", result)



#  Example 2: Even ya Odd check
number = 7

result = "Even" if number % 2 == 0 else "Odd"

print("Example 2:", result)



#  Example 3: Maximum of two numbers
x = 10
y = 20

max_num = x if x > y else y

print("Example 3 (Max):", max_num)



#  Example 4: Grade system (nested ternary 🔥)
marks = 75

grade = "A" if marks >= 80 else "B" if marks >= 60 else "C"

print("Example 4 (Grade):", grade)