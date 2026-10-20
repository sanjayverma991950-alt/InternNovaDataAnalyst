# Week 3 Assignment: SQL & Microsoft Excel

Course: Data Analytics  
Total Marks: 100  
Submission Format: PDF Report + Google Drive Link  

---

## Google Drive Link

Link: `https://drive.google.com/drive/folders/1_DATA_ANALYTICS_WEEK3_SUBMISSION_FOLDER?usp=sharing`  
Access: Anyone with the link (Viewer)  

Files to include in Google Drive:
- `Data_Analytics_Week3_Assignment_Report.pdf`
- `excel/Week3_Data_Analytics_Workbook.xlsx`
- `sql/all_sql_tasks.sql`
- `data/company_database.db`

---

## Task Breakdown (100 Marks)

| Task | Topic | Marks | File Reference |
| --- | --- | --- | --- |
| Task 1 | SELECT Statement & Aliases | 10 | `sql/task1_select.sql` |
| Task 2 | WHERE, ORDER BY & Aggregate Functions | 15 | `sql/task2_where_orderby_agg.sql` |
| Task 3 | GROUP BY & HAVING | 10 | `sql/task3_groupby_having.sql` |
| Task 4 | SQL Joins (INNER, LEFT, RIGHT) | 15 | `sql/task4_joins.sql` |
| Task 5 | SQL Subqueries | 10 | `sql/task5_subqueries.sql` |
| Task 6 | Data Formatting, Sorting & Filtering | 10 | `excel/Week3_Data_Analytics_Workbook.xlsx` (Sheet: Task6_Formatting_Sorting) |
| Task 7 | Conditional Formatting & Functions (IF, COUNTIF, SUMIF) | 15 | `excel/Week3_Data_Analytics_Workbook.xlsx` (Sheet: Task7_Conditional_Functions) |
| Task 8 | VLOOKUP & XLOOKUP | 10 | `excel/Week3_Data_Analytics_Workbook.xlsx` (Sheet: Task8_VLOOKUP_XLOOKUP) |
| Task 9 | Pivot Table & Chart | 5 | `excel/Week3_Data_Analytics_Workbook.xlsx` (Sheet: Task9_Pivot_and_Chart) |
| Total | | 100 | |

---

## Folder Structure

```text
week3/
├── Data_Analytics_Week3_Assignment_Report.pdf
├── README.md
├── data/
│   ├── company_database.db
│   ├── insert_data.sql
│   └── schema.sql
├── sql/
│   ├── all_sql_tasks.sql
│   ├── task1_select.sql
│   ├── task2_where_orderby_agg.sql
│   ├── task3_groupby_having.sql
│   ├── task4_joins.sql
│   └── task5_subqueries.sql
├── excel/
│   └── Week3_Data_Analytics_Workbook.xlsx
├── screenshots/
│   ├── task1_all_records.png
│   ├── task1_column_aliases.png
│   ├── task1_specific_columns.png
│   ├── task2_aggregates.png
│   ├── task2_orderby.png
│   ├── task2_where_filter.png
│   ├── task3_groupby.png
│   ├── task3_groupby_having.png
│   ├── task4_inner_join.png
│   ├── task4_left_join.png
│   ├── task4_right_join.png
│   ├── task5_subquery1.png
│   ├── task5_subquery2.png
│   ├── task6_formatting_sorting_filtering.png
│   ├── task7_conditional_formatting_functions.png
│   ├── task8_vlookup_xlookup.png
│   └── task9_pivot_table_and_chart.png
└── scripts/
    ├── generate_excel.py
    ├── generate_excel_visuals.py
    ├── generate_pdf_report.py
    └── run_sql_tasks.py
```

---

## Running the Project

To rerun all SQL queries, rebuild the Excel workbook, update the screenshots, and recompile the PDF report, run:

```powershell
python week3/scripts/run_sql_tasks.py
python week3/scripts/generate_excel.py
python week3/scripts/generate_excel_visuals.py
python week3/scripts/generate_pdf_report.py
```
