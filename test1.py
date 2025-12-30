import os

# Ask the user for a number
n = int(input("Enter a number: "))

# First two numbers in the sequence
a = 0
b = 1

# Store the Fibonacci sequence in a string
result_text = "Fibonacci sequence:\n"

while a <= n:
    result_text += str(a) + "\n"
    temp = a
    a = b
    b = temp + b

# Print the result
print(result_text)

# Define the folder and file path
folder_path = r"/Users/jenniferalex/Desktop/Learn/python/ex_1"
file_path = os.path.join(folder_path, "test1_output.txt")

# Ensure folder exists
if not os.path.exists(folder_path):
	os.makedirs(folder_path)

# Write to the file
with open(file_path, "w") as file:
	file.write(result_text)
