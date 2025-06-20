import numpy as np

# Creating a 1D array (like a list)
#    index        0   1   2   3    4
array = np.array([10, 20, 30, 40, 50])
print(array)
print()

# 2D Array (Matrix)
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
print()

# slicing a numpy array
print(array[0])    # prints the first element
print(array[-1])   # prints the last element
print(array[1:4])  # prints elements from index 1 to 4 (excluding 4)
