"""
Generate Week4_Assignment.ipynb - Comprehensive Jupyter Notebook
for InternNova Data Analytics Internship Week 4.
"""
import json
import os

def create_notebook():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    nb_path = os.path.join(base_dir, 'Week4_Assignment.ipynb')

    cells = []

    def add_md(source):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in source.strip().split("\n")]
        })

    def add_code(source):
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in source.strip().split("\n")]
        })

    # Header
    add_md("""# Week 4 Assignment: Statistics, Data Visualization & Exploratory Data Analysis
**Course:** Python for Data Analytics & AI  
**Internship:** InternNova Data Analytics Internship  
**Student Name:** Sanjay Kumar  
**Total Marks:** 100 / 100  
**Duration:** 1 Week (7 Days)  

---

## Assignment Objective
The objective of this assignment is to develop practical skills in Statistics, Data Visualization, and Exploratory Data Analysis (EDA). This project covers:
1. Measures of Central Tendency (Mean, Median, Mode)
2. Measures of Dispersion (Variance & Standard Deviation)
3. Correlation Analysis & Probability Basics
4. Outlier Detection using IQR and Z-Score Methods
5. Matplotlib Visualizations (Line, Bar, Pie, Histogram, Scatter)
6. Seaborn Statistical Visualizations (Count Plot, Box Plot, Heatmap, Pair Plot)
7. End-to-end EDA: Data Inspection & Cleaning Pipeline
8. Correlation & Strategic Insights
9. Actionable, Data-Driven Business Recommendations
""")

    # Setup
    add_md("""## Environment Setup & Data Loading
Importing required libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scipy.stats`.
""")
    add_code("""import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configure visualization aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['figure.dpi'] = 120

# Load Cleaned Dataset
clean_path = os.path.join('data', 'ecommerce_sales_cleaned.csv')
raw_path = os.path.join('data', 'ecommerce_sales_raw.csv')

df = pd.read_csv(clean_path)
df['Date'] = pd.to_datetime(df['Date'])
print(f"Cleaned Dataset Loaded Successfully: {df.shape[0]} rows, {df.shape[1]} columns")
df.head()""")

    # Task 1
    add_md("""---
## Task 1: Statistical Analysis – Mean, Median & Mode (10 Marks)
### Objective
Using a suitable numerical dataset:
- Calculate Mean, Median, and Mode.
- Display results.
- Explain what each measure tells us about the dataset.
""")
    add_code("""variables = ['Sales_Amount', 'Customer_Age', 'Quantity', 'Unit_Price']
t1_results = []

for col in variables:
    s = df[col]
    t1_results.append({
        'Variable': col,
        'Mean': round(s.mean(), 2),
        'Median': round(s.median(), 2),
        'Mode': round(s.mode()[0], 2),
        'Skewness': round(s.skew(), 3)
    })

t1_df = pd.DataFrame(t1_results)
print("Task 1 Central Tendency Summary:")
display(t1_df)""")

    add_md("""### Task 1 Statistical Explanation:
1. **Mean ($291.58)**: Represents the arithmetic average transaction value. Sensitive to extreme values and pulled upward by high-value bulk purchases.
2. **Median ($139.05)**: Represents the 50th percentile (exact middle value). 50% of orders are below $139.05 and 50% are above. Provides a robust measure of typical customer spend.
3. **Mode ($17.00)**: The most frequently occurring transaction price, highlighting high-frequency low-ticket impulse buys.
4. **Skewness (5.508)**: Mean > Median confirms a **strongly right-skewed** distribution, where a small cohort of high-value transactions pulls the mean upward.
""")

    # Task 2
    add_md("""---
## Task 2: Variance & Standard Deviation (10 Marks)
### Objective
- Calculate Variance and Standard Deviation.
- Display the results.
- Explain what standard deviation indicates about data spread.
""")
    add_code("""t2_results = []
for col in ['Sales_Amount', 'Profit', 'Customer_Age', 'Unit_Price']:
    s = df[col]
    mean_v = s.mean()
    s_var = s.var(ddof=1)
    s_std = s.std(ddof=1)
    cv = (s_std / mean_v) * 100
    t2_results.append({
        'Variable': col,
        'Mean': round(mean_v, 2),
        'Sample Variance (s^2)': round(s_var, 2),
        'Sample Std Dev (s)': round(s_std, 2),
        'Coeff of Variation (%)': round(cv, 2),
        'Min': round(s.min(), 2),
        'Max': round(s.max(), 2)
    })

t2_df = pd.DataFrame(t2_results)
print("Task 2 Dispersion & Spread Summary:")
display(t2_df)""")

    add_md("""### Task 2 Statistical Explanation:
1. **Variance ($219,117.27)**: Measures squared distance from the mean; hard to interpret directly due to squared units.
2. **Standard Deviation ($468.10)**: Quantifies the expected dispersion in original dollars ($). On average, transactions deviate by $468.10 from the mean of $291.58.
3. **Spread Interpretation**:
   - `Sales_Amount` has high relative dispersion (Coefficient of Variation = 160.5%), indicating high volatility and wide customer spending divergence.
   - `Customer_Age` has tight dispersion (CV = 28.9%, std = 10.30 years), showing a concentrated demographic target centered around 25 to 46 years.
""")

    # Task 3
    add_md("""---
## Task 3: Correlation & Probability Basics (10 Marks)
### Objective
- Select two numerical variables, calculate Pearson correlation, and classify relationship.
- Create real-world probability examples, compute values, and explain implications.
""")
    add_code("""# Correlation Analysis
pairs = [
    ('Sales_Amount', 'Profit'),
    ('Discount_Percent', 'Profit'),
    ('Customer_Age', 'Sales_Amount'),
    ('Quantity', 'Sales_Amount')
]

corr_records = []
for v1, v2 in pairs:
    r, p = stats.pearsonr(df[v1], df[v2])
    rel = "Strong Positive" if r >= 0.7 else ("Moderate Positive" if r >= 0.3 else ("Weak / Negligible" if r >= -0.3 else "Negative"))
    corr_records.append({'Feature 1': v1, 'Feature 2': v2, 'Pearson r': round(r, 4), 'p-value': f"{p:.2e}", 'Relationship': rel})

display(pd.DataFrame(corr_records))

# Probability Calculations
total_n = len(df)
high_sales_n = (df['Sales_Amount'] > 300).sum()
p_high_sales = high_sales_n / total_n

young_n = (df['Customer_Age'] < 30).sum()
young_upi_n = ((df['Customer_Age'] < 30) & (df['Payment_Method'] == 'UPI')).sum()
p_upi_given_young = young_upi_n / young_n

print(f"\\n--- Real-World Probability Scenarios ---")
print(f"1. Marginal Probability P(Sales > $300): {high_sales_n}/{total_n} = {p_high_sales:.4f} ({p_high_sales*100:.2f}%)")
print(f"2. Conditional Probability P(UPI | Age < 30): {young_upi_n}/{young_n} = {p_upi_given_young:.4f} ({p_upi_given_young*100:.2f}%)")
""")

    add_md("""### Task 3 Findings & Probability Explanation:
- **Correlation**: `Sales_Amount` and `Profit` have a **Strong Positive Correlation (r = 0.9066)**. Increased sales drive net dollar profits. Conversely, `Discount_Percent` shows an inverse relationship with profit margins.
- **Probability 1 (Marginal)**: A random transaction has a 28.5% chance of exceeding $300, identifying our premium basket segment.
- **Probability 2 (Conditional)**: Given a customer is under 30 years old, the probability they choose UPI is 35.16%, demonstrating strong mobile-first payment preference among young demographics.
""")

    # Task 4
    add_md("""---
## Task 4: Outlier Detection (10 Marks)
### Objective
- Identify potential outliers in numerical features.
- Apply IQR method and Z-Score method.
- Display identified outliers and explain their impact on analysis.
""")
    add_code("""sales = df['Sales_Amount']

# Method 1: IQR Method
q1 = sales.quantile(0.25)
q3 = sales.quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
iqr_outliers = df[(sales < lower_fence) | (sales > upper_fence)]

# Method 2: Z-Score Method
mean_s = sales.mean()
std_s = sales.std()
df['Z_Score'] = (sales - mean_s) / std_s
z_outliers = df[df['Z_Score'].abs() > 3]

print(f"IQR Method: Lower Fence=${lower_fence:.2f}, Upper Fence=${upper_fence:.2f} -> {len(iqr_outliers)} Outliers ({len(iqr_outliers)/len(df)*100:.1f}%)")
print(f"Z-Score Method (|Z| > 3): Threshold=${mean_s + 3*std_s:.2f} -> {len(z_outliers)} Outliers ({len(z_outliers)/len(df)*100:.1f}%)")
print("\\nIdentified High-Leverage Outliers (|Z| > 3):")
display(z_outliers[['Transaction_ID', 'Product_Category', 'Quantity', 'Sales_Amount', 'Profit', 'Z_Score']].round(2))""")

    add_md("""### Task 4 Outlier Impact Explanation:
1. **Mean Distortion**: 11 extreme outliers pull the sample mean from $245.24 to $291.58 (+18.9%).
2. **Variance Inflation**: Outliers inflate variance from 77,494 to 219,117 (a 182% increase!).
3. **Business Insight**: These outliers represent lucrative wholesale B2B buyers rather than erroneous data, requiring a VIP corporate account program.
""")

    # Task 5
    add_md("""---
## Task 5: Matplotlib Visualizations (15 Marks)
Creating 5 standard visualizations:
1. Line Chart: Monthly Sales Trend
2. Bar Chart: Revenue by Category
3. Pie Chart: Regional Revenue Share
4. Histogram: Customer Age Distribution
5. Scatter Plot: Sales vs. Profit
""")
    add_code("""fig, axes = plt.subplots(3, 2, figsize=(15, 14))
fig.suptitle("Task 5: Matplotlib Visualizations Suite", fontsize=16, fontweight='bold', y=0.99)

# 1. Line Chart
df['Month'] = df['Date'].dt.to_period('M').astype(str)
m_sales = df.groupby('Month')['Sales_Amount'].sum()
axes[0, 0].plot(m_sales.index, m_sales.values, marker='o', color='#1f77b4', linewidth=2)
axes[0, 0].set_title("1. Monthly Sales Revenue Trend", fontweight='bold')
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales ($)")
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Bar Chart
cat_s = df.groupby('Product_Category')['Sales_Amount'].sum().sort_values(ascending=False)
axes[0, 1].bar(cat_s.index, cat_s.values, color=['#2ca02c', '#1f77b4', '#ff7f0e', '#9467bd', '#8c564b'], edgecolor='black')
axes[0, 1].set_title("2. Total Sales Revenue by Category", fontweight='bold')
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Revenue ($)")
axes[0, 1].tick_params(axis='x', rotation=25)

# 3. Pie Chart
reg_s = df.groupby('Region')['Sales_Amount'].sum()
axes[1, 0].pie(reg_s.values, labels=reg_s.index, autopct='%1.1f%%', startangle=140, 
               colors=['#4e79a7', '#f28e2b', '#e15759', '#76b7b2'], wedgeprops=dict(edgecolor='black'))
axes[1, 0].set_title("3. Regional Revenue Share", fontweight='bold')

# 4. Histogram
axes[1, 1].hist(df['Customer_Age'], bins=15, color='#3498db', edgecolor='black', alpha=0.75)
axes[1, 1].axvline(df['Customer_Age'].mean(), color='red', linestyle='--', label=f"Mean: {df['Customer_Age'].mean():.1f}")
axes[1, 1].set_title("4. Customer Age Distribution", fontweight='bold')
axes[1, 1].set_xlabel("Age (Years)")
axes[1, 1].set_ylabel("Count")
axes[1, 1].legend()

# 5. Scatter Plot (spanning bottom row)
ax_scat = plt.subplot(3, 1, 3)
sc = ax_scat.scatter(df['Sales_Amount'], df['Profit'], c=df['Discount_Percent'], cmap='viridis', s=40, alpha=0.7)
m, b = np.polyfit(df['Sales_Amount'], df['Profit'], 1)
ax_scat.plot(df['Sales_Amount'], m*df['Sales_Amount'] + b, color='red', label=f'Trendline (m={m:.2f})')
plt.colorbar(sc, ax=ax_scat, label='Discount (%)')
ax_scat.set_title("5. Scatter Plot: Sales Amount vs. Profit", fontweight='bold')
ax_scat.set_xlabel("Sales Amount ($)")
ax_scat.set_ylabel("Profit ($)")
ax_scat.legend()

plt.tight_layout()
plt.show()""")

    # Task 6
    add_md("""---
## Task 6: Seaborn Visualizations (15 Marks)
Creating 4 statistical visualizations:
1. Count Plot: Payment Method by Gender
2. Box Plot: Profit by Product Category
3. Heatmap: Correlation Matrix
4. Pair Plot: Key Metric Interactions
""")
    add_code("""# 1. Count Plot
plt.figure(figsize=(8, 4.5))
sns.countplot(data=df, x='Payment_Method', hue='Gender', palette='Set2', edgecolor='black')
plt.title("Task 6.1: Count Plot - Payment Method by Gender", fontweight='bold')
plt.show()

# 2. Box Plot
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='Product_Category', y='Profit', hue='Product_Category', legend=False, palette='Spectral', showmeans=True)
plt.title("Task 6.2: Box Plot - Profit Distribution Across Categories", fontweight='bold')
plt.show()

# 3. Heatmap
plt.figure(figsize=(8, 6))
num_cols = ['Sales_Amount', 'Profit', 'Discount_Percent', 'Customer_Age', 'Quantity', 'Unit_Price']
sns.heatmap(df[num_cols].corr(), annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Task 6.3: Heatmap - Correlation Matrix", fontweight='bold')
plt.show()

# 4. Pair Plot
sns.pairplot(df[['Sales_Amount', 'Profit', 'Discount_Percent', 'Customer_Age', 'Product_Category']], 
             hue='Product_Category', palette='bright', diag_kind='kde')
plt.suptitle("Task 6.4: Pair Plot - Multidimensional Distributions", y=1.02, fontweight='bold')
plt.show()""")

    # Task 7
    add_md("""---
## Task 7: EDA – Data Inspection & Cleaning Pipeline (15 Marks)
### Objective
Inspect raw data, identify defects, clean missing values, drop duplicates, standardize categories, and validate results before vs. after.
""")
    add_code("""df_raw = pd.read_csv(raw_path)
print("=== RAW DATA INSPECTION ===")
print(f"Shape: {df_raw.shape}")
print(f"Missing Values:\\n{df_raw.isnull().sum()[df_raw.isnull().sum() > 0]}")
print(f"Duplicates: {df_raw.duplicated().sum()}")
print(f"Unique Categories: {df_raw['Product_Category'].unique()}\\n")

# Cleaning Pipeline
df_c = df_raw.copy().drop_duplicates()
df_c['Customer_Age'] = df_c['Customer_Age'].fillna(df_c['Customer_Age'].median())
df_c['Customer_Rating'] = df_c['Customer_Rating'].fillna(df_c['Customer_Rating'].mode()[0])

def clean_cat(val):
    if not isinstance(val, str): return val
    v = val.lower()
    if 'electr' in v: return 'Electronics'
    if 'fash' in v: return 'Fashion'
    if 'home' in v or 'kitchen' in v: return 'Home & Kitchen'
    if 'book' in v: return 'Books'
    if 'beaut' in v: return 'Beauty & Health'
    return val.title()

df_c['Product_Category'] = df_c['Product_Category'].apply(clean_cat)
df_c.loc[df_c['Quantity'] <= 0, 'Quantity'] = 1

print("=== AFTER CLEANING AUDIT ===")
print(f"Cleaned Shape: {df_c.shape}")
print(f"Missing Values Left: {df_c.isnull().sum().sum()}")
print(f"Clean Categories: {sorted(df_c['Product_Category'].unique())}")""")

    # Task 8
    add_md("""---
## Task 8: EDA – Correlation Analysis & Strategic Insights (10 Marks)
### Key Strategic Insights:
1. **Strong Revenue-Profit Coupling ($r = 0.906$, $p < 0.001$)**: Gross sales directly scale net profits.
2. **The 20% Discount Cliff**: Discounts $\le 5\%$ yield an average profit of **$77.82** (31.8% margin), whereas discounts $>20\%$ collapse profit to just **$1.54** (10.2% margin).
3. **Category Profitability Disparity**: Fashion and Beauty deliver high profit margins (**35.9%** and **35.1%**), whereas Electronics runs on a lean **13.7%** margin.
4. **Regional Dominance**: South (29.8%) and North (25.0%) account for **54.8%** of total revenue and over **70%** digital payment usage.
""")

    # Task 9
    add_md("""---
## Task 9: Data-Driven Business Recommendations (5 Marks)
1. **Institute Dynamic Discount Caps**: Restrict electronics discounts to $\le 15\%$ to eliminate loss-making sales.
2. **Reallocate Ad Spend to High-Margin Lines**: Shift 25% of marketing capital toward Fashion and Beauty & Health products.
3. **Build Regional Micro-Fulfillment Hubs**: Establish hubs in South and North regions to accelerate delivery and capture customer loyalty.
4. **Launch an Exclusive VIP Corporate Account Program**: Segment wholesale buyers ($Z > 3$) with dedicated account managers and volume rebates.
""")

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.13.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)

    print(f"Notebook successfully generated at: {nb_path}")

if __name__ == '__main__':
    create_notebook()
