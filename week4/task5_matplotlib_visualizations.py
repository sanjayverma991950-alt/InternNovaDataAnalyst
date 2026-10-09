"""
InternNova Data Analytics Internship - Week 4
Task 5: Matplotlib Visualization (15 Marks)
Student Name: Sanjay Kumar

Objective:
Using a suitable dataset, create the following visualizations using Matplotlib:
1. Line Chart
2. Bar Chart
3. Pie Chart
4. Histogram
5. Scatter Plot

For each visualization:
- Add an appropriate title.
- Label the axes where applicable.
- Use meaningful data.
- Write a brief explanation of the visualization.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Configure matplotlib styling for clean, professional reports
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def generate_visualizations():
    df = load_data()
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualizations')
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 70)
    print("TASK 5: MATPLOTLIB DATA VISUALIZATIONS")
    print("=" * 70)
    
    # -------------------------------------------------------------
    # 1. LINE CHART: Monthly Sales Trend (2024)
    # -------------------------------------------------------------
    df['Month_Year'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month_Year')['Sales_Amount'].sum().reset_index()
    monthly_sales['Month_Str'] = monthly_sales['Month_Year'].astype(str)
    
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(monthly_sales['Month_Str'], monthly_sales['Sales_Amount'], 
             color='#1f77b4', marker='o', linewidth=2.5, markersize=7, label='Total Monthly Sales ($)')
    ax1.fill_between(monthly_sales['Month_Str'], monthly_sales['Sales_Amount'], color='#1f77b4', alpha=0.15)
    ax1.set_title("Monthly Sales Revenue Trend (2024)", fontsize=14, fontweight='bold', pad=12)
    ax1.set_xlabel("Month", fontsize=11, fontweight='bold')
    ax1.set_ylabel("Total Sales Revenue ($)", fontsize=11, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    
    # Annotate highest peak
    max_idx = monthly_sales['Sales_Amount'].idxmax()
    peak_month = monthly_sales.loc[max_idx, 'Month_Str']
    peak_val = monthly_sales.loc[max_idx, 'Sales_Amount']
    ax1.annotate(f"Peak: ${peak_val:,.0f}", 
                 xy=(peak_month, peak_val), 
                 xytext=(max_idx - 1, peak_val + 2000),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6),
                 fontweight='bold', color='#d62728')
    
    plt.tight_layout()
    chart1_path = os.path.join(output_dir, 'task5_1_line_chart.png')
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[1/5] Line Chart saved to: {chart1_path}")
    print("Explanation 1: The line chart illustrates the monthly sales velocity across 2024. It reveals peak revenue periods driven by seasonal promotional campaigns.")

    # -------------------------------------------------------------
    # 2. BAR CHART: Total Sales Revenue by Product Category
    # -------------------------------------------------------------
    cat_sales = df.groupby('Product_Category')['Sales_Amount'].sum().sort_values(ascending=False)
    
    fig2, ax2 = plt.subplots(figsize=(9, 5))
    colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#9467bd', '#8c564b']
    bars = ax2.bar(cat_sales.index, cat_sales.values, color=colors, edgecolor='black', linewidth=0.8, width=0.6)
    ax2.set_title("Total Sales Revenue by Product Category", fontsize=14, fontweight='bold', pad=12)
    ax2.set_xlabel("Product Category", fontsize=11, fontweight='bold')
    ax2.set_ylabel("Total Revenue ($)", fontsize=11, fontweight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f"${height:,.0f}",
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 4), textcoords="offset points",
                     ha='center', va='bottom', fontsize=9, fontweight='bold')
                     
    plt.tight_layout()
    chart2_path = os.path.join(output_dir, 'task5_2_bar_chart.png')
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[2/5] Bar Chart saved to: {chart2_path}")
    print("Explanation 2: The bar chart clearly compares total sales volume across product lines, confirming Electronics and Fashion as the primary revenue drivers.")

    # -------------------------------------------------------------
    # 3. PIE CHART: Regional Revenue Market Share
    # -------------------------------------------------------------
    region_sales = df.groupby('Region')['Sales_Amount'].sum()
    
    fig3, ax3 = plt.subplots(figsize=(7, 7))
    explode = (0.05, 0, 0, 0)
    pie_colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2']
    wedges, texts, autotexts = ax3.pie(
        region_sales.values, 
        labels=region_sales.index, 
        autopct='%1.1f%%',
        startangle=140, 
        explode=explode, 
        colors=pie_colors,
        wedgeprops=dict(edgecolor='black', linewidth=1.2),
        textprops=dict(fontsize=11)
    )
    for at in autotexts:
        at.set_color('white')
        at.set_weight('bold')
        
    ax3.set_title("Sales Revenue Distribution by Geographic Region", fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    chart3_path = os.path.join(output_dir, 'task5_3_pie_chart.png')
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print(f"[3/5] Pie Chart saved to: {chart3_path}")
    print("Explanation 3: The pie chart showcases regional market share proportions, highlighting the North and South regions as commanding the largest combined revenue share.")

    # -------------------------------------------------------------
    # 4. HISTOGRAM: Customer Age Distribution
    # -------------------------------------------------------------
    fig4, ax4 = plt.subplots(figsize=(9, 5))
    n, bins, patches = ax4.hist(df['Customer_Age'], bins=15, color='#3498db', edgecolor='black', alpha=0.75)
    
    age_mean = df['Customer_Age'].mean()
    age_median = df['Customer_Age'].median()
    
    ax4.axvline(age_mean, color='red', linestyle='--', linewidth=2, label=f"Mean Age: {age_mean:.1f}")
    ax4.axvline(age_median, color='green', linestyle='-', linewidth=2, label=f"Median Age: {age_median:.1f}")
    
    ax4.set_title("Distribution of Customer Age", fontsize=14, fontweight='bold', pad=12)
    ax4.set_xlabel("Customer Age (Years)", fontsize=11, fontweight='bold')
    ax4.set_ylabel("Number of Customers (Frequency)", fontsize=11, fontweight='bold')
    ax4.legend(loc='upper right', frameon=True)
    ax4.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    chart4_path = os.path.join(output_dir, 'task5_4_histogram.png')
    plt.savefig(chart4_path, dpi=300)
    plt.close()
    print(f"[4/5] Histogram saved to: {chart4_path}")
    print("Explanation 4: The histogram shows a bell-shaped, approximately normal distribution of customer ages centered around 35 years, identifying young professionals as the primary user base.")

    # -------------------------------------------------------------
    # 5. SCATTER PLOT: Sales Amount vs Profit
    # -------------------------------------------------------------
    fig5, ax5 = plt.subplots(figsize=(9, 5.5))
    scatter = ax5.scatter(df['Sales_Amount'], df['Profit'], 
                          c=df['Discount_Percent'], cmap='viridis', 
                          alpha=0.75, edgecolors='black', linewidth=0.5, s=45)
    
    # Regression trendline
    m, b = np.polyfit(df['Sales_Amount'], df['Profit'], 1)
    ax5.plot(df['Sales_Amount'], m*df['Sales_Amount'] + b, color='red', linestyle='-', linewidth=2, label=f'Trendline (Slope = {m:.2f})')
    
    cbar = plt.colorbar(scatter, ax=ax5)
    cbar.set_label('Discount Percentage (%)', fontsize=10, fontweight='bold')
    
    ax5.set_title("Scatter Plot: Sales Amount vs. Profit", fontsize=14, fontweight='bold', pad=12)
    ax5.set_xlabel("Sales Amount ($)", fontsize=11, fontweight='bold')
    ax5.set_ylabel("Profit ($)", fontsize=11, fontweight='bold')
    ax5.legend(loc='upper left', frameon=True)
    ax5.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    chart5_path = os.path.join(output_dir, 'task5_5_scatter_plot.png')
    plt.savefig(chart5_path, dpi=300)
    plt.close()
    print(f"[5/5] Scatter Plot saved to: {chart5_path}")
    print("Explanation 5: The scatter plot reveals a strong positive linear relationship between Sales Amount and Profit, while color shading shows that transactions with higher discounts yield lower relative profit margins.")

    # -------------------------------------------------------------
    # COMBINED 5-PANEL FIGURE FOR REPORT SUBMISSION
    # -------------------------------------------------------------
    fig_all = plt.figure(figsize=(16, 12))
    gs = fig_all.add_gridspec(3, 2, hspace=0.35, wspace=0.25)
    
    # 1. Line
    ax1 = fig_all.add_subplot(gs[0, 0])
    ax1.plot(monthly_sales['Month_Str'], monthly_sales['Sales_Amount'], color='#1f77b4', marker='o', linewidth=2)
    ax1.set_title("1. Line Chart: Monthly Sales Trend", fontweight='bold')
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Sales ($)")
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    # 2. Bar
    ax2 = fig_all.add_subplot(gs[0, 1])
    ax2.bar(cat_sales.index, cat_sales.values, color=colors, edgecolor='black', alpha=0.85)
    ax2.set_title("2. Bar Chart: Revenue by Category", fontweight='bold')
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Revenue ($)")
    ax2.tick_params(axis='x', rotation=25)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    
    # 3. Pie
    ax3 = fig_all.add_subplot(gs[1, 0])
    ax3.pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%', 
            startangle=140, colors=pie_colors, wedgeprops=dict(edgecolor='black'))
    ax3.set_title("3. Pie Chart: Regional Revenue Share", fontweight='bold')
    
    # 4. Hist
    ax4 = fig_all.add_subplot(gs[1, 1])
    ax4.hist(df['Customer_Age'], bins=15, color='#3498db', edgecolor='black', alpha=0.75)
    ax4.axvline(age_mean, color='red', linestyle='--', label=f"Mean: {age_mean:.1f}")
    ax4.set_title("4. Histogram: Customer Age Distribution", fontweight='bold')
    ax4.set_xlabel("Age (Years)")
    ax4.set_ylabel("Count")
    ax4.legend()
    ax4.grid(True, linestyle='--', alpha=0.5)
    
    # 5. Scatter (spanning bottom row)
    ax5 = fig_all.add_subplot(gs[2, :])
    sc = ax5.scatter(df['Sales_Amount'], df['Profit'], c=df['Discount_Percent'], cmap='viridis', s=35, alpha=0.7)
    ax5.plot(df['Sales_Amount'], m*df['Sales_Amount'] + b, color='red', linestyle='-', linewidth=2, label=f'Trendline (m={m:.2f})')
    cbar = plt.colorbar(sc, ax=ax5, orientation='vertical')
    cbar.set_label('Discount (%)')
    ax5.set_title("5. Scatter Plot: Sales vs. Profit (Color: Discount %)", fontweight='bold')
    ax5.set_xlabel("Sales Amount ($)")
    ax5.set_ylabel("Profit ($)")
    ax5.legend()
    ax5.grid(True, linestyle='--', alpha=0.5)
    
    combined_path = os.path.join(output_dir, 'task5_all_matplotlib_visualizations.png')
    plt.savefig(combined_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\n[Combined Master Figure] saved to: {combined_path}")
    print("=" * 70)

if __name__ == '__main__':
    generate_visualizations()
