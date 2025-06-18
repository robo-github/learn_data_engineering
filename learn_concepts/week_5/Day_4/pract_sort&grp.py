import pandas as pd

data = {
    "Name": ["Anand", "Ravi", "Sneha", "Divya"],
    "Marks": [75, 89, 92, 68],
    "Subject": ["Math", "Science", "Math", "English"]
}

df = pd.DataFrame(data)

# Sort students by marks in ascending order.
sort_student = df.sort_values(by="Marks", ascending=True)
print("Sort students by marks in ascending order:")
print(sort_student)

# Group students by subject and show average marks.
average_mark = df.groupby("Subject")["Marks"].mean()
print("\nAverage marks of students:")
print(average_mark)

# Group students by subject and count how many students per subject.
student_count = df.groupby("Subject")["Name"].count()
print("\nNumber of students per subject:")
print(student_count)
