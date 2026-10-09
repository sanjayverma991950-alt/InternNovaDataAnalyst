"""
InternNova Data Analytics Internship - Week 4
Task 1: Statistical Analysis – Mean, Median & Mode (10 Marks)
Student Name: Sanjay Kumar

Objective:
Using a suitable numerical dataset:
1. Calculate the Mean.
2. Calculate the Median.
3. Calculate the Mode.
4. Display the results.
5. Write a brief explanation of what each measure tells you about the dataset.
"""

import pandas as pd
import numpy as np
from scipy import stats
import os

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    return pd.read_csv(csv_path)

def analyze_central_tendency():
    df = load_data()
    
    print("=" * 70)
    print("TASK 1: STATISTICAL ANALYSIS - MEAN, MEDIAN & MODE")
    print("=" * 70)
    print(f"Dataset Loaded: E-Commerce Customer & Sales Analytics")
    print(f"Total Observations: {len(df)} rows")
    print("-" * 70)
    
    variables = ['Sales_Amount', 'Customer_Age', 'Quantity', 'Unit_Price']
    
    results = []
    for col in variables:
        series = df[col]
        mean_val = series.mean()
        median_val = series.median()
        mode_val = series.mode()[0]
        skew_val = series.skew()
        
        results.append({
            'Variable': col,
            'Mean': round(mean_val, 2),
            'Median': round(median_val, 2),
            'Mode': round(mode_val, 2),
            'Skewness': round(skew_val, 3)
        })
    
    results_df = pd.DataFrame(results)
    print("\n[Summary Table of Measures of Central Tendency]")
    print(results_df.to_string(index=False))
    print("-" * 70)
    
    # Detailed focus on Sales_Amount
    sales = df['Sales_Amount']
    sales_mean = sales.mean()
    sales_median = sales.median()
    sales_mode = sales.mode()[0]
    
    print("\nDetailed Case Study: Sales_Amount ($)")
    print(f"- Mean   (Average)           : ${sales_mean:.2f}")
    print(f"- Median (Middle Value)      : ${sales_median:.2f}")
    print(f"- Mode   (Most Frequent)     : ${sales_mode:.2f}")
    print(f"- Difference (Mean - Median) : ${sales_mean - sales_median:.2f}")
    
    print("\n" + "=" * 70)
    print("EXPLANATION OF RESULTS & STATISTICAL INTERPRETATION")
    print("=" * 70)
    print(f"""
1. MEAN (Arithmetic Average):
   - Definition: The sum of all values divided by total count (Sum(X) / N).
   - What it reveals: The mean Sales Amount is ${sales_mean:.2f}. The mean represents 
     the overall expected revenue per transaction. However, the mean is sensitive 
     to extreme values (outliers) and is pulled upward by large bulk/electronic orders.

2. MEDIAN (50th Percentile / Center):
   - Definition: The middle value when values are arranged in ascending order.
   - What it reveals: The median Sales Amount is ${sales_median:.2f}. Exactly 50% of 
     customer purchases are below ${sales_median:.2f}, and 50% are above ${sales_median:.2f}. Because 
     Median is resistant to extreme outliers, it provides a more robust representation 
     of the typical customer basket size than the arithmetic mean.

3. MODE (Most Frequent Observation):
   - Definition: The value that appears most often in the dataset.
   - What it reveals: The mode indicates the most common transaction total (${sales_mode:.2f}).
     This points to a high volume of lower-cost accessories and book purchases.

4. SKEWNESS & DISTRIBUTION IMPLICATIONS:
   - Notice that Mean (${sales_mean:.2f}) > Median (${sales_median:.2f}).
   - This right-skewed (positively skewed, skewness = {results[0]['Skewness']}) distribution confirms that while the 
     majority of transactions fall below $150, a small cluster of high-ticket electronic 
     purchases creates a long right tail that pulls the mean upward.
""")
    print("=" * 70)

if __name__ == '__main__':
    analyze_central_tendency()
