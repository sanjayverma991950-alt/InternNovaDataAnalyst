import pandas as pd

# Create sample CSV dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Rahul", "Priya", "Amit", "Sneha", "Rohan",
        "Neha", "Vikas", "Anjali", "Karan", "Pooja"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", "Sales",
        "HR", "IT", "Finance", "Sales", "IT"
    ],
    "Age": [25, 28, 24, 30, 27, 29, 26, 31, 28, 25],
    "Salary": [
        45000, 52000, 48000, 60000, 55000,
        50000, 47000, 65000, 58000, 49000
    ],
    "Experience": [2, 4, 1, 6, 3, 5, 2, 7, 4, 2]
}

employee_df = pd.DataFrame(data)

# Save dataset to CSV
employee_df.to_csv("employee_dataset.csv", index=False)

print("CSV file created successfully.")

# Read CSV file
df = pd.read_csv("employee_dataset.csv")

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Last 5 Rows ---")
print(df.tail())

# Number of rows and columns
print("\n--- Shape ---")
print(df.shape)

# Column names
print("\n--- Column Names ---")
print(df.columns)

# Data types
print("\n--- Data Types ---")
print(df.dtypes)

# Information
print("\n--- Dataset Information ---")
df.info()

# Statistical description
print("\n--- Statistical Description ---")
print(df.describe())