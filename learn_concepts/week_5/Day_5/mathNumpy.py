import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # Output: [5 7 9]
print(a * b)   # Output: [ 4 10 18]
print(a ** b)  # Output: [  1  32 729]


print(np.mean(b))  # Output: 5.0 Average
print(np.max(a))   # Output: 3 Maximum
