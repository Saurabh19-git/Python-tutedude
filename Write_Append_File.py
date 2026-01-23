file_name = "output.txt"
user_input = input("Enter text to write to the file: ")
with open(file_name,"x") as f:
    f.write(user_input+"\n")
print(f"Data successfully written to {file_name}.")
print()

user_input2 = input("Enter additional text to append: ")
with open(file_name,"a") as f:
    f.write(user_input2)
print(f"Data successfully appended.")
print()

print(f"Final content of {file_name}:")

with open(file_name,"r") as f:
    print(f.read())

