import pandas as pd

df = pd.read_csv("students.csv")

# Show first few rows
print("First 5 row of data :")
print(df.head())
print()

# Show Last few rows
print("Last few row of data :")
print(df.tail())
print()

# Show summary info (column types, missing values)
print("Info about the data :")
print(df.info())
print()

# Show statistics for numeric columns
print("Statistics :")
print(df.describe())
print()

# Show all student names
print("All students name :")
print(df["Name"])
print()

# Show only students who passed (Marks >= 40)
print("Passed student (Marks >= 40) :")
passed = df[df["Marks"] >= 40]
print(f"Total passed student = {passed.count()}")
print(passed)
print()

# Show only student who failed (marks < 40)
print("Failed students (marks < 40) :")
failed = df[df["Marks"] < 40]
print(failed)
print(f"Total failed student = {failed.count()}")
print()

print("Unique Grade")
print(df["Grade"].unique())
