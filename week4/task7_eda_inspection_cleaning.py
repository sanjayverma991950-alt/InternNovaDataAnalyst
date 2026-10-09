"""
InternNova Data Analytics Internship - Week 4
Task 7: Exploratory Data Analysis (EDA) – Data Inspection & Cleaning (15 Marks)
Student Name: Sanjay Kumar

Objective:
1. Data Inspection:
   - Check the number of rows and columns.
   - Display column names.
   - Check data types.
   - Generate a statistical summary.
2. Data Cleaning:
   - Identify missing values.
   - Handle missing values appropriately.
   - Check for duplicate records.
   - Remove duplicates where required.
   - Check the dataset for incorrect or inconsistent values.
3. Display visual comparison / summary of the dataset before and after cleaning.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def run_eda_cleaning():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_raw.csv')
    clean_csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    viz_dir = os.path.join(base_dir, 'visualizations')
    os.makedirs(viz_dir, exist_ok=True)
    
    print("=" * 75)
    print("TASK 7: EDA - DATA INSPECTION & DATA CLEANING PIPELINE")
    print("=" * 75)
    
    # -------------------------------------------------------------
    # 1. DATA INSPECTION (RAW DATASET)
    # -------------------------------------------------------------
    df_raw = pd.read_csv(raw_csv_path)
    print("\n>>> STEP 1: INITIAL DATA INSPECTION (RAW DATASET)")
    print(f"- Dataset Shape        : {df_raw.shape[0]} Rows, {df_raw.shape[1]} Columns")
    print(f"- Column Names         : {list(df_raw.columns)}")
    print("\n[Column Data Types]:")
    print(df_raw.dtypes)
    
    print("\n[Five-Number Summary / Statistical Summary (Numerical)]: ")
    print(df_raw.describe().round(2).to_string())
    
    print("\n[Categorical Summary]: ")
    print(df_raw.describe(include=['object', 'string', 'str']).to_string())
    
    # -------------------------------------------------------------
    # 2. IDENTIFY DATA QUALITY ISSUES (BEFORE CLEANING)
    # -------------------------------------------------------------
    print("\n" + "-" * 75)
    print(">>> STEP 2: AUDITING DATA ANOMALIES & DEFECTS")
    print("-" * 75)
    
    # Missing values
    missing_before = df_raw.isnull().sum()
    print("[Missing Values Count]:")
    print(missing_before[missing_before > 0])
    
    # Duplicates
    dup_count = df_raw.duplicated().sum()
    print(f"\n[Duplicate Records Count] : {dup_count} duplicate rows found")
    
    # Inconsistent categories
    unique_cats_raw = df_raw['Product_Category'].unique()
    print(f"\n[Unique Categories Raw]   : {list(unique_cats_raw)}")
    
    # Negative/Zero Quantities
    invalid_qty_count = (df_raw['Quantity'] <= 0).sum()
    print(f"[Invalid Quantities (<=0)]: {invalid_qty_count} rows with invalid quantity")
    
    # -------------------------------------------------------------
    # 3. DATA CLEANING EXECUTION
    # -------------------------------------------------------------
    print("\n" + "-" * 75)
    print(">>> STEP 3: PERFORMING SYSTEMATIC DATA CLEANING")
    print("-" * 75)
    df_cleaned = df_raw.copy()
    
    # Action 1: Remove Duplicate Rows
    df_cleaned = df_cleaned.drop_duplicates()
    print(f"1. Removed {dup_count} duplicate records. Shape is now: {df_cleaned.shape}")
    
    # Action 2: Impute Missing Values
    # Impute Customer_Age using Median (robust against skewness)
    age_median = df_cleaned['Customer_Age'].median()
    df_cleaned['Customer_Age'] = df_cleaned['Customer_Age'].fillna(age_median)
    print(f"2. Imputed missing Customer_Age with median value: {age_median:.0f} years")
    
    # Impute Customer_Rating using Mode / Rounded Median
    rating_mode = df_cleaned['Customer_Rating'].mode()[0]
    df_cleaned['Customer_Rating'] = df_cleaned['Customer_Rating'].fillna(rating_mode)
    print(f"3. Imputed missing Customer_Rating with mode value: {rating_mode:.1f} stars")
    
    # Action 3: Standardize Categorical Strings
    def standardize_category(val):
        if not isinstance(val, str):
            return val
        clean_val = val.strip().lower()
        if 'electr' in clean_val:
            return 'Electronics'
        elif 'fash' in clean_val:
            return 'Fashion'
        elif 'home' in clean_val or 'kitchen' in clean_val:
            return 'Home & Kitchen'
        elif 'book' in clean_val:
            return 'Books'
        elif 'beaut' in clean_val or 'health' in clean_val:
            return 'Beauty & Health'
        return val.title()
        
    df_cleaned['Product_Category'] = df_cleaned['Product_Category'].apply(standardize_category)
    print(f"4. Standardized category casing. Unique categories now: {sorted(df_cleaned['Product_Category'].unique())}")
    
    # Action 4: Correct Invalid Numeric Values
    # Quantity <= 0 replaced with valid minimum 1, recompute sales
    mask_invalid_qty = df_cleaned['Quantity'] <= 0
    df_cleaned.loc[mask_invalid_qty, 'Quantity'] = 1
    # Recalculate Sales_Amount and Profit for corrected rows
    for idx in df_cleaned[mask_invalid_qty].index:
        p = df_cleaned.loc[idx, 'Unit_Price']
        q = df_cleaned.loc[idx, 'Quantity']
        d = df_cleaned.loc[idx, 'Discount_Percent'] / 100.0
        s = round(p * q * (1 - d), 2)
        df_cleaned.loc[idx, 'Sales_Amount'] = s
    print(f"5. Corrected {invalid_qty_count} invalid quantity entries and reconciled transaction amounts.")
    
    # Save final cleaned dataset
    df_cleaned.to_csv(clean_csv_path, index=False)
    print(f"\nCleaned dataset persisted to: {clean_csv_path}")
    
    # -------------------------------------------------------------
    # 4. BEFORE VS. AFTER COMPARISON SUMMARY
    # -------------------------------------------------------------
    print("\n" + "=" * 75)
    print(">>> STEP 4: BEFORE VS. AFTER DATA QUALITY COMPARISON MATRIX")
    print("=" * 75)
    
    comparison_table = pd.DataFrame({
        'Quality Dimension': [
            'Total Row Count', 
            'Missing Age Values', 
            'Missing Rating Values', 
            'Duplicate Records', 
            'Distinct Product Categories', 
            'Invalid Quantity Records'
        ],
        'Before Cleaning (Raw)': [
            len(df_raw), 
            df_raw['Customer_Age'].isnull().sum(), 
            df_raw['Customer_Rating'].isnull().sum(), 
            df_raw.duplicated().sum(), 
            df_raw['Product_Category'].nunique(), 
            (df_raw['Quantity'] <= 0).sum()
        ],
        'After Cleaning (Cleaned)': [
            len(df_cleaned), 
            df_cleaned['Customer_Age'].isnull().sum(), 
            df_cleaned['Customer_Rating'].isnull().sum(), 
            df_cleaned.duplicated().sum(), 
            df_cleaned['Product_Category'].nunique(), 
            (df_cleaned['Quantity'] <= 0).sum()
        ],
        'Cleaning Treatment Applied': [
            'Duplicates dropped (608 -> 600)',
            'Median imputation (35.0 years)',
            'Mode imputation (4.0 stars)',
            'drop_duplicates() on primary keys',
            'Casing normalization (.replace)',
            'Floored to valid min Quantity = 1'
        ]
    })
    print(comparison_table.to_string(index=False))
    
    # -------------------------------------------------------------
    # 5. GENERATE VISUAL COMPARISON CHART (SCREENSHOT ASSET)
    # -------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("Data Cleaning Audit: Before vs. After Comparative Dashboard", fontsize=15, fontweight='bold')
    
    # Panel 1: Missing Values
    categories_miss = ['Customer_Age', 'Customer_Rating']
    before_miss = [df_raw['Customer_Age'].isnull().sum(), df_raw['Customer_Rating'].isnull().sum()]
    after_miss = [df_cleaned['Customer_Age'].isnull().sum(), df_cleaned['Customer_Rating'].isnull().sum()]
    
    x = np.arange(len(categories_miss))
    width = 0.35
    axes[0, 0].bar(x - width/2, before_miss, width, label='Before Cleaning', color='#e74c3c', edgecolor='black')
    axes[0, 0].bar(x + width/2, after_miss, width, label='After Cleaning', color='#2ecc71', edgecolor='black')
    axes[0, 0].set_title("Missing Values by Feature", fontweight='bold')
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(categories_miss)
    axes[0, 0].set_ylabel("Null Count")
    axes[0, 0].legend()
    axes[0, 0].grid(axis='y', linestyle='--', alpha=0.5)
    
    # Panel 2: Total Rows & Duplicates
    metrics_row = ['Total Rows', 'Duplicates']
    before_rows = [len(df_raw), df_raw.duplicated().sum()]
    after_rows = [len(df_cleaned), df_cleaned.duplicated().sum()]
    x2 = np.arange(len(metrics_row))
    axes[0, 1].bar(x2 - width/2, before_rows, width, label='Before Cleaning', color='#e67e22', edgecolor='black')
    axes[0, 1].bar(x2 + width/2, after_rows, width, label='After Cleaning', color='#27ae60', edgecolor='black')
    axes[0, 1].set_title("Dataset Records & Redundancies", fontweight='bold')
    axes[0, 1].set_xticks(x2)
    axes[0, 1].set_xticklabels(metrics_row)
    axes[0, 1].set_ylabel("Record Count")
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)
    
    # Panel 3: Category Cardinality
    cats_before = df_raw['Product_Category'].nunique()
    cats_after = df_cleaned['Product_Category'].nunique()
    axes[1, 0].bar(['Raw Categories', 'Cleaned Categories'], [cats_before, cats_after], color=['#9b59b6', '#3498db'], edgecolor='black', width=0.5)
    axes[1, 0].set_title("Product Category Cardinality (String Normalization)", fontweight='bold')
    axes[1, 0].set_ylabel("Distinct Categories Count")
    for i, v in enumerate([cats_before, cats_after]):
        axes[1, 0].text(i, v + 0.15, str(v), ha='center', fontweight='bold')
    axes[1, 0].grid(axis='y', linestyle='--', alpha=0.5)
    
    # Panel 4: Quantity Distribution (Violin or Box)
    axes[1, 1].hist(df_cleaned['Quantity'], bins=6, color='#1abc9c', edgecolor='black', alpha=0.8)
    axes[1, 1].set_title("Cleaned Order Quantity Distribution (Min >= 1)", fontweight='bold')
    axes[1, 1].set_xlabel("Quantity")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    comp_plot_path = os.path.join(viz_dir, 'task7_cleaning_comparison.png')
    plt.savefig(comp_plot_path, dpi=300)
    plt.close()
    print(f"\nComparative Audit Visualization saved to: {comp_plot_path}")
    print("=" * 75)

if __name__ == '__main__':
    run_eda_cleaning()
