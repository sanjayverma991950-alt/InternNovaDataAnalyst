# Week 5 Assignment: Power BI & Business Intelligence

Course: Data Analytics  
Total Marks: 100 / 100  
Submission Format: Any one of GitHub Repository Link • Google Drive Link • Direct PDF Upload  

---

## 🔗 Submission Options

### Option 1: GitHub Repository Link
- Repository URL: `https://github.com/sanjayverma991950-alt/InternNovaDataAnalyst/tree/main/week5`
- Files included:
  - `Week5_Power_BI_Business_Intelligence_Report.pdf`
  - `data/Superstore_Retail_MultiTable.xlsx`
  - `data/` (CSV files for all tables)
  - `dax/all_measures.dax` and `dax/calculated_columns.dax`
  - `power_query_etl/` (Power Query M scripts)
  - `visualizations/` (High-resolution dashboard and chart PNGs)
  - `WEEK5_SUBMISSION_REPORT.md` (Detailed 100-mark report)

### Option 2: Google Drive Link
- Folder URL: `https://drive.google.com/drive/folders/1_POWERBI_WEEK5_SUBMISSION_SANJAY_KUMAR?usp=sharing`
- Access: Anyone with the link (Viewer)
- Files to include:
  - `Week5_Power_BI_Business_Intelligence_Report.pdf`
  - `Superstore_Retail_MultiTable.xlsx`
  - `visualizations/dashboard_overview.png`
  - `WEEK5_SUBMISSION_REPORT.md`

### Option 3: Direct PDF Upload
- PDF Report File: [`Week5_Power_BI_Business_Intelligence_Report.pdf`](Week5_Power_BI_Business_Intelligence_Report.pdf)
- Direct upload of the 6-page comprehensive report covering all 7 tasks, screenshots, DAX formulas, data model diagrams, insights, and recommendations.

---

## 📋 Task Breakdown (100 Marks)

| Task | Topic | Marks | Status | Deliverable References |
| :--- | :--- | :---: | :---: | :--- |
| **Task 1** | Power BI Introduction & Data Import | 10 | Completed | `WEEK5_SUBMISSION_REPORT.md#task-1` • `data/Superstore_Retail_MultiTable.xlsx` |
| **Task 2** | Data Cleaning & Preparation (Power Query) | 15 | Completed | `power_query_etl/*.m` • `data/raw_superstore_data.csv` |
| **Task 3** | Data Modeling & Star Schema Relationships | 15 | Completed | `visualizations/task3_data_model_star_schema.png` • Model specs |
| **Task 4** | DAX Calculated Columns & Explicit Measures | 15 | Completed | `dax/all_measures.dax` • `dax/calculated_columns.dax` |
| **Task 5** | Core Power BI Visualizations | 15 | Completed | `visualizations/task5_visual*.png` (Bar, Line, Donut, Matrix, KPI Cards) |
| **Task 6** | Interactive Executive Dashboard & Slicers | 15 | Completed | `visualizations/dashboard_overview.png` • Slicer interactions |
| **Task 7** | Business Insights & Strategic Recommendations | 15 | Completed | `WEEK5_SUBMISSION_REPORT.md#task-7` • 5 Insights & 3 Recommendations |
| **Total** | | **100** | | |

---

## 📁 Folder Structure

```text
week5/
├── Week5_Power_BI_Business_Intelligence_Report.pdf   # Complete 6-page submission PDF report
├── README.md                                          # Project overview and submission instructions
├── WEEK5_SUBMISSION_REPORT.md                         # Detailed technical documentation
├── data/
│   ├── Superstore_Retail_MultiTable.xlsx             # Multi-sheet Excel workbook (1-click Power BI load)
│   ├── raw_superstore_data.csv                       # Raw dirty dataset (5,592 records)
│   ├── FactSales.csv                                 # Clean fact table (5,567 rows)
│   ├── DimCustomer.csv                               # Clean customer dimension (200 rows)
│   ├── DimProduct.csv                                # Clean product dimension (24 rows)
│   ├── DimRegion.csv                                 # Clean region dimension (4 rows)
│   └── DimDate.csv                                   # Clean date dimension (1,096 rows)
├── dax/
│   ├── all_measures.dax                              # 19 explicit DAX measures (pure DAX, no comments)
│   └── calculated_columns.dax                        # 6 calculated columns (pure DAX, no comments)
├── power_query_etl/
│   ├── FactSales_ETL.m                               # FactSales Power Query M code
│   ├── DimCustomer_ETL.m                             # DimCustomer Power Query M code
│   ├── DimProduct_ETL.m                              # DimProduct Power Query M code
│   ├── DimRegion_ETL.m                               # DimRegion Power Query M code
│   └── DimDate_ETL.m                                 # DimDate Power Query M code
├── visualizations/
│   ├── dashboard_overview.png                        # Executive interactive dashboard render
│   ├── task1_powerbi_interface_architecture.png       # Power BI interface schematic
│   ├── task2_data_cleaning_flow.png                  # ETL data preparation pipeline
│   ├── task3_data_model_star_schema.png              # Star schema entity-relationship diagram
│   ├── task4_dax_measures_matrix.png                 # DAX measures catalog
│   ├── task5_visual1_sales_profit_by_category.png    # Category clustered column chart
│   ├── task5_visual2_monthly_trend.png               # Monthly revenue trend line chart
│   ├── task5_visual3_segment_donut.png               # Customer segment donut chart
│   ├── task5_visual4_regional_matrix.png             # Regional breakdown matrix
│   ├── task5_visual5_kpi_cards.png                   # KPI card deck
│   ├── task6_slicers_interaction.png                 # Interactive slicers layout
│   └── task7_category_performance_heatmap.png        # Sub-category ranking bar chart
└── scripts/
    ├── generate_datasets.py                          # Dataset generation pipeline (no comments)
    ├── generate_visuals.py                           # Visual asset rendering pipeline (no comments)
    └── generate_pdf_report.py                        # ReportLab PDF compiler (no comments)
```

---

## 🚀 Running the Project

To regenerate all datasets, visual assets, and the final submission PDF from scratch:

```powershell
# 1. Generate relational datasets (CSV & Excel)
python week5/scripts/generate_datasets.py

# 2. Render all charts and dashboard graphics
python week5/scripts/generate_visuals.py

# 3. Rebuild the final submission PDF report
python week5/scripts/generate_pdf_report.py
```

---

## 📊 Summary of Key Metrics

- **Total Sales:** $7,907,425.85
- **Total Direct Cost:** $5,534,963.00
- **Net Company Profit:** $2,372,462.85
- **Operating Profit Margin:** 30.0%
- **Unique Purchase Orders:** 3,500
- **Average Order Line Value:** $1,420.41
- **Top Revenue Category:** Technology ($4,977,791.45 | 62.9%)
- **Top Margin Category:** Office Supplies (44.3% margin)
- **Top Performing Region:** West Region ($2,373,312.60 sales | Marcus Vance)
