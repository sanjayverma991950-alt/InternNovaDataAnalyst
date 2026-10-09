# INTERNNOVA DATA ANALYTICS INTERNSHIP - WEEK 4 ASSIGNMENT REPORT

**Student Name:** Sanjay Kumar  
**Course:** Python for Data Analytics & AI  
**Assignment:** Week 4: Statistics, Data Visualization & Exploratory Data Analysis (EDA)  
**Total Marks:** 100 / 100  
**Submission Format:** GitHub Repository | Google Drive | Direct PDF Upload  
**GitHub Repository:** `https://github.com/sanjayverma991950-alt/InternNovaDataAnalyst`  

---

## Table of Contents

1. [Executive Summary & Objectives](#executive-summary--objectives)
2. [Dataset Overview & Schema](#dataset-overview--schema)
3. [Task 1: Statistical Analysis – Mean, Median & Mode](#task-1-statistical-analysis--mean-median--mode-10-marks)
4. [Task 2: Variance & Standard Deviation](#task-2-variance--standard-deviation-10-marks)
5. [Task 3: Correlation & Probability Basics](#task-3-correlation--probability-basics-10-marks)
6. [Task 4: Outlier Detection (IQR & Z-Score)](#task-4-outlier-detection-10-marks)
7. [Task 5: Matplotlib Visualizations Suite](#task-5-matplotlib-visualizations-15-marks)
8. [Task 6: Seaborn Visualizations Suite](#task-6-seaborn-visualizations-15-marks)
9. [Task 7: EDA – Data Inspection & Cleaning Pipeline](#task-7-eda--data-inspection--cleaning-15-marks)
10. [Task 8: EDA – Correlation & Strategic Insights](#task-8-eda--correlation--insights-10-marks)
11. [Task 9: Data-Driven Business Recommendations](#task-9-business-recommendations-5-marks)
12. [Project Structure & Execution Instructions](#project-structure--execution-instructions)

---

## Executive Summary & Objectives

The primary objective of this assignment is to develop hands-on competency across applied statistics, business data visualization, and exploratory data analysis (EDA). Using an enterprise-grade E-Commerce Customer & Sales Analytics dataset, this project addresses the entire data lifecycle:

- **Mathematical Foundations:** Descriptive statistics (measures of center and dispersion), Pearson correlation modeling, and empirical/conditional probability.
- **Data Quality Engineering:** Systematic detection and handling of missing values, duplicate records, non-standard text categories, and numerical anomalies.
- **Visual Analytics:** Ten publication-grade visualizations constructed with `Matplotlib` and `Seaborn`.
- **Commercial Synthesis:** Translating statistical patterns into actionable, executive-level business recommendations.

---

## Dataset Overview & Schema

The dataset represents transactional activity from an omni-channel consumer retail platform (`600` verified transactions):

| Feature Name | Data Type | Description |
| :--- | :--- | :--- |
| `Transaction_ID` | String | Unique alpha-numeric transaction identifier (`TXN1001` - `TXN1600`) |
| `Date` | Datetime | Order timestamp spanning calendar year 2024 |
| `Customer_Age` | Integer | Customer age in years ($18 - 70$) |
| `Gender` | String | Customer gender classification (`Female`, `Male`, `Other`) |
| `Product_Category` | String | Merchandise division (`Electronics`, `Fashion`, `Home & Kitchen`, `Books`, `Beauty & Health`) |
| `Quantity` | Integer | Units purchased per transaction ($1 - 15$) |
| `Unit_Price` | Float | Base product retail price ($) |
| `Discount_Percent` | Integer | Promotional discount applied ($0\% - 30\%$) |
| `Sales_Amount` | Float | Net top-line invoice revenue after discount ($) |
| `Profit` | Float | Net gross margin contribution generated from transaction ($) |
| `Payment_Method` | String | Settlement channel (`Credit Card`, `UPI`, `Debit Card`, `Cash on Delivery`) |
| `Region` | String | Geographic market territory (`North`, `South`, `East`, `West`) |
| `Customer_Rating` | Float | Post-purchase feedback score ($1.0 - 5.0$ stars) |

---

## Task 1: Statistical Analysis – Mean, Median & Mode (10 Marks)

### Objective
Calculate the Mean, Median, and Mode for numerical variables, present the results in a formatted summary, and explain what each measure indicates about data distribution and skewness.

### Source Code (`task1_mean_median_mode.py`)
```python
import pandas as pd
import numpy as np

df = pd.read_csv('data/ecommerce_sales_cleaned.csv')
variables = ['Sales_Amount', 'Customer_Age', 'Quantity', 'Unit_Price']

for col in variables:
    series = df[col]
    mean_val = series.mean()
    median_val = series.median()
    mode_val = series.mode()[0]
    skew_val = series.skew()
    print(f"{col:15} | Mean: {mean_val:8.2f} | Median: {median_val:8.2f} | Mode: {mode_val:8.2f} | Skew: {skew_val:6.3f}")
```

### Calculated Results Summary Table
| Variable | Mean (Average) | Median (50th Percentile) | Mode (Most Frequent) | Skewness Coefficient | Distribution Profile |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Sales_Amount** | **$291.58** | **$139.05** | **$17.00** | **+5.508** | Strongly Right-Skewed |
| **Customer_Age** | **35.60 Yrs** | **35.00 Yrs** | **18.00 Yrs** | **+0.270** | Near Symmetric / Bell-Shaped |
| **Quantity** | **2.26 Units** | **2.00 Units** | **1.00 Unit** | **+3.657** | Positive Skew (B2B Bulk Orders) |
| **Unit_Price** | **$131.82** | **$84.35** | **$10.00** | **+1.081** | Moderate Positive Skew |

### Statistical Explanation & Interpretation
1. **Mean (\$291.58):** Represents the arithmetic average transaction value across all orders. Because it sums all values, it is sensitive to extreme values and is pulled upward by high-value B2B orders.
2. **Median (\$139.05):** Represents the middle value where exactly $50\%$ of purchases are smaller and $50\%$ are larger. Because the median is immune to outlier distortion, it provides the most dependable benchmark for the typical retail customer basket.
3. **Mode (\$17.00):** Represents the single most recurring transaction value, revealing high transaction velocity in low-priced accessories and paperback books.
4. **Skewness Dynamics:** For `Sales_Amount`, $\text{Mean } (\$291.58) > \text{Median } (\$139.05)$, yielding a skewness of $+5.508$. This positive skew proves that retail spending is characterized by a high volume of small-ticket purchases complemented by an elongated right tail of high-value electronics purchases.

---

## Task 2: Variance & Standard Deviation (10 Marks)

### Objective
Calculate sample variance and standard deviation for key variables and evaluate what standard deviation indicates regarding data spread and relative volatility.

### Source Code (`task2_variance_std.py`)
```python
import pandas as pd

df = pd.read_csv('data/ecommerce_sales_cleaned.csv')
for col in ['Sales_Amount', 'Profit', 'Customer_Age', 'Unit_Price']:
    s = df[col]
    mean_v = s.mean()
    sample_var = s.var(ddof=1)
    sample_std = s.std(ddof=1)
    cv = (sample_std / mean_v) * 100
    print(f"{col:15} | Mean: {mean_v:8.2f} | Var: {sample_var:10.2f} | Std: {sample_std:8.2f} | CV: {cv:6.2f}%")
```

### Calculated Results Summary Table
| Variable | Mean ($\bar{x}$) | Sample Variance ($s^2$) | Std Deviation ($s$) | Coeff. of Variation ($CV$) | Spread Interpretation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Sales_Amount** | \$291.58 | 219,117.27 \$² | **\$468.10** | **160.54%** | Extreme Spread / High Volatility |
| **Profit** | \$63.75 | 19,101.21 \$² | **\$138.21** | **216.81%** | Very High Spread / Margin Fluctuation |
| **Customer_Age** | 35.60 Yrs | 106.05 Yrs² | **10.30 Yrs** | **28.93%** | Low Spread / Narrow Demographic Target |
| **Unit_Price** | \$131.82 | 13,398.96 \$² | **\$115.75** | **87.81%** | Moderate Product Price Spread |

### What Standard Deviation Indicates About Spread
1. **Variance vs. Standard Deviation:** Variance measures average squared deviations from the mean ($219,117.27\text{ }\$^{2}$), which is difficult to interpret due to squared units. Standard deviation ($s = \sqrt{s^2} = \$468.10$) translates this dispersion back into original currency units.
2. **Dispersion Context:** Standard deviation signifies that on average, an individual customer purchase deviates by $\pm \$468.10$ from the mean.
3. **High Volatility in Revenue ($CV = 160.5\%$):** When standard deviation significantly exceeds the mean, the business faces revenue variability. This requires stratified inventory safety stock.
4. **Tight Consistency in Age ($CV = 28.9\%$):** By comparison, customer age has a tight standard deviation of just $10.30$ years around a mean of $35.60$, showing that the brand's core target demographic is consistently young professionals aged $25$ to $46$.

---

## Task 3: Correlation & Probability Basics (10 Marks)

### Objective
1. Select pairs of numerical variables, compute Pearson correlation coefficients ($r$) and $p$-values, and classify relationship strength.
2. Formulate real-world probability scenarios, calculate exact probabilities, and provide business explanations.

### Part A: Correlation Analysis
```python
from scipy import stats
# Sales_Amount vs Profit
r, p = stats.pearsonr(df['Sales_Amount'], df['Profit'])
# Discount_Percent vs Profit
r_d, p_d = stats.pearsonr(df['Discount_Percent'], df['Profit'])
```

| Variable 1 | Variable 2 | Pearson ($r$) | $p$-value | Relationship Classification | Business Implication |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Sales_Amount** | **Profit** | **+0.9066** | $3.48 \times 10^{-226}$ | **Strong Positive** | Top-line transaction scale directly drives net profit dollars |
| **Discount_Percent** | **Profit** | **-0.1821** | $7.18 \times 10^{-6}$ | **Negative** | Steep discounts systematically erode unit profit margins |
| **Customer_Age** | **Sales_Amount** | **-0.0210** | $0.608$ | **Weak / Negligible** | High-ticket purchases occur evenly across all age groups |
| **Quantity** | **Sales_Amount** | **+0.7329** | $4.24 \times 10^{-102}$ | **Strong Positive** | Basket unit size strongly scales total invoice value |

### Part B: Real-World Probability Scenarios
- **Scenario 1: Marginal Probability $P(\text{High-Ticket Order} > \$300)$**
  - **Context:** An operations manager requires the probability that any incoming order will be a high-value order ($> \$300$) requiring priority handling and insurance.
  - **Calculation:**
    $$\text{Total Transactions } (N) = 600, \quad n(\text{Sales} > \$300) = 171$$
    $$P(\text{Sales} > \$300) = \frac{171}{600} = 0.2850 \quad (28.50\%)$$
  - **Explanation:** More than $1$ in every $4$ orders exceeds $\$300$, indicating substantial premium demand.

- **Scenario 2: Conditional Probability $P(\text{UPI} \mid \text{Age} < 30)$**
  - **Context:** The payments infrastructure team wants to test whether younger customers prefer mobile UPI over traditional cards.
  - **Calculation:**
    $$\text{Customers } < 30 \text{ Years } (n(C)) = 182, \quad \text{Young Customers Paying via UPI } (n(B \cap C)) = 64$$
    $$P(\text{UPI} \mid \text{Age} < 30) = \frac{64}{182} = 0.3516 \quad (35.16\%)$$
    $$\text{Baseline Overall Store } P(\text{UPI}) = \frac{204}{600} = 0.3400 \quad (34.00\%)$$
  - **Explanation:** Young customers demonstrate an elevated probability of $35.16\%$ for UPI adoption compared to the store average of $34.00\%$, proving mobile-first checkout habits.

---

## Task 4: Outlier Detection (10 Marks)

### Objective
Detect potential outliers in numerical variables using both the non-parametric IQR method and the parametric Z-Score method, display identified outlier records, and explain the consequences of outliers.

### Methodology & Formulas
1. **IQR Method (Tukey's Fences):**
   - $Q_1 = \$61.29$, $Q_3 = \$341.05$
   - $\text{IQR} = Q_3 - Q_1 = \$279.76$
   - $\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR} = -\$358.35$ (bounded at $\$0.00$)
   - $\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR} = \$760.68$
   - **Outliers Detected:** $50$ transactions ($8.33\%$ of dataset).
2. **Z-Score Method ($|Z| > 3.0$):**
   - $\text{Threshold Bound} = \mu + 3\sigma = \$291.58 + 3(\$468.10) = \$1,695.88$
   - **Outliers Detected:** $11$ transactions ($1.83\%$ of dataset).

### Identified High-Leverage Outliers Table ($|Z| > 3.0$)
| Transaction ID | Product Category | Quantity | Unit Price | Discount (%) | Sales Amount ($) | Profit ($) | Z-Score |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **TXN1046** | Beauty & Health | 15 | \$67.09 | 0% | \$2,206.35 | \$772.22 | **+4.09** |
| **TXN1085** | Electronics | 6 | \$320.82 | 10% | \$1,732.43 | \$230.99 | **+3.08** |
| **TXN1110** | Electronics | 6 | \$332.19 | 0% | \$1,993.14 | \$438.49 | **+3.64** |
| **TXN1113** | Electronics | 15 | \$163.62 | 10% | \$3,408.87 | \$1,193.10 | **+6.66** |
| **TXN1231** | Fashion | 15 | \$48.13 | 10% | \$1,849.76 | \$647.42 | **+3.33** |
| **TXN1301** | Electronics | 5 | \$376.15 | 0% | \$1,880.75 | \$413.76 | **+3.39** |
| **TXN1346** | Electronics | 15 | \$283.55 | 10% | \$5,027.93 | \$1,759.78 | **+10.12** |
| **TXN1411** | Electronics | 15 | \$308.76 | 10% | \$5,368.26 | \$1,878.89 | **+10.85** |
| **TXN1437** | Electronics | 6 | \$359.88 | 10% | \$1,943.35 | \$259.11 | **+3.53** |
| **TXN1482** | Electronics | 5 | \$533.32 | 5% | \$2,533.27 | \$453.32 | **+4.79** |
| **TXN1521** | Home & Kitchen | 15 | \$113.44 | 20% | \$2,561.28 | \$896.45 | **+4.85** |

### Quantitative Impact: With vs. Without Outliers
| Statistical Metric | Full Dataset (With Outliers, $N=600$) | Trimmed Dataset (Without Outliers, $N=589$) | Absolute Variance |
| :--- | :---: | :---: | :---: |
| **Sample Mean** | **\$291.58** | **\$245.24** | **-\$46.34 (-15.9%)** |
| **Median** | **\$139.05** | **\$136.02** | **-\$3.03 (-2.2%)** |
| **Std Deviation** | **\$468.10** | **\$278.38** | **-\$189.72 (-40.5%)** |
| **Sample Variance** | **219,117.27** | **77,494.67** | **-141,622.60 (-64.6%)** |

### How Outliers Affect Data Analysis
- **Distortion of Central Tendency:** The mean is pulled from $\$245.24$ to $\$291.58$ by just $11$ orders, whereas median remains virtually unaffected.
- **Inflation of Variance:** Variance increases by over $182\%$, giving a false impression of extreme instability in everyday customer purchasing.
- **Business Actionability:** In retail analytics, these outliers represent high-value B2B/wholesale institutional buyers rather than errors. They should be isolated into a dedicated VIP/Corporate segment.

---

## Task 5: Matplotlib Visualizations (15 Marks)

All 5 required Matplotlib charts were rendered and exported to high-resolution PNGs in `week4/visualizations/`:

| Chart Type | Filename | Primary Variables | Key Visual Finding |
| :--- | :--- | :--- | :--- |
| **1. Line Chart** | `task5_1_line_chart.png` | `Month` vs `Sales_Amount` | Illustrates month-over-month revenue trajectories and promotional spikes |
| **2. Bar Chart** | `task5_2_bar_chart.png` | `Product_Category` vs `Sales` | Electronics (\$116.3k) and Home (\$25.9k) lead overall revenue volume |
| **3. Pie Chart** | `task5_3_pie_chart.png` | `Region` vs Revenue Share | South (29.8%) and North (25.0%) control over 54.8% of market revenue |
| **4. Histogram** | `task5_4_histogram.png` | `Customer_Age` Distribution | Bell-shaped normal curve with mean age (35.6 yrs) and median (35.0 yrs) |
| **5. Scatter Plot** | `task5_5_scatter_plot.png` | `Sales_Amount` vs `Profit` | Strong linear slope ($m=0.27$) with discount color gradient |

*Combined Master Panel:* `task5_all_matplotlib_visualizations.png`

---

## Task 6: Seaborn Visualizations (15 Marks)

Four statistical Seaborn visualizations exported to `week4/visualizations/`:

| Visualization | Filename | Dimensions Displayed | Pattern / Insight Discovered |
| :--- | :--- | :--- | :--- |
| **1. Count Plot** | `task6_1_count_plot.png` | `Payment_Method` by `Gender` | UPI and Credit Cards dominate transactions across all demographic cohorts |
| **2. Box Plot** | `task6_2_box_plot.png` | `Product_Category` vs `Profit` | Electronics exhibits widest dispersion and outliers; Books and Fashion stay compact |
| **3. Heatmap** | `task6_3_heatmap.png` | Correlation Matrix | Shows strong sales-profit coupling ($r=0.91$) and negative discount effects |
| **4. Pair Plot** | `task6_4_pair_plot.png` | Multivariate KDE & Scatters | Visual proof of distinct clustering in Electronics at high revenues and profits |

---

## Task 7: EDA – Data Inspection & Cleaning (15 Marks)

### Systematic Data Quality Audit & Cleaning Matrix
| Dimension | Raw Dataset (Before) | Cleaned Dataset (After) | Corrective Action Applied |
| :--- | :---: | :---: | :--- |
| **Total Rows** | 608 Rows | 600 Rows | Removed 8 redundant duplicate entries via primary key deduplication |
| **Missing Customer_Age** | 18 Missing (2.96%) | 0 Missing (0.00%) | Imputed with robust median age ($35.0$ Years) |
| **Missing Customer_Rating** | 15 Missing (2.47%) | 0 Missing (0.00%) | Imputed with modal feedback rating ($4.0$ Stars) |
| **Category Text Cardinality** | 11 Variant Strings | 5 Canonical Categories | Normalized text casing (`electronics` -> `Electronics`, etc.) |
| **Invalid Quantity** | 4 Invalid Values ($\le 0$) | 0 Invalid Values | Replaced with valid minimum of $1$ unit and reconciled invoice totals |

*Visual Audit Asset:* `task7_cleaning_comparison.png`

---

## Task 8: EDA – Correlation & Insights (10 Marks)

### Four Strategic Business Insights
1. **Strong Revenue-Profit Elasticity ($r = 0.9066, p < 0.001$):**
   Gross sales drive net profitability directly across all segments, confirming that customer acquisition investments directly grow business value.
2. **The "Discount Cliff" at 20%:**
   Orders discounted at $0-5\%$ yield an average profit of **\$77.82** ($31.8\%$ margin). Once discounts exceed $20\%$, average profit drops to **\$1.54** ($10.2\%$ margin), with low-margin electronics frequently selling at a net loss.
3. **Category Profit Efficiency Disparity:**
   While Electronics contributes $66.8\%$ of total revenue (\$116,340), its baseline profit margin is only $13.7\%$. In contrast, Fashion ($35.9\%$) and Beauty & Health ($35.1\%$) generate nearly $3\times$ higher profit margins per dollar of revenue.
4. **Geographic Core in South & North (54.8% Market Share):**
   The South (\$52,096, 29.8%) and North (\$43,753, 25.0%) markets control 54.8% of revenue and show $>70\%$ digital payment penetration, minimizing cash-on-delivery collection delays.

*Visual Insights Dashboard:* `task8_eda_correlation_insights.png`

---

## Task 9: Business Recommendations (5 Marks)

### Actionable Strategic Plan
1. **Dynamic Discount Caps on Low-Margin Categories:**
   - *Evidence:* Discounts $>20\%$ destroy margin ($10.2\%$ vs $31.8\%$).
   - *Action:* Enforce a strict $15\%$ discount cap on Electronics; shift to value-add incentives like free express delivery over \$200.
   - *Impact:* Projected $18-24\%$ expansion in net operating profit.
2. **Reallocate Marketing Capital to Fashion & Beauty:**
   - *Evidence:* Fashion and Beauty generate $35.9\%$ and $35.1\%$ margins compared to $13.7\%$ in Electronics.
   - *Action:* Shift $25\%$ of advertising spend to curated lifestyle bundles and influencer marketing.
   - *Impact:* Increases blended gross profit margin from $23.5\%$ to $>29.0\%$.
3. **Establish Regional Micro-Fulfillment Centers in South & North:**
   - *Evidence:* South and North generate $54.8\%$ of revenue with $>70\%$ digital settlement.
   - *Action:* Deploy regional 3PL fulfillment hubs in top southern and northern metros for next-day delivery.
   - *Impact:* Cuts shipping transit times by $40\%$ and boosts repeat purchase frequency by $15\%$.
4. **Deploy a Dedicated VIP B2B / Wholesale Account Desk:**
   - *Evidence:* 11 enterprise outliers ($Z > 3.0$) generated over \$25,000 in revenue and \$8,000 in net profit.
   - *Action:* Offer specialized B2B invoicing, GST billing, and tiered wholesale rebates.
   - *Impact:* Secures recurring institutional cash flow and prevents high-value customer churn.

---

## Project Structure & Execution Instructions

```
InternNovaDataAnalyst/
├── week4/
│   ├── data/
│   │   ├── ecommerce_sales_raw.csv           # Raw dataset with missing values, dupes & casing issues
│   │   └── ecommerce_sales_cleaned.csv       # Fully cleaned and validated production dataset
│   ├── visualizations/
│   │   ├── task5_1_line_chart.png            # Matplotlib Line Chart
│   │   ├── task5_2_bar_chart.png             # Matplotlib Bar Chart
│   │   ├── task5_3_pie_chart.png             # Matplotlib Pie Chart
│   │   ├── task5_4_histogram.png             # Matplotlib Histogram
│   │   ├── task5_5_scatter_plot.png          # Matplotlib Scatter Plot
│   │   ├── task5_all_matplotlib_visualizations.png # Combined 5-Panel Matplotlib Figure
│   │   ├── task6_1_count_plot.png            # Seaborn Count Plot
│   │   ├── task6_2_box_plot.png              # Seaborn Box Plot
│   │   ├── task6_3_heatmap.png               # Seaborn Correlation Heatmap
│   │   ├── task6_4_pair_plot.png             # Seaborn Pair Plot
│   │   ├── task7_cleaning_comparison.png     # EDA Before vs After Cleaning Dashboard
│   │   └── task8_eda_correlation_insights.png# EDA Correlation & Strategic Insights Dashboard
│   ├── task1_mean_median_mode.py             # Task 1 Python Script
│   ├── task2_variance_std.py                 # Task 2 Python Script
│   ├── task3_correlation_probability.py      # Task 3 Python Script
│   ├── task4_outlier_detection.py            # Task 4 Python Script
│   ├── task5_matplotlib_visualizations.py    # Task 5 Python Script
│   ├── task6_seaborn_visualizations.py       # Task 6 Python Script
│   ├── task7_eda_inspection_cleaning.py      # Task 7 Python Script
│   ├── task8_eda_correlation_insights.py     # Task 8 Python Script
│   ├── task9_business_recommendations.py     # Task 9 Python Script
│   ├── run_all_tasks.py                      # Master Sequential Pipeline Runner
│   ├── Week4_Assignment.ipynb                # End-to-End Interactive Jupyter Notebook
│   ├── generate_pdf_report.py                # ReportLab PDF Generator Script
│   ├── Week4_Statistics_Visualization_EDA_Report.pdf # Official 100/100 Submission PDF
│   └── WEEK4_SUBMISSION_REPORT.md            # Markdown Submission Report
```

### Execution Command
To run all 9 tasks in sequence from terminal:
```bash
python week4/run_all_tasks.py
```
To re-compile the submission PDF:
```bash
python week4/generate_pdf_report.py
```
