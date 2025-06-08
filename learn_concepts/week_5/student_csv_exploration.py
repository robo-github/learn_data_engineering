import pandas as pd

df = pd.read_csv("students2.csv")

# first row of data
print("First 5 row of data L :")
print(df.head())
print()

# info of data
print("Info about this data :")
print(df.info())
print()

# statistics
print("Statistics")
print(df.describe())
print()

# Name of the students
print("Name of the students in the data : ")
print(df["Name"])
print()

# students of mark > 70
print("Students of mark > 70")
print(df[df["Marks"] >= 70])
