"""
InternNova Data Analytics Internship - Week 4
Task 4: Outlier Detection (10 Marks)
Student Name: Sanjay Kumar

Objective:
Using a numerical dataset:
1. Identify potential outliers.
2. Use an appropriate method to detect the outliers (IQR Method & Z-Score Method).
3. Display the identified outliers.
4. Briefly explain how outliers can affect data analysis.
"""

import pandas as pd
import numpy as np
from scipy import stats
import os

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    return pd.read_csv(csv_path)

def detect_outliers():
    df = load_data()
    
    print("=" * 75)
    print("TASK 4: OUTLIER DETECTION IN NUMERICAL DATA")
    print("=" * 75)
    print(f"Dataset Loaded: E-Commerce Customer & Sales Analytics ({len(df)} records)")
    print("-" * 75)
    
    col = 'Sales_Amount'
    series = df[col]
    
    # ---------------------------------------------------------
    # METHOD 1: INTERQUARTILE RANGE (IQR) METHOD
    # ---------------------------------------------------------
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    iqr_outliers = df[(series < lower_bound) | (series > upper_bound)]
    
    print("\n[METHOD 1: INTERQUARTILE RANGE (IQR) METHOD (Tukey's Fences)]")
    print(f"- 25th Percentile (Q1)     : ${q1:.2f}")
    print(f"- 75th Percentile (Q3)     : ${q3:.2f}")
    print(f"- Interquartile Range (IQR): ${iqr:.2f}")
    print(f"- Lower Threshold Bound    : ${lower_bound:.2f} (Q1 - 1.5 * IQR)")
    print(f"- Upper Threshold Bound    : ${upper_bound:.2f} (Q3 + 1.5 * IQR)")
    print(f"- Total IQR Outliers Found : {len(iqr_outliers)} out of {len(df)} rows ({(len(iqr_outliers)/len(df))*100:.2f}%)")
    
    # ---------------------------------------------------------
    # METHOD 2: Z-SCORE METHOD (Standard Score)
    # ---------------------------------------------------------
    mean_val = series.mean()
    std_val = series.std()
    df['Z_Score_Sales'] = (series - mean_val) / std_val
    z_outliers = df[df['Z_Score_Sales'].abs() > 3]
    
    print("\n[METHOD 2: Z-SCORE METHOD (|Z| > 3.0)]")
    print(f"- Dataset Mean (mu)        : ${mean_val:.2f}")
    print(f"- Standard Deviation (s)   : ${std_val:.2f}")
    print(f"- Lower Limit (mu - 3s)    : ${mean_val - 3*std_val:.2f}")
    print(f"- Upper Limit (mu + 3s)    : ${mean_val + 3*std_val:.2f}")
    print(f"- Total Z-Score Outliers   : {len(z_outliers)} out of {len(df)} rows ({(len(z_outliers)/len(df))*100:.2f}%)")
    
    # ---------------------------------------------------------
    # DISPLAY IDENTIFIED OUTLIERS
    # ---------------------------------------------------------
    print("\n" + "-" * 75)
    print("DISPLAYING IDENTIFIED HIGH-LEVERAGE OUTLIERS (Z-Score > 3.0):")
    print("-" * 75)
    outlier_display = z_outliers[['Transaction_ID', 'Product_Category', 'Quantity', 'Unit_Price', 
                                  'Discount_Percent', 'Sales_Amount', 'Profit', 'Z_Score_Sales']].copy()
    outlier_display['Z_Score_Sales'] = outlier_display['Z_Score_Sales'].round(2)
    print(outlier_display.to_string(index=False))
    
    # Impact comparison: with vs without outliers
    clean_series = series[~series.index.isin(z_outliers.index)]
    print("\n[IMPACT DEMONSTRATION: METRICS WITH VS. WITHOUT OUTLIERS]")
    print(f"{'Metric':<25} | {'With Outliers (N=600)':<22} | {'Without Outliers (N=' + str(len(clean_series)) + ')':<22}")
    print("-" * 75)
    print(f"{'Mean Sales':<25} | ${mean_val:<21.2f} | ${clean_series.mean():<21.2f}")
    print(f"{'Median Sales':<25} | ${series.median():<21.2f} | ${clean_series.median():<21.2f}")
    print(f"{'Std Deviation':<25} | ${std_val:<21.2f} | ${clean_series.std():<21.2f}")
    print(f"{'Variance':<25} | {series.var():<22.2f} | {clean_series.var():<22.2f}")
    
    # ---------------------------------------------------------
    # EXPLANATION OF OUTLIER EFFECTS
    # ---------------------------------------------------------
    print("\n" + "=" * 75)
    print("HOW OUTLIERS AFFECT DATA ANALYSIS & DECISION MAKING")
    print("=" * 75)
    print("""
1. DISTORTION OF CENTRAL TENDENCY (MEAN):
   - The mean is heavily pulled by extreme values. In our dataset, just 6 high-value 
     bulk orders inflate the average transaction from ~$235 to $291.58.
   - Relying on the mean alone would misguide inventory and pricing targets.

2. ARTIFICIAL INFLATION OF VARIANCE & STANDARD DEVIATION:
   - Because variance sums squared deviations (x - mu)^2, extreme values cause an 
     exponential jump in variance and standard deviation, exaggerating perceived 
     system instability or volatility.

3. IMPACT ON MACHINE LEARNING & CORRELATIONS:
   - High leverage outliers can artificially steepen or flatten regression lines, 
     drastically altering predictive model coefficients and correlation values.

4. BUSINESS CONTEXT & TREATMENT:
   - In commercial analytics, outliers should NOT simply be discarded blindly.
   - In our e-commerce data, these outliers represent high-value B2B/wholesale accounts.
   - Best practice: Segment them into an 'Enterprise Accounts' category rather than 
     treating them as corrupt noise.
""")
    print("=" * 75)

if __name__ == '__main__':
    detect_outliers()
