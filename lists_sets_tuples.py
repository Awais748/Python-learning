# collection = single "variable" user to store multiple values
#    list = [] ordered and changeable. Duplicates OK
#    Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates Ok. FASTER



# PYTHON LISTS - COMPLETE EXAMPLES

# 1. Creating a List
# my_list = [1, 2, 3, 4, 5]
# print("List:", my_list)


#  2. Mixed Data Types
# mixed = [1, "Awais", 3.5, True]
# print("Mixed List:", mixed)


# # 3. Accessing Elements
# numbers = [10, 20, 30, 40]
# print("First Element:", numbers[0])
# print("Last Element:", numbers[-1])


# # 4. Slicing
# nums = [1, 2, 3, 4, 5]
# print("Slicing (1:4):", nums[1:4])


# # 5. Modify List
# nums[0] = 100
# print("After Modification:", nums)


# # 6. Add Elements
# nums.append(6)        # add at end
# nums.insert(1, 50)    # add at specific index
# print("After Adding:", nums)


# # 7. Remove Elements
# nums.remove(3)   # remove specific value
# nums.pop()       # remove last element
# print("After Removing:", nums)


# # 8. Loop Through List
# print("Looping:")
# for item in nums:
#     print(item)


# # 9. List Length
# print("Length:", len(nums))


# # 10. Nested List (2D List)
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print("Matrix Element [0][1]:", matrix[0][1])


# # 11. List Comprehension
# squares = [x**2 for x in range(5)]
# print("Squares:", squares)


# 12. Sorting
# nums2 = [5, 2, 9, 1]
# nums2.sort()
# print("Sorted:", nums2)


# 13. Reverse
# nums2.reverse()
# print("Reversed:", nums2)


# # 14. Copy List
# copy_list = nums2.copy()
# print("Copy:", copy_list)


# # 15. Clear List
# nums2.clear()
# print("After Clear:", nums2)


# End List

# PYTHON SETS - COMPLETE EXAMPLES

# 1. Creating a Set
# my_set = {1, 2, 3, 4, 5}
# print("Set:", my_set)


#  2. Duplicate Values (Automatically Removed)
# dup_set = {1, 2, 2, 3, 3, 4}
# print("No Duplicates:", dup_set)


# 3. Mixed Data Types
# mixed = {1, "Awais", 3.5, True}
# print("Mixed Set:", mixed)


# 4. Empty Set (Important ⚠️)
# empty_set = set()# {} is NOT empty set, it's a dictionary
# print("Empty Set:", empty_set)


#  5. Adding Elements
# my_set.add(6)
# print("After Add:", my_set)


#  6. Adding Multiple Elements
# my_set.update([10,11,1001,7, 8, 9])
# print("After Update:", my_set)


#  7. Removing Elements
# my_set.remove(2)   # error if not found
# print("After Remove:", my_set)

# my_set.discard(100)  # no error if not found
# print("After Discard:", my_set)

# my_set.pop()   # removes random element
# print("After Pop:", my_set)


# # 8. Loop Through Set
# print("Looping:")
# for item in my_set:
#     print(item)


# # 9. Set Length
# print("Length:", len(my_set))


# # 10. Set Operations
# a = {1, 2, 3}
# b = {3, 4, 5}

# print("Union:", a | b)          # {1,2,3,4,5}
# print("Intersection:", a & b)  # {3}
# print("Difference:", a - b)    # {1,2}
# print("Symmetric Diff:", a ^ b) # {1,2,4,5}


# # 11. Using Methods
# print("Union Method:", a.union(b))
# print("Intersection Method:", a.intersection(b))


# # 12. Check Membership
# print("Is 2 in set?", 2 in a)


# # 13. Copy Set 
# copy_set = a.copy()
# print("Copy:", copy_set)


# # 14. Clear Set
# a.clear()
# print("After Clear:", a)


# ===============================
# IMPORTANT NOTES
# ===============================
# - Sets are unordered ❗
# - No duplicate values allowed ❗
# - No indexing (you can't use set[0]) ❗

# End Set



# ===================================
# Python Tuples Complete Guide (English)
# ===================================

# 1. What is a Tuple?
# A tuple is an ordered, immutable sequence in Python.
# Immutable means you cannot change its items after creation.

# Example:
# my_tuple = (1, 2, 3, 4)
# print("Tuple:", my_tuple)

# # 2. Single item tuple
# single_item_tuple = (5,)  # comma is necessary
# print("Single item tuple:", single_item_tuple)

# 3. Tuple with different data types
# mixed_tuple = (1, "hello", 3.14, True)
# print("Mixed tuple:", mixed_tuple)

# # 4. Accessing items (indexing)
# print("First item:", my_tuple[0])
# print("Last item:", my_tuple[-1])

# # 5. Slicing
# print("Slice 1 to 3:", my_tuple[1:3])
# print("Full slice:", my_tuple[:])

# # 6. Length of a tuple
# print("Length of tuple:", len(my_tuple))

# # 7. Tuples are immutable
# # my_tuple[0] = 10  # This will give an error

# # 8. Loop through a tuple
# for item in my_tuple:
#     print("Item:", item)

# # 9. Tuple methods
# # count() - counts occurrences of a value
# # index() - finds index of first occurrence

# numbers = (1, 2, 3, 2, 4, 2)
# print("Count of 2:", numbers.count(2))
# print("Index of 3:", numbers.index(3))

# # 10. Tuple packing & unpacking
# # Packing
# person = ("Awais", 18, "Student")
# print("Packed tuple:", person)

# # Unpacking
# name, age, role = person
# print("Name:", name)
# print("Age:", age)
# print("Role:", role)

# # 11. Nested tuples
# nested = ((1, 2), (3, 4))
# print("Nested tuple:", nested)
# print("Nested item:", nested[0][1])  # Output: 2

# # 12. Tuple vs List
# # Tuple is immutable, list is mutable
# my_list = [1, 2, 3]
# my_list[0] = 10  # Allowed
# print("Modified list:", my_list)

# # 13. Tuple operations
# a = (1, 2)
# b = (3, 4)
# c = a + b  # Concatenation
# print("Concatenated tuple:", c)

# d = a * 3  # Repetition
# print("Repeated tuple:", d)

# # 14. Check item existence
# print("Is 2 in tuple?", 2 in a)
# print("Is 5 not in tuple?", 5 not in a)

# # 15. Converting between list and tuple
# list_to_tuple = tuple([1, 2, 3])
# tuple_to_list = list(a)
# print("List to tuple:", list_to_tuple)
# print("Tuple to list:", tuple_to_list)

# ===================================
# Tuples Summary:
# - Ordered
# - Immutable
# - Can store multiple types
# - Support indexing, slicing, loops
# - Use tuple() to convert list -> tuple
# - Packing & unpacking possible
# ===================================