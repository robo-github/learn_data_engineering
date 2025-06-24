import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'data', 'students6.csv')


df = pd.read_csv(csv_path)

print(df.head())

print(df.info())
print(df.shape)

# Sorting students by data
sorting_data = df.sort_values(by='Name', ascending=True)
print("\n Students sorted data")
print(sorting_data)

# show subject wise average
sub_wise_average = df.groupby(
    ["Subject"])["Marks"].mean()
print("\n Subject wise average")
print(sub_wise_average)

# students who failed less than 40
student_failed = df[df["Marks"] < 40]
print("\n Students who failed less than 40")
print(student_failed)

# Top score of mark
top_score = df["Marks"].max()
print("\n Top score of mark : ", top_score)
