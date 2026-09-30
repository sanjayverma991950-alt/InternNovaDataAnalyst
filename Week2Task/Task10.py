import pandas as pd
import numpy as np

print("=" * 60)
print("       EMPLOYEE DATA ANALYSIS PROJECT")
print("=" * 60)

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("employee_dataset.csv")

print("\n1. DATASET")
print("-" * 60)
print(df)

# ==========================================
# 2. DATA INSPECTION
# ==========================================

print("\n2. DATA INSPECTION")
print("-" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# 3. CHECK MISSING VALUES
# ==========================================

print("\n3. MISSING VALUES")
print("-" * 60)

print(df.isnull().sum())

# ==========================================
# 4. HANDLE MISSING VALUES
# ==========================================

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# ==========================================
# 5. SELECTING DATA
# ==========================================

print("\n4. SELECTING DATA")
print("-" * 60)

selected_columns = df[
    ["Name", "Department", "Salary"]
]

print(selected_columns)

# ==========================================
# 6. FILTERING DATA
# ==========================================

print("\n5. FILTERING DATA")
print("-" * 60)

print("\nEmployees with Salary > 50000:")

high_salary = df[
    df["Salary"] > 50000
]

print(high_salary)

print("\nIT Employees:")

it_employees = df[
    df["Department"] == "IT"
]

print(it_employees)

print("\nIT Employees with Salary > 45000:")

it_high_salary = df[
    (df["Department"] == "IT") &
    (df["Salary"] > 45000)
]

print(it_high_salary)

# ==========================================
# 7. SORTING
# ==========================================

print("\n6. SORTING DATA")
print("-" * 60)

print("\nSalary - Ascending:")

salary_ascending = df.sort_values(
    by="Salary",
    ascending=True
)

print(salary_ascending)

print("\nSalary - Descending:")

salary_descending = df.sort_values(
    by="Salary",
    ascending=False
)

print(salary_descending)

# ==========================================
# 8. GROUPBY ANALYSIS
# ==========================================

print("\n7. GROUPBY ANALYSIS")
print("-" * 60)

department_analysis = df.groupby(
    "Department"
)["Salary"].agg(
    ["count", "sum", "mean", "min", "max"]
)

print(department_analysis)

# ==========================================
# 9. PIVOT TABLE
# ==========================================

print("\n8. PIVOT TABLE")
print("-" * 60)

pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc=["count", "mean", "sum", "min", "max"]
)

print(pivot)

# ==========================================
# 10. NUMPY ANALYSIS
# ==========================================

print("\n9. NUMPY ANALYSIS")
print("-" * 60)

salary_array = np.array(
    df["Salary"]
)

print("Salary Array:")
print(salary_array)

print("\nAverage Salary:")
print(np.mean(salary_array))

print("\nMedian Salary:")
print(np.median(salary_array))

print("\nMinimum Salary:")
print(np.min(salary_array))

print("\nMaximum Salary:")
print(np.max(salary_array))

print("\nSalary Standard Deviation:")
print(np.std(salary_array))

print("\nTotal Salary:")
print(np.sum(salary_array))

# ==========================================
# 11. ADD NEW COLUMN
# ==========================================

df["Annual_Salary"] = df["Salary"] * 12

print("\n10. ANNUAL SALARY")
print("-" * 60)

print(
    df[
        ["Name", "Department", "Salary", "Annual_Salary"]
    ]
)

# ==========================================
# 12. FIND INSIGHTS
# ==========================================

print("\n11. KEY INSIGHTS")
print("-" * 60)

highest_salary_employee = df.loc[
    df["Salary"].idxmax()
]

lowest_salary_employee = df.loc[
    df["Salary"].idxmin()
]

highest_avg_department = (
    df.groupby("Department")["Salary"]
    .mean()
    .idxmax()
)

highest_avg_salary = (
    df.groupby("Department")["Salary"]
    .mean()
    .max()
)

print(
    "Highest Paid Employee:",
    highest_salary_employee["Name"]
)

print(
    "Highest Salary:",
    highest_salary_employee["Salary"]
)

print(
    "Lowest Paid Employee:",
    lowest_salary_employee["Name"]
)

print(
    "Lowest Salary:",
    lowest_salary_employee["Salary"]
)

print(
    "Department with Highest Average Salary:",
    highest_avg_department
)

print(
    "Highest Department Average Salary:",
    highest_avg_salary
)

print(
    "Overall Average Salary:",
    df["Salary"].mean()
)

# ==========================================
# 13. EXPORT CLEANED DATASET
# ==========================================

output_file = "final_cleaned_employee_dataset.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n12. EXPORT")
print("-" * 60)

print(
    "Cleaned dataset exported successfully as:",
    output_file
)

# ==========================================
# 14. VERIFY EXPORTED DATA
# ==========================================

final_df = pd.read_csv(
    output_file
)

print("\nExported Dataset:")
print(final_df)

print("\nAnalysis Completed Successfully!")