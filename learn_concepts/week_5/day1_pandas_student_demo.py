import pandas as pd

# Step 1: Create a dictionary
student_data = {
    "Name": ["Asha", "Ravi", "Sneha", "Arun"],
    "Subject": ["Math", "Science", "English", "History"],
    "Marks": [88, 76, 90, 67],
    "Passed": [True, True, True, True]
}

# Step 2: Convert it to a DataFrame
df = pd.DataFrame(student_data)

# Step 3: Print:
# a) The 'Marks' column
print(df["Marks"])
# b) The 2nd row using iloc
print(df.iloc[1])
