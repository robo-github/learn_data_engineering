import pandas as pd

data = {
    "Name": ["Anand", "Ravi", "Sneha", None],
    "Marks": [85, None, 75, 90],
    "City": ["Kozhikode", "Bangalore", None, "Mysore"]
}

df = pd.DataFrame(data)
print("Before cleaning data :")
print(df)

# Finding  missing values in each column
print("\nMissing value in each column:")
print(df.isnull().sum())
print()

average = df["Marks"].mean()  # Filling missing value
df["Marks"] = df["Marks"].fillna(average)
print("\nAfter filling missing value: ")
print(df)

df["Name"] = df["Name"].fillna("unknown")  # Set the null names to Unknown
print(df)
df["Name"] = df["Name"].fillna[3]("Babu")
print(df)

# Rename one ore more columns
df = df.rename(columns={"Name": "Student Names", "Marks": "Students Marks"})
print("\nAfter rename the columns: ")
print(df)
# Alternate Way (rename all at once with order):
df.columns = ["Names", "Marks", "City"]
print(df)
