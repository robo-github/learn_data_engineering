import numpy as np

marks = np.array([55, 78, 90, 45, 62, 33, 100])

print("Order the array", np.sort(marks))

print("Mean:", np.mean(marks))  # ➕ Adds all values, ➗ divides by total count.

print("Median:", np.median(marks))  # Sorts data, picks the middle value.

# Measures how spread out the numbers are from the mean.
print("Standard Deviation:", np.std(marks))

# Variance is just std squared. Variance is just std squared.
print("Variance:", np.var(marks))

print("Min:", np.min(marks))  # Finds the smallest value in the array.

print("Max:", np.max(marks))  # Finds the largest value in the array.
