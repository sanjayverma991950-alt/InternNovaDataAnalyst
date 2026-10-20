# Omnichannel E-Commerce Customer Analytics & Lifetime Value Optimization
## Final Capstone Project Presentation | InternNova Data Analytics Internship

**Presenter:** Sanjay Kumar  
**Domain:** E-Commerce, Retail Customer Analytics & Business Intelligence  
**Tools:** Python (Pandas, NumPy, Matplotlib, Seaborn), Power BI Desktop, DAX, Git/GitHub  

---

## Slide 1: Executive Overview & Project Title
- **Project Title:** Omnichannel E-Commerce Customer Analytics & Lifetime Value Optimization
- **Core Objective:** Deliver an end-to-end analytical framework to optimize customer acquisition costs (CAC), improve customer lifetime value (CLV), evaluate product profitability, and identify churn risk across multi-channel retail operations.
- **Key Metrics:** $1.25M Revenue, $654K Net Profit, 52.3% Operating Margin, 6,307 Transactions, 350 Active Customers.

---

## Slide 2: Business Problem Statement & Objectives
- **Problem 1 (Uneven Customer Lifetime Value):** High divergence in customer lifetime value between Champions ($5,420 CLV) and At-Risk / Hibernating segments ($1,920 - $2,830 CLV).
- **Problem 2 (Marketing Attribution Imbalance):** Paid Search drives high acquisition costs ($48 CAC) with sub-optimal ROAS compared to Organic and Retention Email Newsletter channels ($8 - $12.50 CAC).
- **Problem 3 (Category Margin Variance):** Furniture dominates top-line revenue ($654K, 52.3% share), but requires careful bundling with high-margin accessories to preserve basket profitability.
- **Project Objectives:**
  1. Build an automated data cleaning and normalization pipeline.
  2. Perform comprehensive exploratory data analysis and outlier detection.
  3. Deploy a production-grade Star Schema Power BI model with dynamic DAX measures.
  4. Formulate four data-backed strategic recommendations with projected financial ROI.

---

## Slide 3: Dataset Architecture & Power Query ETL
- **Raw Ingestion Feed:** 6,342 records with artificial noise (35 duplicates, null phone numbers, mixed casing, non-standard date formats).
- **Power Query M Transformations:**
  - Removed duplicates on composite keys.
  - Imputed missing phone and contact numbers.
  - Standardized payment methods (Credit Card, PayPal, Debit Card, Apple Pay, BNPL).
  - Explicitly cast column types to Date, Decimal Currency, and Integer.
- **Relational Star Schema:**
  - `FactTransactions` (6,307 rows)
  - `DimCustomer` (350 rows)
  - `DimProduct` (16 rows)
  - `DimMarketingChannel` (5 rows)
  - `DimDate` (731 rows)

---

## Slide 4: Exploratory Data Analysis & Statistical Discoveries
- **Descriptive Statistics:**
  - Mean Sales: $198.29 | Median Sales: $149.00 (Positive Skewness: 4.06).
  - Fulfillment SLA: 2.77 Days average delivery turnaround.
  - Return Rate: 5.88% across all order types.
- **Correlation Insights:**
  - Sales & Profit: Strong positive linear correlation ($r = 0.997$).
  - Sales & Quantity: Moderate positive correlation ($r = 0.446$).
  - Sales & Delivery Days: Uncorrelated ($r = 0.010$), confirming fulfillment reliability across all ticket sizes.
- **Outlier Analysis:**
  - IQR non-parametric fencing detected 284 high-ticket enterprise transactions ($>$ $489 upper fence).

---

## Slide 5: Interactive Power BI Dashboard
- **Layout:** Executive dark-slate architecture (`#0F172A`) with F-pattern hierarchy.
- **KPI Deck:** Total Revenue ($1.25M), Net Profit ($654K), Profit Margin (52.3%), Unique Customers (350).
- **Analytical Views:**
  - Clustered Bar: Category Sales Volume vs Net Profit.
  - Chronological Line: 24-Month Revenue Trajectory with seasonal Q4 surges.
  - Donut Chart: Channel Attribution and Payment Method Distribution.
  - Regional Matrix: Performance across West, South, Central, and East territories.
- **Dynamic Cross-Filtering:** 4 Slicers enabling real-time slice-and-dice across channel, segment, year, and geography.

---

## Slide 6: Strategic Recommendations & ROI Projections
- **Recommendation 1 (Automated Loyalty Win-Back):** Target 'At Risk' customers ($172K sales) with targeted re-engagement email workflows.
  - *Expected Impact:* +$45,000 retained annual revenue.
- **Recommendation 2 (Marketing Budget Reallocation):** Shift 25% of paid ad budget from Paid Search ($48 CAC) to Email and Organic Content ($8 - $12.50 CAC).
  - *Expected Impact:* +18% increase in blended ROAS.
- **Recommendation 3 (Checkout Accessory Bundling):** Bundle premium office seating and desks with high-margin cable sleeves and riser accessories.
  - *Expected Impact:* +$60,000 incremental gross profit.
- **Recommendation 4 (Fulfillment SLA Optimization):** Standardize delivery to 1-2 day express tiers.
  - *Expected Impact:* 1.8% reduction in return rates and improved customer satisfaction scores.
