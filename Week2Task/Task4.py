import pandas as pd

# Create a Pandas Series
marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)

# Create DataFrame
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 92, 88],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display index
print("\nIndex:")
print(df.index)

# Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nUpdated DataFrame:")
print(df)