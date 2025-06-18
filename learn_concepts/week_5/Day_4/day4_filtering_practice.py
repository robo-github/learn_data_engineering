import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Sneha", "Arun", "Priya", "Kiran"],
    "Subject": ["Math", "Science", "English", "History", "Math", "Science"],
    "Marks": [88, 76, 90, 67, 72, 59],
    "Passed": [True, True, True, True, True, False]
}

df = pd.DataFrame(data)

# Filter students with Marks less than 80
less_mark = df[df["Marks"] < 80]
print("\nStudents with Marks less than 80")
print(less_mark)

# Show students who are studying English
eng = df[df["Subject"] == "English"]
print("\nStudent who are studying in english")
print(eng)

# Show students who are studying Math or Science
sub = df[(df["Subject"] == "Maths") | (df["Subject"] == "Science")]
print("\nStudents who are studying Math or Science")
print(sub)

# Show students who passed and scored above 85
passed_student = df[(df["Passed"] == True) & (df["Marks"] > 85)]
print("\nStudents who passed and scored above 85")
print(passed_student)
