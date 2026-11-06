
import csv
import json

# 1. Create CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["id", "name", "department", "marks"])
    writer.writerow([101, "Soham", "CSE", 90])
    writer.writerow([102, "Sarvadnya", "IT", 85])
    writer.writerow([103, "Aman", "ECE", 88])
    writer.writerow([104, "Pranav", "CSE", 92])

# 2. Read CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# 3. Convert values into integers
for student in data:
    student["id"] = int(student["id"])
    student["marks"] = int(student["marks"])

# 4. Convert CSV data into JSON
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print("CSV data successfully converted to JSON.")




