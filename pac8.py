
# 1. Create input.txt
with open("input.txt", "w") as file:
    file.write("Hello, my name is Jivika.\n")
    file.write("I am a computer science student.\n")
    file.write("I am learning Python.\n")
    file.write("Python is easy to learn.\n")

# 2. Read the file
with open("input.txt", "r") as file:
    lines = file.readlines()

# 3. Count total lines
line_count = len(lines)
print("Total number of lines:", line_count)

# 4. Get first two lines
first_two_lines = lines[:2]

print("\nFirst two lines:")
for line in first_two_lines:
    print(line.strip())

# 5. Write first two lines into output.txt
with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("\nFirst two lines written to output.txt successfully!")

