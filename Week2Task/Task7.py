import pandas as pd
import numpy as np

# Create dataset containing missing values
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan", "Neha"],
    "Age": [20, 21, np.nan, 22, 21, np.nan],
    "Marks": [85, np.nan, 78, 92, np.nan, 88],
    "Department": ["CSE", "IT", "CSE", np.nan, "IT", "CSE"]
}

df = pd.DataFrame(data)

print("--- Dataset Before Handling Missing Values ---")
print(df)

# Identify missing values
print("\n--- Missing Values using isnull() ---")
print(df.isnull())

# Count missing values in each column
print("\n--- Missing Value Count ---")
print(df.isnull().sum())

# Remove rows containing missing values
df_dropped = df.dropna()

print("\n--- After Removing Rows with Missing Values ---")
print(df_dropped)

# Fill missing values
df_filled = df.copy()

# Fill Age with mean age
df_filled["Age"] = df_filled["Age"].fillna(
    df_filled["Age"].mean()
)

# Fill Marks with mean marks
df_filled["Marks"] = df_filled["Marks"].fillna(
    df_filled["Marks"].mean()
)

# Fill Department with mode
df_filled["Department"] = df_filled["Department"].fillna(
    df_filled["Department"].mode()[0]
)

print("\n--- After Filling Missing Values ---")
print(df_filled)

# Check again
print("\n--- Missing Values After Cleaning ---")
print(df_filled.isnull().sum())