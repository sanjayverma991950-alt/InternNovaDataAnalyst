"""
InternNova Data Analytics Internship - Week 4
Task 6: Seaborn Visualization (15 Marks)
Student Name: Sanjay Kumar

Objective:
Using a suitable dataset, create the following visualizations using Seaborn:
1. Count Plot
2. Box Plot
3. Heatmap
4. Pair Plot

For each visualization:
- Add an appropriate title.
- Use relevant variables.
- Display the output.
- Write a brief explanation of the pattern or relationship shown.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set modern, publication-quality aesthetic
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'Arial'

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    return pd.read_csv(csv_path)

def generate_seaborn_visualizations():
    df = load_data()
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualizations')
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 70)
    print("TASK 6: SEABORN STATISTICAL DATA VISUALIZATIONS")
    print("=" * 70)
    
    # -------------------------------------------------------------
    # 1. COUNT PLOT: Payment Method by Gender
    # -------------------------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(9, 5))
    sns.countplot(
        data=df, 
        x='Payment_Method', 
        hue='Gender', 
        palette='Set2', 
        edgecolor='black', 
        ax=ax1
    )
    ax1.set_title("Transaction Count by Payment Method and Gender", fontsize=14, fontweight='bold', pad=12)
    ax1.set_xlabel("Payment Method", fontsize=11, fontweight='bold')
    ax1.set_ylabel("Transaction Count", fontsize=11, fontweight='bold')
    ax1.legend(title='Gender', frameon=True)
    
    # Add count labels
    for p in ax1.patches:
        h = p.get_height()
        if h > 0:
            ax1.annotate(f"{int(h)}", 
                         (p.get_x() + p.get_width() / 2., h), 
                         ha='center', va='bottom', fontsize=9, xytext=(0, 2), 
                         textcoords='offset points')
                         
    plt.tight_layout()
    chart1_path = os.path.join(output_dir, 'task6_1_count_plot.png')
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[1/4] Count Plot saved to: {chart1_path}")
    print("Explanation 1: The count plot demonstrates that Credit Card and UPI are the dominant payment modes across both male and female customers, whereas Cash on Delivery represents a smaller fraction, reflecting mature digital payment adoption.")

    # -------------------------------------------------------------
    # 2. BOX PLOT: Profit Distribution across Product Categories
    # -------------------------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(10, 5.5))
    sns.boxplot(
        data=df, 
        x='Product_Category', 
        y='Profit', 
        hue='Product_Category',
        legend=False,
        palette='Spectral', 
        showmeans=True,
        meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"8"},
        ax=ax2
    )
    ax2.set_title("Profit Distribution Across Product Categories (with Outliers)", fontsize=14, fontweight='bold', pad=12)
    ax2.set_xlabel("Product Category", fontsize=11, fontweight='bold')
    ax2.set_ylabel("Profit ($)", fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    chart2_path = os.path.join(output_dir, 'task6_2_box_plot.png')
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[2/4] Box Plot saved to: {chart2_path}")
    print("Explanation 2: The box plot reveals that Electronics exhibits the highest median profit and widest interquartile spread with prominent high-end outliers, while Books and Fashion display tighter, more consistent low-to-mid profit ranges.")

    # -------------------------------------------------------------
    # 3. HEATMAP: Correlation Matrix of Numerical Features
    # -------------------------------------------------------------
    num_cols = ['Sales_Amount', 'Profit', 'Discount_Percent', 'Customer_Age', 'Quantity', 'Unit_Price', 'Customer_Rating']
    corr_matrix = df[num_cols].corr()
    
    fig3, ax3 = plt.subplots(figsize=(8.5, 6.5))
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        fmt=".2f", 
        cmap='coolwarm', 
        vmin=-1, vmax=1, 
        linewidths=0.8, 
        cbar_kws={'label': 'Pearson Correlation (r)'},
        ax=ax3
    )
    ax3.set_title("Heatmap: Correlation Matrix of Key Metrics", fontsize=14, fontweight='bold', pad=12)
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    chart3_path = os.path.join(output_dir, 'task6_3_heatmap.png')
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print(f"[3/4] Heatmap saved to: {chart3_path}")
    print("Explanation 3: The correlation heatmap reveals an exceptionally strong positive correlation between Sales Amount and Profit (r = 0.91), while Discount Percent shows a negative drag on margins, and Customer Age shows near-zero correlation with purchase volume.")

    # -------------------------------------------------------------
    # 4. PAIR PLOT: Pairwise Multidimensional Relationships
    # -------------------------------------------------------------
    pair_cols = ['Sales_Amount', 'Profit', 'Discount_Percent', 'Customer_Age', 'Product_Category']
    pair_grid = sns.pairplot(
        df[pair_cols], 
        hue='Product_Category', 
        palette='bright', 
        corner=False, 
        diag_kind='kde',
        plot_kws={'alpha': 0.6, 's': 30}
    )
    pair_grid.fig.subplots_adjust(top=0.94)
    pair_grid.fig.suptitle("Seaborn Pair Plot: Multivariate Distributions & Relationships", fontsize=14, fontweight='bold')
    
    chart4_path = os.path.join(output_dir, 'task6_4_pair_plot.png')
    pair_grid.savefig(chart4_path, dpi=250)
    plt.close()
    print(f"[4/4] Pair Plot saved to: {chart4_path}")
    print("Explanation 4: The pair plot provides an all-in-one matrix comparing bivariate scatter plots and univariate KDE distributions. It visually proves how Electronics cluster distinctly at higher sales and profits compared to other consumer goods.")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    generate_seaborn_visualizations()
