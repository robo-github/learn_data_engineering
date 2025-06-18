import pandas as pd

datadata = {
    "Name": ["Anand", "Ravi", "Sneha", "Divya", "Arjun", "Neha", "Asha"],
    "Marks": [75, 89, 92, 68, 55, 80, 92],
    "Subject": ["Math", "Science", "Math", "English", "Science", "Math", "English"],
    "Passed": [True, True, True, False, False, True, True]
}

df = pd.DataFrame(datadata)

# Show students who passed and scored more than 70 marks.
high_score = df[(df["Passed"] == True) & (df["Marks"] > 70)]
print("Student grater than 70  marks:")
print(high_score)

# Sort all students by their marks from highest to lowest.
sort_mark = df.sort_values(by="Marks", ascending=False)
print("\nStudent and there marks:")
print(sort_mark)

# Group students by their subject and show the average marks per subject.
average_mark = df.groupby("Subject")["Marks"].mean()
print("\nAverage mark of the students:")
print(average_mark)

# Group students who passed and count how many passed in each subject.
passed_df = df[df["Passed"] == True]
count_student = passed_df.groupby("Subject")["Name"].count()
print("\nNumber of passed students per subject:")
print(count_student)
