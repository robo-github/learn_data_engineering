import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Sneha", "Arun"],
    "Marks": [88, None, 90, None]
}

df = pd.DataFrame(data)

print("\nBefore cleaning data:")
print(df)
print()

average_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(average_marks)
print("✅ After filling missing values with average:")
print(df)
print()

df = df.rename(columns={
    "Name": "Student Name",
    "Marks": "Students Marks"
})

print("✅ After renaming columns:")
print(df)
