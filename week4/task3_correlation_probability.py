"""
InternNova Data Analytics Internship - Week 4
Task 3: Correlation & Probability Basics (10 Marks)
Student Name: Sanjay Kumar

Objective:
Part A: Correlation
1. Select two numerical variables from a dataset.
2. Calculate their correlation.
3. Determine whether the relationship is positive, negative, or weak.

Part B: Probability
1. Create a simple real-world probability example.
2. Calculate the probability.
3. Display and explain the result.
"""

import pandas as pd
import numpy as np
from scipy import stats
import os

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    return pd.read_csv(csv_path)

def analyze_correlation_and_probability():
    df = load_data()
    
    print("=" * 70)
    print("TASK 3: CORRELATION & PROBABILITY BASICS")
    print("=" * 70)
    print(f"Dataset Loaded: E-Commerce Customer & Sales Analytics ({len(df)} records)")
    print("-" * 70)
    
    # -------------------------------------------------------------
    # PART A: CORRELATION ANALYSIS
    # -------------------------------------------------------------
    print("\n--- PART A: CORRELATION ANALYSIS ---")
    
    pairs = [
        ('Sales_Amount', 'Profit', "Revenue vs Profitability"),
        ('Discount_Percent', 'Profit', "Discount Level vs Profit"),
        ('Customer_Age', 'Sales_Amount', "Customer Demographics vs Sales"),
        ('Quantity', 'Sales_Amount', "Order Size vs Sales Volume")
    ]
    
    def interpret_corr(r):
        if r >= 0.7:
            return "Strong Positive"
        elif 0.3 <= r < 0.7:
            return "Moderate Positive"
        elif -0.3 < r < 0.3:
            return "Weak / Negligible"
        elif -0.7 < r <= -0.3:
            return "Moderate Negative"
        else:
            return "Strong Negative"
            
    corr_records = []
    for var1, var2, desc in pairs:
        r_val, p_val = stats.pearsonr(df[var1], df[var2])
        classification = interpret_corr(r_val)
        corr_records.append({
            'Variable 1': var1,
            'Variable 2': var2,
            'Description': desc,
            'Pearson (r)': round(r_val, 4),
            'p-value': f"{p_val:.2e}",
            'Relationship Type': classification
        })
        
    corr_df = pd.DataFrame(corr_records)
    print(corr_df.to_string(index=False))
    print("\n[Detailed Correlation Interpretation]:")
    print(f"1. Sales_Amount vs Profit (r = {corr_records[0]['Pearson (r)']} - {corr_records[0]['Relationship Type']}):")
    print("   Higher sales volume strongly drives dollar gross profit across all categories.")
    print(f"2. Discount_Percent vs Profit (r = {corr_records[1]['Pearson (r)']} - {corr_records[1]['Relationship Type']}):")
    print("   Higher promotional discount percentages erode net profit margins.")
    print(f"3. Customer_Age vs Sales_Amount (r = {corr_records[2]['Pearson (r)']} - {corr_records[2]['Relationship Type']}):")
    print("   Transaction ticket size is essentially independent of age; high-ticket electronics are bought across age brackets.")
    
    # -------------------------------------------------------------
    # PART B: REAL-WORLD PROBABILITY BASICS
    # -------------------------------------------------------------
    print("\n" + "-" * 70)
    print("--- PART B: REAL-WORLD PROBABILITY EXAMPLES ---")
    print("-" * 70)
    
    total_txns = len(df)
    
    # Scenario 1: Marginal Probability P(High Value Order: Sales > $300)
    high_val_count = (df['Sales_Amount'] > 300).sum()
    p_high_val = high_val_count / total_txns
    
    # Scenario 2: Marginal Probability P(Payment via UPI)
    upi_count = (df['Payment_Method'] == 'UPI').sum()
    p_upi = upi_count / total_txns
    
    # Scenario 3: Conditional Probability P(UPI | Age < 30)
    young_mask = df['Customer_Age'] < 30
    n_young = young_mask.sum()
    young_and_upi = ((df['Customer_Age'] < 30) & (df['Payment_Method'] == 'UPI')).sum()
    p_upi_given_young = young_and_upi / n_young if n_young > 0 else 0
    
    # Scenario 4: Probability of 5-Star Customer Rating
    five_star_count = (df['Customer_Rating'] == 5.0).sum()
    p_five_star = five_star_count / total_txns
    
    print("\nReal-World Scenario 1: Marginal Probability")
    print("Event A: A randomly chosen customer order exceeds $300 (High-Ticket Purchase)")
    print(f"- Total Orders (N)                     : {total_txns}")
    print(f"- Orders with Sales > $300 (n(A))      : {high_val_count}")
    print(f"- Probability P(Sales > $300)          : {high_val_count} / {total_txns} = {p_high_val:.4f} ({p_high_val*100:.2f}%)")
    print(f"Explanation: Approximately {p_high_val*100:.1f}% of all orders generate high revenue, informing inventory stocking.")
    
    print("\nReal-World Scenario 2: Conditional Probability")
    print("Event B: Payment via UPI; Condition C: Customer is Young Adult (Age < 30)")
    print(f"- Customers under 30 (n(C))            : {n_young}")
    print(f"- Young Customers paying UPI (n(B n C)): {young_and_upi}")
    print(f"- Overall P(UPI)                       : {p_upi:.4f} ({p_upi*100:.2f}%)")
    print(f"- Conditional P(UPI | Age < 30)        : {p_upi_given_young:.4f} ({p_upi_given_young*100:.2f}%)")
    print(f"Explanation: Young shoppers show a {p_upi_given_young*100:.1f}% likelihood of paying via UPI compared to ")
    print(f"the overall store average of {p_upi*100:.1f}%, indicating mobile-first payment behavior among youth.")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    analyze_correlation_and_probability()
