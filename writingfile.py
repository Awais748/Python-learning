# Python writing files (.txt , .json, .csv)


file = open("example1.txt", "w")   

file.write("Hello, this is my first file.\n")
file.write("I am learning file handling in Python.")

file.close()

print("Data written successfully!")