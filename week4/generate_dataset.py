"""
Generate Realistic E-Commerce Customer & Sales Analytics Dataset
for InternNova Week 4 Assignment: Statistics, Data Visualization & EDA.
"""
import numpy as np
import pandas as pd
import os

# Set seed for reproducibility
np.random.seed(42)
n_records = 600

# 1. Base transaction data
txn_ids = [f"TXN{1000 + i}" for i in range(1, n_records + 1)]
start_date = pd.to_datetime("2024-01-01")
dates = [start_date + pd.Timedelta(days=int(d)) for d in np.random.randint(0, 365, size=n_records)]

categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Books', 'Beauty & Health']
category_weights = [0.28, 0.26, 0.20, 0.14, 0.12]
assigned_categories = np.random.choice(categories, size=n_records, p=category_weights)

regions = ['North', 'South', 'East', 'West']
region_weights = [0.32, 0.28, 0.22, 0.18]
assigned_regions = np.random.choice(regions, size=n_records, p=region_weights)

payment_methods = ['Credit Card', 'UPI', 'Debit Card', 'Cash on Delivery']
payment_weights = [0.35, 0.35, 0.18, 0.12]
assigned_payments = np.random.choice(payment_methods, size=n_records, p=payment_weights)

genders = ['Female', 'Male', 'Other']
gender_weights = [0.49, 0.48, 0.03]
assigned_genders = np.random.choice(genders, size=n_records, p=gender_weights)

# Age: Mean ~ 35, std ~ 11, bounded 18 to 70
ages = np.clip(np.random.normal(loc=35, scale=11, size=n_records).round(), 18, 70).astype(int)

# Unit prices by category
cat_price_mean = {
    'Electronics': 280,
    'Fashion': 65,
    'Home & Kitchen': 110,
    'Books': 25,
    'Beauty & Health': 45
}
cat_price_std = {
    'Electronics': 90,
    'Fashion': 25,
    'Home & Kitchen': 40,
    'Books': 10,
    'Beauty & Health': 15
}

unit_prices = []
quantities = []
discounts = []
profits = []
sales_amounts = []

for i in range(n_records):
    cat = assigned_categories[i]
    price = round(max(10, np.random.normal(cat_price_mean[cat], cat_price_std[cat])), 2)
    qty = int(np.random.choice([1, 2, 3, 4, 5, 6], p=[0.42, 0.28, 0.14, 0.08, 0.05, 0.03]))
    
    # Discount: correlated with quantity & promotions (0 to 30%)
    discount = round(float(np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], 
                                           p=[0.25, 0.20, 0.22, 0.15, 0.10, 0.05, 0.03])), 2)
    
    gross_sales = round(price * qty, 2)
    net_sales = round(gross_sales * (1 - discount), 2)
    
    # Base margin varies by category (Books/Fashion ~ 35%, Electronics ~ 18%)
    base_margin = {'Electronics': 0.22, 'Fashion': 0.42, 'Home & Kitchen': 0.32, 'Books': 0.38, 'Beauty & Health': 0.40}[cat]
    cost = round(price * qty * (1 - base_margin), 2)
    profit = round(net_sales - cost, 2)
    
    unit_prices.append(price)
    quantities.append(qty)
    discounts.append(int(discount * 100))
    sales_amounts.append(net_sales)
    profits.append(profit)

# Ratings: 1 to 5, skewed towards 4 and 5
ratings = np.random.choice([1.0, 2.0, 3.0, 4.0, 5.0], size=n_records, p=[0.05, 0.08, 0.18, 0.39, 0.30])

# Add 6 high-value / anomalous outliers for demonstration in Task 4
outlier_indices = [45, 112, 230, 345, 410, 520]
for idx in outlier_indices:
    quantities[idx] = 15  # bulk order
    sales_amounts[idx] = round(unit_prices[idx] * quantities[idx] * (1 - discounts[idx]/100), 2) + 1200
    profits[idx] = round(sales_amounts[idx] * 0.35, 2)

# Build Cleaned DataFrame
df_clean = pd.DataFrame({
    'Transaction_ID': txn_ids,
    'Date': dates,
    'Customer_Age': ages,
    'Gender': assigned_genders,
    'Product_Category': assigned_categories,
    'Quantity': quantities,
    'Unit_Price': unit_prices,
    'Discount_Percent': discounts,
    'Sales_Amount': sales_amounts,
    'Profit': profits,
    'Payment_Method': assigned_payments,
    'Region': assigned_regions,
    'Customer_Rating': ratings
})

# Save cleaned dataset
clean_csv_path = os.path.join(os.path.dirname(__file__), 'data', 'ecommerce_sales_cleaned.csv')
df_clean.to_csv(clean_csv_path, index=False)
print(f"Clean dataset saved to: {clean_csv_path} (Shape: {df_clean.shape})")

# Build Raw DataFrame with intentional flaws for Task 7:
# 1. Missing values in Customer_Age (18 rows) and Customer_Rating (15 rows)
# 2. Duplicate records (8 duplicate rows appended)
# 3. Inconsistent categorical labels (e.g., 'electronics', 'ELECTRONICS', 'fashion')
# 4. Inconsistent negative/zero quantity (3 rows)
df_raw = df_clean.copy()

# Add missing values
nan_age_idx = np.random.choice(n_records, size=18, replace=False)
nan_rating_idx = np.random.choice(n_records, size=15, replace=False)
df_raw.loc[nan_age_idx, 'Customer_Age'] = np.nan
df_raw.loc[nan_rating_idx, 'Customer_Rating'] = np.nan

# Inconsistent text casing
casing_idx = np.random.choice(n_records, size=12, replace=False)
for idx in casing_idx[:6]:
    df_raw.loc[idx, 'Product_Category'] = df_raw.loc[idx, 'Product_Category'].lower()
for idx in casing_idx[6:]:
    df_raw.loc[idx, 'Product_Category'] = df_raw.loc[idx, 'Product_Category'].upper()

# Inconsistent quantity values
err_qty_idx = [12, 88, 195]
df_raw.loc[err_qty_idx[0], 'Quantity'] = -1
df_raw.loc[err_qty_idx[1], 'Quantity'] = 0
df_raw.loc[err_qty_idx[2], 'Quantity'] = -2

# Add duplicate rows
duplicates = df_raw.iloc[10:18].copy()
df_raw = pd.concat([df_raw, duplicates], ignore_index=True)

raw_csv_path = os.path.join(os.path.dirname(__file__), 'data', 'ecommerce_sales_raw.csv')
df_raw.to_csv(raw_csv_path, index=False)
print(f"Raw dataset saved to: {raw_csv_path} (Shape: {df_raw.shape})")
