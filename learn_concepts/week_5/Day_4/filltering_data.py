import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Sneha", "Arun"],
    "Marks": [88, 76, 90, 67],
    "Subject": ["Math", "Science", "English", "History"]
}

df = pd.DataFrame(data)
# Filter: Students who scored more than 75
high_score = df[df["Marks"] > 75]

print("Students with Marks > 75:")
print(high_score)
