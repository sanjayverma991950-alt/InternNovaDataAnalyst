"""
InternNova Data Analytics Internship - Week 4
Task 2: Variance & Standard Deviation (10 Marks)
Student Name: Sanjay Kumar

Objective:
Using a suitable numerical dataset:
1. Calculate Variance.
2. Calculate Standard Deviation.
3. Display the results.
4. Explain what the standard deviation indicates about the spread of the data.
"""

import pandas as pd
import numpy as np
import os

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    return pd.read_csv(csv_path)

def analyze_dispersion():
    df = load_data()
    
    print("=" * 70)
    print("TASK 2: VARIANCE & STANDARD DEVIATION ANALYSIS")
    print("=" * 70)
    print(f"Dataset Loaded: E-Commerce Customer & Sales Analytics")
    print(f"Total Observations: {len(df)} rows")
    print("-" * 70)
    
    variables = ['Sales_Amount', 'Profit', 'Customer_Age', 'Unit_Price']
    
    dispersion_results = []
    for col in variables:
        series = df[col]
        mean_val = series.mean()
        # Sample variance (ddof=1) and Population variance (ddof=0)
        sample_var = series.var(ddof=1)
        pop_var = series.var(ddof=0)
        sample_std = series.std(ddof=1)
        pop_std = series.std(ddof=0)
        cv = (sample_std / mean_val) * 100 if mean_val != 0 else 0
        val_range = series.max() - series.min()
        
        dispersion_results.append({
            'Variable': col,
            'Mean': round(mean_val, 2),
            'Sample Variance (s^2)': round(sample_var, 2),
            'Sample Std Dev (s)': round(sample_std, 2),
            'Pop Std Dev (sigma)': round(pop_std, 2),
            'Coeff of Var (%)': round(cv, 2),
            'Range': round(val_range, 2)
        })
        
    disp_df = pd.DataFrame(dispersion_results)
    print("\n[Summary Table of Dispersion & Spread Measures]")
    print(disp_df.to_string(index=False))
    print("-" * 70)
    
    # In-depth Case Study on Sales_Amount and Customer_Age
    sales = df['Sales_Amount']
    s_mean = sales.mean()
    s_std = sales.std()
    s_var = sales.var()
    
    age = df['Customer_Age']
    a_mean = age.mean()
    a_std = age.std()
    a_var = age.var()
    
    print("\nDetailed Breakdown: Sales_Amount ($)")
    print(f"- Mean                     : ${s_mean:.2f}")
    print(f"- Sample Variance (s^2)    : {s_var:.2f} (in squared dollars)")
    print(f"- Sample Std Dev (s)       : ${s_std:.2f}")
    print(f"- 1 Std Dev Interval       : [${max(0, s_mean - s_std):.2f}, ${s_mean + s_std:.2f}]")
    print(f"- Coefficient of Variation : {(s_std/s_mean)*100:.2f}%")
    
    print("\nDetailed Breakdown: Customer_Age (Years)")
    print(f"- Mean                     : {a_mean:.2f} years")
    print(f"- Sample Variance (s^2)    : {a_var:.2f} years^2")
    print(f"- Sample Std Dev (s)       : {a_std:.2f} years")
    print(f"- 1 Std Dev Interval       : [{a_mean - a_std:.2f}, {a_mean + a_std:.2f}] years")
    print(f"- Coefficient of Variation : {(a_std/a_mean)*100:.2f}%")
    
    print("\n" + "=" * 70)
    print("EXPLANATION OF WHAT STANDARD DEVIATION INDICATES ABOUT DATA SPREAD")
    print("=" * 70)
    print(f"""
1. VARIANCE:
   - Variance measures the average of squared differences from the Mean.
   - For Sales Amount, variance is {s_var:.2f} dollars squared. Because variance is 
     expressed in squared units, it is unintuitive for direct business comparison.

2. STANDARD DEVIATION:
   - Standard deviation (s = sqrt(Variance)) converts the spread back into the original 
     units of the data ($). For Sales Amount, standard deviation is ${s_std:.2f}.
   - Standard deviation quantifies the typical distance or dispersion that individual 
     transactions deviate from the average transaction value (${s_mean:.2f}).

3. INTERPRETATION OF DATA SPREAD:
   - High Spread in Sales Amount (CV = {(s_std/s_mean)*100:.1f}%):
     A standard deviation of ${s_std:.2f} relative to a mean of ${s_mean:.2f} indicates 
     substantial revenue variability. Customers are not buying at a uniform price point; 
     instead, orders fluctuate widely between low-ticket books/fashion items and 
     expensive enterprise electronics orders.
   - Low Spread in Customer Age (CV = {(a_std/a_mean)*100:.1f}%):
     By contrast, customer age has a tight standard deviation of only {a_std:.2f} years 
     around a mean of {a_mean:.2f} years. This indicates that our core customer demographic 
     is consistently centered around 25 to 46 years of age.

4. BUSINESS SIGNIFICANCE:
   - High standard deviation in sales signals revenue volatility and inventory forecasting 
     complexity, necessitating tiered marketing and segmented safety-stock planning.
""")
    print("=" * 70)

if __name__ == '__main__':
    analyze_dispersion()
