# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates 


# #  Add / Update values
# car = {"brand": "Honda"}
# car["model"] = "Civic"   # new key add
# car["brand"] = "Toyota"  # update existing key

# print("Car Dictionary:", car)

# print("\n----------------\n")

# #  Loop through dictionary
# student = {"name": "Awais", "age": 20, "city": "Lahore"}

# for key in student:
#     print(key, "=", student[key])

# print("\n----------------\n")

# # Check if key exists
# data = {"username": "admin", "password": "1234"}

# if "email" in data:
#     print("Found")
# else:
#     print("Not Found")   # Corrected logic from your previous code

# print("\n----------------\n")

# #  Sum of values in dictionary
# marks = {"math": 80, "eng": 70, "cs": 90}

# total = 0
# for subject in marks:
#     total += marks[subject]

# print("Total marks:", total)

# print("\n----------------\n")

# #  Nested Dictionary
# students = {
#     "std1": {"name": "Ali", "marks": 80},
#     "std2": {"name": "Awais", "marks": 90}
# }

# print("Awais ke marks:", students["std2"]["marks"])

# print("\n----------------\n")

# #  Mini Login Logic
# users = {
#     "admin": "1234",
#     "awais": "pass123"
# }

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username in users and users[username] == password:
#     print("Login successful ✅")
# else:
#     print("Invalid credentials ❌")

# print("\n----------------\n")

# #  Dictionary meaning lookup
# words = {"apple": "fruit", "car": "vehicle"}

# word = input("Enter word to search: ")
# if word in words:
#     print(word, "means:", words[word])
# else:
#     print("Word not found ❌")

# print("\n----------------\n")

# # Swap keys and values
# data = {"a": 1, "b": 2, "c": 3}

# swapped = {}
# for key, value in data.items():
#     swapped[value] = key

# print("Swapped dictionary:", swapped)

# print("\n----------------\n")

# # Difference between mutable (list) and immutable (tuple) vs dict
# my_list = [1, 2, 3]
# my_list[0] = 100
# print("Updated List:", my_list)

# my_tuple = (1, 2, 3)
# # my_tuple[0] = 100  # ❌ Error: Tuple is immutable
# Day 3 - Dictionary
