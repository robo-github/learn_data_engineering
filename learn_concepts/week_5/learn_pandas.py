import pandas as pd

# About the pandas Series

data = [10, 20, 30, 40, 50]

dt = pd.Series(data, index=[1, 2, 3, 4, 5])
print(dt)

print()

# About the dataframe

data = {
    "Name": ["Anand", "John", "Manu",],
    "Marks": [10, 40, 50]
}

df = pd.DataFrame(data)
print(df)
print()
# Printing the data

print(df["Name"])
print()
print(df.iloc[0])
print()
print(df.loc[0])
