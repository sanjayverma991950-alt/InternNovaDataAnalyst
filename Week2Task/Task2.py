import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original Array:")
print(arr)

# Access specific elements using indexing
print("\nFirst Element:")
print(arr[0])

print("\nFourth Element:")
print(arr[3])

print("\nLast Element:")
print(arr[-1])

# Slicing
print("\nElements from index 2 to 5:")
print(arr[2:6])

print("\nFirst five elements:")
print(arr[:5])

print("\nElements from index 3 onwards:")
print(arr[3:])

# Create a 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nTwo-Dimensional Array:")
print(matrix)

# Access specific rows
print("\nFirst Row:")
print(matrix[0])

print("\nSecond Row:")
print(matrix[1])

# Access specific columns
print("\nFirst Column:")
print(matrix[:, 0])

print("\nSecond Column:")
print(matrix[:, 1])

# Access a specific element
print("\nElement at Row 2, Column 3:")
print(matrix[1, 2])

# Reshaping
original = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("\nOriginal Array for Reshaping:")
print(original)

reshaped_3x4 = original.reshape(3, 4)

print("\nReshaped into 3 x 4:")
print(reshaped_3x4)

reshaped_4x3 = original.reshape(4, 3)

print("\nReshaped into 4 x 3:")
print(reshaped_4x3)