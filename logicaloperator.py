# LOGICAL OPERATORS IN PYTHON (and, or, not)
# Logical operators are used to combine conditional statements
# They return True or False based on conditions

# 1. AND OPERATOR

# Definition:
# "and" returns True only if BOTH conditions are True

# Example 1
age = 20
has_id = True

if age >= 20 and has_id:
    print("Example 1: You can enter the club.")
else:
    print("Example 1: You cannot enter the club.")

# Example 2
marks = 85
attendance = 75

if marks >= 50 and attendance >= 70:
    print("Example 2: You passed the exam.")
else:
    print("Example 2: You failed the exam.")

# 2. OR OPERATOR

# Definition:
# "or" returns True if at least ONE condition is True

# Example 1
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Example 1: You can relax today.")
else:
    print("Example 1: You have to work.")

# Example 2
temperature = 35
is_raining = False

if temperature > 30 or is_raining:
    print("Example 2: Stay at home.")
else:
    print("Example 2: You can go outside.")

# 3. NOT OPERATOR

# Definition:
# "not" reverses the condition (True -> False, False -> True)


# Example 1
is_logged_in = False

if not is_logged_in:
    print("Example 1: Please log in first.")
else:
    print("Example 1: Welcome back!")


# Example 2
is_raining = True

if not is_raining:
    print("Example 2: Go outside and enjoy.")
else:
    print("Example 2: Stay inside.")# Day 2 - Logical Operators
