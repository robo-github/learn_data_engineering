import pandas as pd

data = {
    "Name": ["Anand", "John", "Karthik", "Manu"],
    "Marks": [50, 60, 50, 40],
    "City": ["Kozhikode", "Bangaluru", "Karnataka", "Mysore"]
}


df = pd.DataFrame(data)

print(df["City"])
print()
print(df.iloc[0])
print()
print(df.loc[3])
print()
print(df.loc[3, "Name"])
