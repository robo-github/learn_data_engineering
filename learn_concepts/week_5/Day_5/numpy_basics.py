import numpy as np

arr = np.array([55, 78, 90, 45, 62, 33, 100])

# print all marks
print("All marks:")
print(arr)

# Top 3 marks (sorted)
print("\nTop 3 marks: ")
sort_data = np.sort(arr)
reverse_data = sort_data[::-1]
top3 = reverse_data[0:3]
print(top3)

# Count how many passed (marks >= 40)
print("\nPassed students: ")
your_array = (arr >= 40).sum()
print(your_array)

# Average marks
print("\nAverage Marks: ")
print(round(np.mean(arr)))

# Highest mark
print("\nHighest mark: ")
print(np.max(arr))

# Lowest mark
print("\nLowest mark: ")
print(np.min(arr))
