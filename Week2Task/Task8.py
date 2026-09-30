import pandas as pd

# ------------------------------------------
# DATAFRAME 1
# ------------------------------------------

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Department": ["IT", "HR", "IT", "Finance", "Sales"]
})

# ------------------------------------------
# DATAFRAME 2
# ------------------------------------------

salary = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Salary": [45000, 52000, 48000, 60000, 55000],
    "Experience": [2, 4, 1, 6, 3]
})

print("--- Employees DataFrame ---")
print(employees)

print("\n--- Salary DataFrame ---")
print(salary)

# ==========================================
# MERGE
# ==========================================

merged_df = pd.merge(
    employees,
    salary,
    on="Employee_ID"
)

print("\n--- Merged DataFrame ---")
print(merged_df)

# ==========================================
# CONCATENATE
# ==========================================

new_employees = pd.DataFrame({
    "Employee_ID": [106, 107],
    "Name": ["Neha", "Vikas"],
    "Department": ["HR", "IT"]
})

concatenated_df = pd.concat(
    [employees, new_employees],
    ignore_index=True
)

print("\n--- Concatenated DataFrame ---")
print(concatenated_df)

# ==========================================
# GROUPBY
# ==========================================

print("\n--- GroupBy Department: Average Salary ---")

grouped_mean = merged_df.groupby(
    "Department"
)["Salary"].mean()

print(grouped_mean)

# Sum of salaries
print("\n--- GroupBy Department: Total Salary ---")

grouped_sum = merged_df.groupby(
    "Department"
)["Salary"].sum()

print(grouped_sum)

# Count employees
print("\n--- GroupBy Department: Employee Count ---")

grouped_count = merged_df.groupby(
    "Department"
)["Employee_ID"].count()

print(grouped_count)

# Multiple aggregate functions
print("\n--- Multiple Aggregate Functions ---")

grouped_agg = merged_df.groupby(
    "Department"
)["Salary"].agg(
    ["sum", "mean", "min", "max", "count"]
)

print(grouped_agg)

# ==========================================
# PIVOT TABLE
# ==========================================

print("\n--- Pivot Table ---")

pivot_table = pd.pivot_table(
    merged_df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print(pivot_table)

# Pivot table with multiple values
print("\n--- Detailed Pivot Table ---")

pivot_detailed = pd.pivot_table(
    merged_df,
    values=["Salary", "Experience"],
    index="Department",
    aggfunc="mean"
)

print(pivot_detailed)