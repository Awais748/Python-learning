#  format specifiers = {value:flags} format a value based on what flags are inserted

# 1. Float formatting
price = 123.4567
print("Price (2 decimal):", f"{price:.2f}")

# 2. Alignment
name = "Awais"
print("Left:", f"{name:<10}")
print("Right:", f"{name:>10}")
print("Center:", f"{name:^10}")

# 3. Zero padding
num = 9
print("Zero padded:", f"{num:03}")

# 4. Large number formatting
salary = 1500000
print("Formatted salary:", f"{salary:,}")

# 5. Percentage
score = 0.89
print("Percentage:", f"{score:.1%}")

# 6. Mixed example
item = "Laptop"
price = 999.99

print(f"Item: {item:<10} Price: {price:>8.2f}")# Day 2 - Format Specifiers
