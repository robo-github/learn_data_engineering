import csv

try:
    with open("student.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            marks = row[1]
            print(f"Name : {name} Marks : {marks}")
except FileNotFoundError:
    print("FileNotFoundError: No student data available.")
except Exception:
    print("Something wrong while reading the file.")
