import pandas as pd

# Read dataset
df = pd.read_csv("employee_dataset.csv")

print("Original DataFrame:")
print(df)

# Select specific columns
print("\n--- Selected Columns ---")
print(df[["Name", "Department", "Salary"]])

# Select specific rows
print("\n--- Selected Rows ---")
print(df.iloc[0:5])

# Filter records based on one condition
print("\n--- Employees with Salary > 50000 ---")
high_salary = df[df["Salary"] > 50000]
print(high_salary)

# Multiple filtering conditions
print("\n--- IT Employees with Salary > 45000 ---")

filtered = df[
    (df["Department"] == "IT") &
    (df["Salary"] > 45000)
]

print(filtered)

# Another multiple condition
print("\n--- Employees with Age < 30 and Experience >= 3 ---")

filtered2 = df[
    (df["Age"] < 30) &
    (df["Experience"] >= 3)
]

print(filtered2)

# Sort ascending
print("\n--- Salary Sorted Ascending ---")
ascending = df.sort_values(by="Salary", ascending=True)
print(ascending)

# Sort descending
print("\n--- Salary Sorted Descending ---")
descending = df.sort_values(by="Salary", ascending=False)
print(descending)