import pandas as pd

# Sample data
data = {
    "Name": ["Anand", "Ravi", "Sneha", "Divya"],
    "Marks": [75, 89, 92, 68],
    "Subject": ["Math", "Science", "Math", "English"]
}


df = pd.DataFrame(data)

sorting_df = df.sort_values(by="Name", ascending=True)
print(sorting_df)
print()

average_marks = df.groupby("Subject")["Marks"].mean()
print(average_marks)
