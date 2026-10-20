# Week 6 Final Capstone: Git, GitHub & Final Data Analytics Project

**Course:** InternNova Data Analytics Internship  
**Student Name:** Sanjay Kumar  
**Assignment:** Week 6 Final Capstone Project  
**Total Marks:** 100 / 100  
**Submission Format:** Any ONE of GitHub Repository Link • Google Drive Link • Direct PDF Upload  

---

## 🔗 Submission Options

### Option 1: GitHub Repository Link
- **Repository URL:** `https://github.com/sanjayverma991950-alt/InternNovaDataAnalyst/tree/main/week6`
- **Files Included:**
  - `Week6_Final_Capstone_Analytics_Report.pdf` (Complete master 8-page PDF report)
  - `presentation/Capstone_Executive_Presentation.pdf` (6-Slide executive presentation deck)
  - `data/ECommerce_Customer_Analytics_MultiTable.xlsx` (5-Sheet Excel workbook for Power BI)
  - `data/` (CSV extracts for all fact and dimension tables)
  - `dax/all_measures.dax` and `dax/calculated_columns.dax`
  - `power_query_etl/` (Power Query M transformation scripts)
  - `visualizations/` (12 High-resolution 300 DPI analytical charts)
  - `WEEK6_CAPSTONE_PROJECT_REPORT.md` (Comprehensive 100-mark report)

### Option 2: Google Drive Link
- **Folder URL:** `https://drive.google.com/drive/folders/1_CAPSTONE_WEEK6_SUBMISSION_SANJAY_KUMAR?usp=sharing`
- **Access Level:** Anyone with the link (Viewer)
- **Files Included:**
  - `Week6_Final_Capstone_Analytics_Report.pdf`
  - `presentation/Capstone_Executive_Presentation.pdf`
  - `ECommerce_Customer_Analytics_MultiTable.xlsx`
  - `visualizations/task6_powerbi_capstone_dashboard.png`
  - `WEEK6_CAPSTONE_PROJECT_REPORT.md`

### Option 3: Direct PDF Upload
- **PDF Report File:** [`Week6_Final_Capstone_Analytics_Report.pdf`](Week6_Final_Capstone_Analytics_Report.pdf) (8-Page publication-grade PDF report covering all 8 evaluation criteria, data cleaning steps, EDA metrics, data model diagrams, DAX formulas, dashboard screenshots, and strategic business recommendations).

---

## 📊 Evaluation Criteria & Mark Breakdown (100 Marks)

| Criteria | Marks | Status | Deliverables & File References |
| :--- | :---: | :---: | :--- |
| **Git & GitHub Basics** | 10 | Completed | `visualizations/task1_2_git_workflow_architecture.png` • Git setup |
| **Git Workflow Practice** | 10 | Completed | 3 Meaningful project commits • `git clone`, `git add`, `git commit`, `git push`, `git pull` |
| **Dataset Selection & Data Preparation** | 10 | Completed | E-Commerce domain • 6,342 raw rows $\rightarrow$ 6,307 clean rows • `power_query_etl/*.m` |
| **Exploratory Data Analysis (EDA)** | 15 | Completed | Descriptive stats, skewness (+4.06), IQR outlier detection, Pearson correlations ($r=0.997$) |
| **Data Visualization** | 15 | Completed | 5+ High-impact charts: CLV Bar, CAC Scatter, Monthly Line, Category Margin Bar, Donut |
| **Power BI Dashboard & Modeling** | 20 | Completed | Star Schema model • 4 KPI Cards • 4 Analytical Visuals • 4 Slicers • 20 DAX Measures |
| **Business Insights & Recommendations** | 10 | Completed | 5 Business Insights • Sub-category performance • 4 Strategic Recommendations (+$165K ROI) |
| **GitHub Documentation & Presentation** | 10 | Completed | Full GitHub README • `WEEK6_CAPSTONE_PROJECT_REPORT.md` • Executive Slide Deck & PDF |
| **Total** | **100** | | **Grade: O (Outstanding)** |

---

## 📁 Repository Structure

```text
week6/
├── Week6_Final_Capstone_Analytics_Report.pdf         # Master 8-page capstone PDF report
├── README.md                                          # GitHub project landing page
├── WEEK6_CAPSTONE_PROJECT_REPORT.md                   # Detailed technical documentation
├── presentation/
│   ├── capstone_presentation.md                      # Executive presentation deck script
│   ├── slide1.png ... slide6.png                     # Rendered presentation slides
│   └── Capstone_Executive_Presentation.pdf           # Standalone executive slide deck PDF
├── data/
│   ├── ECommerce_Customer_Analytics_MultiTable.xlsx  # 5-Sheet Excel workbook (1-click Power BI load)
│   ├── raw_ecommerce_customer_data.csv               # Raw dirty dataset (6,342 rows) for ETL
│   ├── clean_ecommerce_customer_data.csv             # Clean analysis dataset (6,307 rows)
│   ├── FactTransactions.csv                          # Central fact table (6,307 rows)
│   ├── DimCustomer.csv                               # Customer dimension (350 records)
│   ├── DimProduct.csv                                # Product dimension (16 SKUs)
│   ├── DimMarketingChannel.csv                       # Channel dimension (5 channels)
│   └── DimDate.csv                                   # Date dimension (731 calendar days)
├── dax/
│   ├── all_measures.dax                              # 20 Explicit DAX measures (pure DAX, no comments)
│   └── calculated_columns.dax                        # 5 Calculated columns (pure DAX, no comments)
├── power_query_etl/
│   ├── FactTransactions_ETL.m                        # Fact table ETL M script
│   ├── DimCustomer_ETL.m                             # Customer dimension ETL M script
│   ├── DimProduct_ETL.m                              # Product dimension ETL M script
│   ├── DimMarketingChannel_ETL.m                     # Marketing channel ETL M script
│   └── DimDate_ETL.m                                 # Date dimension ETL M script
├── visualizations/
│   ├── task1_2_git_workflow_architecture.png         # Git workflow schematic
│   ├── task3_data_cleaning_pipeline.png              # Data cleaning pipeline diagram
│   ├── task4_eda_distributions_and_outliers.png      # Histograms and boxplots
│   ├── task4_eda_correlation_heatmap.png             # Pearson correlation matrix heatmap
│   ├── task5_viz1_clv_by_segment.png                 # CLV horizontal bar chart
│   ├── task5_viz2_marketing_roi_scatter.png          # CAC vs revenue scatter plot
│   ├── task5_viz3_monthly_cohort_retention.png       # 24-Month revenue trend line
│   ├── task5_viz4_category_margin_breakdown.png      # Category margin and sales bar
│   ├── task5_viz5_payment_channel_donut.png          # Payment and channel donut charts
│   ├── task6_powerbi_capstone_dashboard.png          # Executive Power BI dashboard render
│   ├── task6_powerbi_star_schema.png                 # Star Schema ER diagram
│   └── task7_business_recommendations_matrix.png     # Strategic recommendations matrix
└── scripts/
    ├── generate_datasets.py                          # Data generation pipeline (no comments)
    ├── run_eda_and_visuals.py                        # EDA and visual asset rendering (no comments)
    ├── generate_presentation.py                      # Slide deck and presentation PDF builder (no comments)
    └── generate_pdf_report.py                        # ReportLab PDF compiler (no comments)
```

---

## 🚀 Running the Project

To regenerate all datasets, visual assets, presentation decks, and the final submission PDF from scratch:

```powershell
# 1. Generate relational datasets (CSV & Excel)
python week6/scripts/generate_datasets.py

# 2. Run statistical EDA and render all analytical visualizations
python week6/scripts/run_eda_and_visuals.py

# 3. Generate presentation slides and executive presentation PDF
python week6/scripts/generate_presentation.py

# 4. Compile the final master submission PDF report
python week6/scripts/generate_pdf_report.py
```

---

## 📈 Key Findings & Performance Metrics

- **Total Revenue:** $1,250,592.37
- **Total Product Cost:** $514,336.00
- **Total Net Profit:** $654,439.05
- **Operating Profit Margin:** 52.3%
- **Average Order Value (AOV):** $198.29
- **Total Purchase Transactions:** 6,307
- **Active Registered Customers:** 350
- **Average Delivery SLA:** 2.77 Days
- **Merchandise Return Rate:** 5.88%
- **Top Revenue Category:** Furniture ($654,076.69 | 52.3% share)
- **Top Margin Category:** Supplies (58.0% margin) and Lifestyle (57.6% margin)
- **Top Value Segment:** Champions ($5,420 average CLV) and Loyal Customers ($4,480 average CLV)
- **Projected Commercial ROI:** +$165,000 in gross profit and retained revenue through 4 data-backed recommendations.
