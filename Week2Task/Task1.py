import numpy as np

# Create a NumPy array containing at least 10 numbers
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:")
print(arr)

# Display shape
print("\nShape of Array:")
print(arr.shape)

# Display size
print("\nSize of Array:")
print(arr.size)

# Display data type
print("\nData Type of Array:")
print(arr.dtype)

# Create a one-dimensional array
one_d = np.array([1, 2, 3, 4, 5])

print("\nOne-Dimensional Array:")
print(one_d)

# Create a two-dimensional array
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nTwo-Dimensional Array:")
print(two_d)

print("\nShape of 2D Array:")
print(two_d.shape)