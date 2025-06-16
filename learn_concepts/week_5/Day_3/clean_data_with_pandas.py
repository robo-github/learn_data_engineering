import pandas as pd

df = pd.read_csv("students_dirty.csv")
print("Row data")
print(df)
print()

print(df.columns)

# Fix spaces in column names (like " marks ")
df_columns = df.columns.str.strip()
print(df_columns)
print()

# Find the missing value in data
print("Find values (NaNs):")
print(df.isnull())
print()
print("\n count of missing value in each column:")
print(df.isnull().sum())
