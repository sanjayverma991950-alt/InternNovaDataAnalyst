# InternNova Data Analytics Internship Portfolio

**Student Name:** Sanjay Kumar  
**Course:** Python for Data Analytics & AI  
**Repository:** [InternNovaDataAnalyst](https://github.com/sanjayverma991950-alt/InternNovaDataAnalyst)  

---

## 📌 Internship Roadmap & Submissions

| Week | Assignment Title | Key Topics Covered | Status | Links & Documentation |
| :---: | :--- | :--- | :---: | :--- |
| **Week 1** | Python Fundamentals & Basics | Variables, Operators, Loops, Functions, Collections, File I/O, Mini Project | ✅ Completed (100/100) | [Week 1 Report](SUBMISSION_REPORT.md) |
| **Week 2** | SQL & Relational Databases | Querying, Aggregations, Joins, Group By, Subqueries | ⏳ Completed | — |
| **Week 3** | Advanced Python & Data Structures | OOP, Data Structures, Algorithmic Thinking | ⏳ Completed | — |
| **Week 4** | Statistics, Data Visualization & EDA | Mean/Median/Mode, Variance/Std, Correlation, Outliers, Matplotlib, Seaborn, EDA Cleaning & Insights | ✅ Completed (100/100) | [Week 4 Report](week4/WEEK4_SUBMISSION_REPORT.md) • [PDF Report](week4/Week4_Statistics_Visualization_EDA_Report.pdf) • [Jupyter Notebook](week4/Week4_Assignment.ipynb) |
| **Week 5** | Power BI & Business Intelligence | Ingestion, Power Query ETL, Star Schema Modeling, DAX Measures, Dashboard, Insights | ✅ Completed (100/100) | [Week 5 Report](week5/WEEK5_SUBMISSION_REPORT.md) • [PDF Report](week5/Week5_Power_BI_Business_Intelligence_Report.pdf) • [Week 5 Folder](week5/) |
| **Week 6** | Git, GitHub & Final Data Analytics Project | Git Workflow, Omnichannel EDA, Visualizations, Power BI Dashboard, Strategic Recommendations | ✅ Completed (100/100) | [Week 6 Report](week6/WEEK6_CAPSTONE_PROJECT_REPORT.md) • [PDF Report](week6/Week6_Final_Capstone_Analytics_Report.pdf) • [Presentation Deck](week6/presentation/Capstone_Executive_Presentation.pdf) • [Week 6 Folder](week6/) |

---

## 🌟 Week 4: Statistics, Data Visualization & EDA Summary

- **Total Marks:** 100 / 100
- **Duration:** 1 Week (7 Days)
- **Directory:** [`week4/`](week4/)

### Tasks Completed:
1. **Task 1: Statistical Analysis – Mean, Median & Mode (10 Marks):** Central tendency, skewness analysis on E-Commerce sales data.
2. **Task 2: Variance & Standard Deviation (10 Marks):** Measures of dispersion, sample variance, standard deviation, and coefficient of variation ($CV$).
3. **Task 3: Correlation & Probability Basics (10 Marks):** Pearson correlation analysis and real-world marginal and conditional probability modeling.
4. **Task 4: Outlier Detection (10 Marks):** Parametric (Z-Score) and non-parametric (IQR) outlier detection with impact analysis.
5. **Task 5: Matplotlib Visualizations (15 Marks):** Line chart, Bar chart, Pie chart, Histogram, and Scatter plot with annotations.
6. **Task 6: Seaborn Visualizations (15 Marks):** Count plot, Box plot, Correlation Heatmap, and Pair plot.
7. **Task 7: EDA – Data Inspection & Cleaning (15 Marks):** Missing value imputation, deduplication, categorical standardization, and before/after audit dashboard.
8. **Task 8: EDA – Correlation & Insights (10 Marks):** Identification of four strategic business patterns including the "20% Discount Cliff".
9. **Task 9: Business Recommendations (5 Marks):** Actionable, data-backed commercial recommendations with projected ROI.

### Quick Start: Running Week 4 Tasks
```bash
# Execute master pipeline
python week4/run_all_tasks.py

# Recompile the submission PDF
python week4/generate_pdf_report.py
```

---

## 🌟 Week 5: Power BI & Business Intelligence Summary

- **Total Marks:** 100 / 100
- **Duration:** 1 Week (7 Days)
- **Directory:** [`week5/`](week5/)
- **PDF Report:** [`week5/Week5_Power_BI_Business_Intelligence_Report.pdf`](week5/Week5_Power_BI_Business_Intelligence_Report.pdf)

### Tasks Completed:
1. **Task 1: Power BI Introduction & Data Import (10 Marks):** Interface architecture, relational dataset ingestion, table catalog, and Power BI role in analytics.
2. **Task 2: Data Cleaning & Preparation (15 Marks):** Power Query M transformations, deduplication, null imputation, type casting, and schema normalization.
3. **Task 3: Data Modeling & Relationships (15 Marks):** Star Schema data model with 1 Fact table (`FactSales`) and 4 Dimensions (`DimCustomer`, `DimProduct`, `DimRegion`, `DimDate`) with 1-to-many (`1:*`) relationships.
4. **Task 4: DAX Calculated Columns & Measures (15 Marks):** 19 explicit DAX measures (Total Sales $7.91M, Profit $2.37M, Margin 30.0%, 3,500 Orders) and 6 calculated columns.
5. **Task 5: Power BI Visualizations (15 Marks):** Clustered Column Chart, Line & Area Chart, Donut Chart, Regional Performance Matrix, and KPI Cards.
6. **Task 6: Interactive Dashboard & Filters (15 Marks):** Executive dark-mode dashboard with 4 KPI cards, 4 analytical visuals, and 4 interactive slicers with bi-directional cross-filtering.
7. **Task 7: Business Insights & Recommendations (15 Marks):** 5 data-backed insights, sub-category performance ranking, and 3 strategic recommendations.

### Quick Start: Running Week 5 Tasks
```bash
# Generate relational datasets (CSV and Excel multi-table)
python week5/scripts/generate_datasets.py

# Generate visualizations and dashboard graphics
python week5/scripts/generate_visuals.py

# Compile the final submission PDF
python week5/scripts/generate_pdf_report.py
```

---

## 🌟 Week 6: Git, GitHub & Final Data Analytics Project Summary

- **Total Marks:** 100 / 100
- **Duration:** 1 Week (7 Days)
- **Directory:** [`week6/`](week6/)
- **PDF Report:** [`week6/Week6_Final_Capstone_Analytics_Report.pdf`](week6/Week6_Final_Capstone_Analytics_Report.pdf)
- **Executive Presentation:** [`week6/presentation/Capstone_Executive_Presentation.pdf`](week6/presentation/Capstone_Executive_Presentation.pdf)

### Tasks Completed:
1. **Task 1: Git & GitHub Basics (10 Marks):** Git installation, repository initialization, local cloning, staging, and remote synchronization.
2. **Task 2: Git Workflow Practice (10 Marks):** Full Git lifecycle (`git clone`, `git add`, `git commit`, `git push`, `git pull`) with 3 meaningful project commits.
3. **Task 3: Dataset Selection & Data Preparation (10 Marks):** Omnichannel E-Commerce domain, 6,342 raw rows cleaned of 35 duplicates, missing value imputation, type casting, and Star Schema normalization.
4. **Task 4: Exploratory Data Analysis (EDA) (15 Marks):** Central tendency, positive skewness (+4.06), Pearson correlation matrix ($r=0.997$ sales vs profit), and IQR outlier fencing (284 enterprise transactions).
5. **Task 5: Data Visualization (15 Marks):** 5 high-impact analytical charts (CLV by Segment, Marketing CAC Scatter, 24-Month Line Trend, Category Margin Bar, Payment/Channel Donut).
6. **Task 6: Power BI Dashboard & Modeling (20 Marks):** Production Star Schema model (6,307 Fact rows), dark-slate executive dashboard, 4 KPI cards, 4 visuals, 4 slicers, and 20 explicit DAX measures.
7. **Task 7: Business Insights & Recommendations (10 Marks):** 5 high-impact findings and 4 data-driven strategic recommendations with +$165K projected commercial ROI.
8. **Task 8: GitHub Documentation & Project Presentation (10 Marks):** Complete open-source project repository documentation and 6-slide executive presentation deck.

### Quick Start: Running Week 6 Tasks
```bash
# Generate relational datasets (CSV and Excel multi-table)
python week6/scripts/generate_datasets.py

# Run statistical EDA and render analytical visualizations
python week6/scripts/run_eda_and_visuals.py

# Build executive presentation deck and presentation PDF
python week6/scripts/generate_presentation.py

# Compile the master submission PDF report
python week6/scripts/generate_pdf_report.py
```
