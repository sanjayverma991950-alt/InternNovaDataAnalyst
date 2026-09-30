import pandas as pd

# Read original dataset
df = pd.read_csv("employee_dataset.csv")

# Process the data
df["Annual_Salary"] = df["Salary"] * 12

# Sort by salary
df = df.sort_values(
    by="Salary",
    ascending=False
)

# Export final DataFrame
output_file = "processed_employee_dataset.csv"

df.to_csv(
    output_file,
    index=False
)

print("Processed DataFrame:")
print(df)

print("\nFile exported successfully:")
print(output_file)

# Verify exported file
verified_df = pd.read_csv(output_file)

print("\n--- Verified Exported Data ---")
print(verified_df)

print("\nShape of Exported Dataset:")
print(verified_df.shape)