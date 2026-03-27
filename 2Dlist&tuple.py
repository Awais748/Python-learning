# 🔹 2D LIST EXAMPLES

# Example 1: Basic Matrix
matrix = [
    [5, 6],
    [7, 8]
]

print("First row:", matrix[0])        # [5, 6]
print("Specific value:", matrix[1][1])  # 8


# Example 2: Loop through 2D List
print("\nAll elements in matrix:")
for row in matrix:
    for item in row:
        print(item)


# Example 3: Sum of all elements
total = 0
for row in matrix:
    for item in row:
        total += item

print("\nTotal of all elements:", total)


# 🔹 TUPLE EXAMPLES

# Example 1: Simple Tuple
numbers = (1, 2, 3, 4)
print("\nFirst element of tuple:", numbers[0])


# Example 2: 2D Tuple (Nested Tuple)
tuple_matrix = (
    (10, 20),
    (30, 40)
)

print("First row of tuple:", tuple_matrix[0])      # (10, 20)
print("Specific value:", tuple_matrix[1][1])       # 40


# Example 3: Loop through Tuple
print("\nAll elements in tuple_matrix:")
for row in tuple_matrix:
    for item in row:
        print(item)


# 🔹 DIFFERENCE

# List → change ho sakti hai (mutable)
my_list = [1, 2, 3]
my_list[0] = 100
print("\nUpdated list:", my_list)

# Tuple → change nahi hoti (immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 100  ❌ error dega