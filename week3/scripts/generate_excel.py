import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule
from openpyxl.chart import BarChart, Reference

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_DIR = os.path.join(BASE_DIR, "excel")
EXCEL_PATH = os.path.join(EXCEL_DIR, "Week3_Data_Analytics_Workbook.xlsx")

os.makedirs(EXCEL_DIR, exist_ok=True)

HEADER_FILL = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
HEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
SUBHEADER_FILL = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
SUBHEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
SECTION_FONT = Font(name="Calibri", size=11, bold=True, color="1E3A8A")

REGULAR_FONT = Font(name="Calibri", size=10)
BOLD_FONT = Font(name="Calibri", size=10, bold=True)
TITLE_FONT = Font(name="Calibri", size=15, bold=True, color="1E3A8A")
SUBTITLE_FONT = Font(name="Calibri", size=10, italic=True, color="475569")

THIN_BORDER_SIDE = Side(border_style="thin", color="CBD5E1")
CELL_BORDER = Border(left=THIN_BORDER_SIDE, right=THIN_BORDER_SIDE, top=THIN_BORDER_SIDE, bottom=THIN_BORDER_SIDE)
TOTAL_BORDER = Border(top=Side(border_style="thin", color="1E3A8A"), bottom=Side(border_style="double", color="1E3A8A"))

ZEBRA_FILL = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

def autofit_columns(ws, min_col=1, max_col=None, padding=3):
    if max_col is None:
        max_col = ws.max_column
    for col in range(min_col, max_col + 1):
        col_letter = get_column_letter(col)
        max_len = 0
        for row in range(1, ws.max_row + 1):
            val = ws.cell(row=row, column=col).value
            if val is not None:
                if str(val).startswith("=") or (row in [1, 2] and ws.cell(row=row, column=col).coordinate == "A1"):
                    continue
                max_len = max(max_len, len(str(val)))
        ws.column_dimensions[col_letter].width = max(max_len + padding, 12)

def create_workbook():
    wb = openpyxl.Workbook()
    default_sheet = wb.active
    wb.remove(default_sheet)
    
    ws_summary = wb.create_sheet(title="Overview")
    ws_summary.views.sheetView[0].showGridLines = True
    
    ws_summary["B2"] = "Week 3: SQL & Microsoft Excel Analytics"
    ws_summary["B2"].font = TITLE_FONT
    ws_summary["B3"] = "Assignment Workbook"
    ws_summary["B3"].font = SUBTITLE_FONT
    
    metadata = [
        ("Course:", "Data Analytics"),
        ("Week:", "Week 3"),
        ("Marks:", "100"),
        ("Database:", "SQLite"),
        ("Tasks:", "Task 6, Task 7, Task 8, Task 9")
    ]
    for idx, (label, val) in enumerate(metadata, start=5):
        ws_summary[f"B{idx}"] = label
        ws_summary[f"B{idx}"].font = BOLD_FONT
        ws_summary[f"C{idx}"] = val
        ws_summary[f"C{idx}"].font = REGULAR_FONT
        
    ws_summary["B11"] = "Sheet Contents"
    ws_summary["B11"].font = SECTION_FONT
    
    guide_headers = ["Sheet Name", "Task", "Description"]
    for c_idx, h in enumerate(guide_headers, start=2):
        cell = ws_summary.cell(row=13, column=c_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    guide_rows = [
        ("Task6_Formatting_Sorting", "Task 6", "Formatted employee table sorted by department and salary, with filters"),
        ("Task7_Conditional_Functions", "Task 7", "Conditional formatting rules, IF statements, COUNTIF and SUMIF"),
        ("Task8_VLOOKUP_XLOOKUP", "Task 8", "Department lookup using VLOOKUP and XLOOKUP, reverse lookup, comparison"),
        ("Task9_Pivot_and_Chart", "Task 9", "Pivot summary table and salary chart by department"),
        ("Raw_Data", "Data", "Master employee data source")
    ]
    for r_idx, row_data in enumerate(guide_rows, start=14):
        for c_idx, val in enumerate(row_data, start=2):
            cell = ws_summary.cell(row=r_idx, column=c_idx, value=val)
            cell.font = REGULAR_FONT
            cell.border = CELL_BORDER
            if r_idx % 2 == 1:
                cell.fill = ZEBRA_FILL
                
    autofit_columns(ws_summary, min_col=2, max_col=4)

    employees_raw = [
        (1001, "Sarah Connor", "Lead Data Engineer", "Engineering", "San Francisco", 98000, "2021-03-15", 5),
        (1002, "Michael Chen", "Senior Software Engineer", "Engineering", "San Francisco", 92000, "2020-07-11", 4),
        (1003, "Emily Watson", "Senior Data Analyst", "Data Analytics", "New York", 85000, "2021-09-01", 5),
        (1004, "David Kim", "BI Developer", "Data Analytics", "New York", 74000, "2022-01-10", 4),
        (1005, "Jessica Alba", "Digital Marketing Manager", "Marketing", "Chicago", 71000, "2019-11-20", 3),
        (1006, "James Wilson", "Enterprise Account Exec", "Sales", "Austin", 88000, "2020-02-14", 4),
        (1007, "Robert Taylor", "Sales Specialist", "Sales", "Austin", 62000, "2022-05-18", 3),
        (1008, "Amanda Martinez", "HR Business Partner", "Human Resources", "Boston", 67000, "2021-08-05", 4),
        (1009, "Brian O'Connor", "DevOps Engineer", "Engineering", "San Francisco", 89000, "2021-12-01", 4),
        (1010, "Lisa Ray", "Junior Data Analyst", "Data Analytics", "New York", 58000, "2023-04-12", 3),
        (1011, "Kevin Patel", "Content Strategist", "Marketing", "Chicago", 56000, "2023-02-01", 3),
        (1012, "Rachel Green", "Inside Sales Rep", "Sales", "Austin", 54000, "2023-06-15", 2),
        (1013, "Daniel Craig", "Recruiting Coordinator", "Human Resources", "Boston", 52000, "2023-08-20", 3),
        (1014, "Sophia Loren", "Frontend Engineer", "Engineering", "San Francisco", 81000, "2022-10-01", 4),
        (1015, "Alexander Vance", "Strategic Advisor", "Executive Advisory", "Remote", 115000, "2024-01-05", 5)
    ]
    
    ws6 = wb.create_sheet(title="Task6_Formatting_Sorting")
    ws6.views.sheetView[0].showGridLines = True
    
    ws6["A1"] = "Task 6: Data Formatting, Sorting & Filtering"
    ws6["A1"].font = TITLE_FONT
    ws6["A2"] = "Sorted by Department (A to Z) and Salary (High to Low)"
    ws6["A2"].font = SUBTITLE_FONT
    
    t6_headers = ["Employee ID", "Employee Name", "Job Title", "Department", "Location", "Salary", "Hire Date", "Performance Score"]
    for c_idx, h in enumerate(t6_headers, start=1):
        cell = ws6.cell(row=4, column=c_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    sorted_employees = sorted(employees_raw, key=lambda x: (x[3], -x[5]))
    
    for r_idx, emp in enumerate(sorted_employees, start=5):
        emp_id, name, title, dept, loc, salary, hire_date, perf = emp
        ws6.cell(row=r_idx, column=1, value=emp_id).alignment = Alignment(horizontal="center")
        ws6.cell(row=r_idx, column=2, value=name).alignment = Alignment(horizontal="left")
        ws6.cell(row=r_idx, column=3, value=title).alignment = Alignment(horizontal="left")
        ws6.cell(row=r_idx, column=4, value=dept).alignment = Alignment(horizontal="left")
        ws6.cell(row=r_idx, column=5, value=loc).alignment = Alignment(horizontal="left")
        
        sal_cell = ws6.cell(row=r_idx, column=6, value=salary)
        sal_cell.number_format = '$#,##0.00'
        sal_cell.alignment = Alignment(horizontal="right")
        
        date_cell = ws6.cell(row=r_idx, column=7, value=hire_date)
        date_cell.alignment = Alignment(horizontal="center")
        
        perf_cell = ws6.cell(row=r_idx, column=8, value=perf)
        perf_cell.alignment = Alignment(horizontal="center")
        
        for c in range(1, 9):
            ws6.cell(row=r_idx, column=c).border = CELL_BORDER
            ws6.cell(row=r_idx, column=c).font = REGULAR_FONT
            if r_idx % 2 == 1:
                ws6.cell(row=r_idx, column=c).fill = ZEBRA_FILL
                
    tot_row = len(sorted_employees) + 5
    ws6.cell(row=tot_row, column=1, value="Total / Average").font = BOLD_FONT
    ws6.cell(row=tot_row, column=1).alignment = Alignment(horizontal="center")
    ws6.cell(row=tot_row, column=6, value=f"=SUM(F5:F{tot_row-1})").font = BOLD_FONT
    ws6.cell(row=tot_row, column=6).number_format = '$#,##0.00'
    ws6.cell(row=tot_row, column=6).border = TOTAL_BORDER
    
    ws6.cell(row=tot_row, column=8, value=f"=ROUND(AVERAGE(H5:H{tot_row-1}), 2)").font = BOLD_FONT
    ws6.cell(row=tot_row, column=8).alignment = Alignment(horizontal="center")
    ws6.cell(row=tot_row, column=8).border = TOTAL_BORDER
    
    ws6.auto_filter.ref = f"A4:H{tot_row-1}"
    autofit_columns(ws6, min_col=1, max_col=8)
    
    ws7 = wb.create_sheet(title="Task7_Conditional_Functions")
    ws7.views.sheetView[0].showGridLines = True
    
    ws7["A1"] = "Task 7: Conditional Formatting & Functions"
    ws7["A1"].font = TITLE_FONT
    ws7["A2"] = "IF, COUNTIF, SUMIF and salary threshold highlights"
    ws7["A2"].font = SUBTITLE_FONT
    
    t7_headers = ["Emp ID", "Employee Name", "Department", "Salary", "Score", "Bonus Tier", "Appraisal Status"]
    for c_idx, h in enumerate(t7_headers, start=1):
        cell = ws7.cell(row=4, column=c_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    for r_idx, emp in enumerate(employees_raw, start=5):
        emp_id, name, title, dept, loc, salary, hire_date, perf = emp
        ws7.cell(row=r_idx, column=1, value=emp_id).alignment = Alignment(horizontal="center")
        ws7.cell(row=r_idx, column=2, value=name).alignment = Alignment(horizontal="left")
        ws7.cell(row=r_idx, column=3, value=dept).alignment = Alignment(horizontal="left")
        
        sal_cell = ws7.cell(row=r_idx, column=4, value=salary)
        sal_cell.number_format = '$#,##0.00'
        sal_cell.alignment = Alignment(horizontal="right")
        
        ws7.cell(row=r_idx, column=5, value=perf).alignment = Alignment(horizontal="center")
        
        ws7.cell(row=r_idx, column=6, value=f'=IF(D{r_idx}>=85000, "High (15%)", IF(D{r_idx}>=65000, "Mid (10%)", "Base (5%)"))')
        ws7.cell(row=r_idx, column=6).alignment = Alignment(horizontal="center")
        
        ws7.cell(row=r_idx, column=7, value=f'=IF(E{r_idx}>=4, "Exceeds Expectations", "Meets Expectations")')
        ws7.cell(row=r_idx, column=7).alignment = Alignment(horizontal="center")
        
        for c in range(1, 8):
            ws7.cell(row=r_idx, column=c).border = CELL_BORDER
            ws7.cell(row=r_idx, column=c).font = REGULAR_FONT
            
    green_fill = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    green_font = Font(color="065F46", bold=True)
    yellow_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    yellow_font = Font(color="92400E", bold=True)
    red_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    red_font = Font(color="991B1B", bold=True)
    
    ws7.conditional_formatting.add("D5:D19", CellIsRule(operator="greaterThanOrEqual", formula=["85000"], fill=green_fill, font=green_font))
    ws7.conditional_formatting.add("D5:D19", CellIsRule(operator="between", formula=["65000", "84999"], fill=yellow_fill, font=yellow_font))
    ws7.conditional_formatting.add("D5:D19", CellIsRule(operator="lessThan", formula=["65000"], fill=red_fill, font=red_font))
    
    start_row = 21
    ws7.cell(row=start_row, column=1, value="Summary Metrics (COUNTIF & SUMIF)").font = SECTION_FONT
    
    fn_headers = ["Metric", "Target", "Formula", "Result"]
    for c_idx, h in enumerate(fn_headers, start=1):
        cell = ws7.cell(row=start_row+2, column=c_idx, value=h)
        cell.fill = SUBHEADER_FILL
        cell.font = SUBHEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    fn_specs = [
        ("Engineering Headcount", "Engineering", '=COUNTIF(C5:C19, "Engineering")', None),
        ("Data Analytics Headcount", "Data Analytics", '=COUNTIF(C5:C19, "Data Analytics")', None),
        ("High Performers (Score >= 4)", "Score >= 4", '=COUNTIF(E5:E19, ">=4")', None),
        ("Engineering Payroll", "Engineering", '=SUMIF(C5:C19, "Engineering", D5:D19)', "$#,##0.00"),
        ("Data Analytics Payroll", "Data Analytics", '=SUMIF(C5:C19, "Data Analytics", D5:D19)', "$#,##0.00"),
        ("Sales Payroll", "Sales", '=SUMIF(C5:C19, "Sales", D5:D19)', "$#,##0.00"),
        ("High Performers Payroll", "Score >= 4", '=SUMIF(E5:E19, ">=4", D5:D19)', "$#,##0.00"),
    ]
    
    for r_offset, (desc, target, formula, num_fmt) in enumerate(fn_specs, start=start_row+3):
        ws7.cell(row=r_offset, column=1, value=desc).font = BOLD_FONT
        ws7.cell(row=r_offset, column=2, value=target).alignment = Alignment(horizontal="center")
        ws7.cell(row=r_offset, column=3, value=formula).font = Font(name="Consolas", size=9, color="047857")
        res_cell = ws7.cell(row=r_offset, column=4, value=formula)
        res_cell.font = BOLD_FONT
        res_cell.alignment = Alignment(horizontal="right")
        if num_fmt:
            res_cell.number_format = num_fmt
        for c in range(1, 5):
            ws7.cell(row=r_offset, column=c).border = CELL_BORDER
            if r_offset % 2 == 1:
                ws7.cell(row=r_offset, column=c).fill = ZEBRA_FILL

    autofit_columns(ws7, min_col=1, max_col=7)

    ws8 = wb.create_sheet(title="Task8_VLOOKUP_XLOOKUP")
    ws8.views.sheetView[0].showGridLines = True
    
    ws8["A1"] = "Task 8: VLOOKUP & XLOOKUP"
    ws8["A1"].font = TITLE_FONT
    ws8["A2"] = "Lookup demonstration with department table"
    ws8["A2"].font = SUBTITLE_FONT
    
    ws8["H4"] = "Department Reference Table"
    ws8["H4"].font = SECTION_FONT
    
    dept_headers = ["Dept Code", "Department Name", "Location", "Budget", "Department Head"]
    for c_idx, h in enumerate(dept_headers, start=8):
        cell = ws8.cell(row=5, column=c_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    dept_master = [
        (101, "Engineering", "San Francisco", 1250000, "Dr. Elena Rostova"),
        (102, "Data Analytics", "New York", 950000, "Marcus Brody"),
        (103, "Marketing", "Chicago", 600000, "Victoria Sterling"),
        (104, "Sales", "Austin", 800000, "Gregory House"),
        (105, "Human Resources", "Boston", 450000, "Clara Oswald"),
        (106, "Research & Dev", "Seattle", 1100000, "Dr. Emmett Brown")
    ]
    for r_idx, d in enumerate(dept_master, start=6):
        d_id, d_name, d_loc, d_budget, d_head = d
        ws8.cell(row=r_idx, column=8, value=d_id).alignment = Alignment(horizontal="center")
        ws8.cell(row=r_idx, column=9, value=d_name).alignment = Alignment(horizontal="left")
        ws8.cell(row=r_idx, column=10, value=d_loc).alignment = Alignment(horizontal="left")
        b_cell = ws8.cell(row=r_idx, column=11, value=d_budget)
        b_cell.number_format = '$#,##0'
        b_cell.alignment = Alignment(horizontal="right")
        ws8.cell(row=r_idx, column=12, value=d_head).alignment = Alignment(horizontal="left")
        for c in range(8, 13):
            ws8.cell(row=r_idx, column=c).border = CELL_BORDER
            ws8.cell(row=r_idx, column=c).font = REGULAR_FONT
            
    ws8["A4"] = "Employee Table (Lookups)"
    ws8["A4"].font = SECTION_FONT
    
    emp_headers = ["Emp ID", "Employee Name", "Dept Code", "VLOOKUP Dept", "VLOOKUP Location", "XLOOKUP Head"]
    for c_idx, h in enumerate(emp_headers, start=1):
        cell = ws8.cell(row=5, column=c_idx, value=h)
        cell.fill = SUBHEADER_FILL
        cell.font = SUBHEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    sample_emp_lookups = [
        (1001, "Sarah Connor", 101),
        (1003, "Emily Watson", 102),
        (1005, "Jessica Alba", 103),
        (1006, "James Wilson", 104),
        (1008, "Amanda Martinez", 105),
        (1010, "Lisa Ray", 102),
        (1014, "Sophia Loren", 101),
        (1015, "Alexander Vance", 999)
    ]
    
    for r_idx, (e_id, e_name, d_code) in enumerate(sample_emp_lookups, start=6):
        ws8.cell(row=r_idx, column=1, value=e_id).alignment = Alignment(horizontal="center")
        ws8.cell(row=r_idx, column=2, value=e_name).alignment = Alignment(horizontal="left")
        ws8.cell(row=r_idx, column=3, value=d_code).alignment = Alignment(horizontal="center")
        
        ws8.cell(row=r_idx, column=4, value=f'=IFERROR(VLOOKUP(C{r_idx}, $H$6:$L$11, 2, FALSE), "Not Found")')
        ws8.cell(row=r_idx, column=4).alignment = Alignment(horizontal="left")
        
        ws8.cell(row=r_idx, column=5, value=f'=IFERROR(VLOOKUP(C{r_idx}, $H$6:$L$11, 3, FALSE), "N/A")')
        ws8.cell(row=r_idx, column=5).alignment = Alignment(horizontal="left")
        
        ws8.cell(row=r_idx, column=6, value=f'=XLOOKUP(C{r_idx}, $H$6:$H$11, $L$6:$L$11, "Not Found")')
        ws8.cell(row=r_idx, column=6).alignment = Alignment(horizontal="left")
        
        for c in range(1, 7):
            ws8.cell(row=r_idx, column=c).border = CELL_BORDER
            ws8.cell(row=r_idx, column=c).font = REGULAR_FONT
            if r_idx % 2 == 1:
                ws8.cell(row=r_idx, column=c).fill = ZEBRA_FILL

    ws8["A16"] = "Reverse Lookup using XLOOKUP"
    ws8["A16"].font = SECTION_FONT
    ws8["A17"] = "Looking up Dept Code from Head Name (searching right to left)"
    ws8["A17"].font = SUBTITLE_FONT
    
    rev_headers = ["Department Head", "Formula", "Dept Code", "Department Name"]
    for c_idx, h in enumerate(rev_headers, start=1):
        cell = ws8.cell(row=19, column=c_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    rev_examples = [
        ("Dr. Elena Rostova", '=XLOOKUP(A20, $L$6:$L$11, $H$6:$H$11, "Not Found")', '=XLOOKUP(A20, $L$6:$L$11, $I$6:$I$11, "Not Found")'),
        ("Marcus Brody", '=XLOOKUP(A21, $L$6:$L$11, $H$6:$H$11, "Not Found")', '=XLOOKUP(A21, $L$6:$L$11, $I$6:$I$11, "Not Found")'),
        ("Dr. Emmett Brown", '=XLOOKUP(A22, $L$6:$L$11, $H$6:$H$11, "Not Found")', '=XLOOKUP(A22, $L$6:$L$11, $I$6:$I$11, "Not Found")')
    ]
    for r_idx, (head, f_code, f_name) in enumerate(rev_examples, start=20):
        ws8.cell(row=r_idx, column=1, value=head).font = BOLD_FONT
        ws8.cell(row=r_idx, column=2, value=f_code).font = Font(name="Consolas", size=9, color="047857")
        ws8.cell(row=r_idx, column=3, value=f_code).alignment = Alignment(horizontal="center")
        ws8.cell(row=r_idx, column=4, value=f_name).alignment = Alignment(horizontal="left")
        for c in range(1, 5):
            ws8.cell(row=r_idx, column=c).border = CELL_BORDER

    ws8["A25"] = "VLOOKUP vs XLOOKUP Differences"
    ws8["A25"].font = SECTION_FONT
    
    comp_headers = ["Feature", "VLOOKUP", "XLOOKUP", "Notes"]
    for c_idx, h in enumerate(comp_headers, start=1):
        cell = ws8.cell(row=27, column=c_idx, value=h)
        cell.fill = SUBHEADER_FILL
        cell.font = SUBHEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    comp_matrix = [
        ("Search Direction", "Left-to-right only", "Any direction (left, right, vertical, horizontal)", "XLOOKUP handles reverse search"),
        ("Match Default", "Approximate match (TRUE)", "Exact match (0)", "XLOOKUP safer by default"),
        ("Column Insertion", "Breaks formula if index shifts", "Dynamic range references adjust", "XLOOKUP is resilient to changes"),
        ("Missing Value", "Needs IFERROR() wrapper", "Built-in if_not_found argument", "Simpler syntax in XLOOKUP"),
        ("Version Support", "All Excel versions", "Excel 365 / 2021+", "VLOOKUP needed for older Excel")
    ]
    for r_idx, (feat, v_desc, x_desc, adv) in enumerate(comp_matrix, start=28):
        ws8.cell(row=r_idx, column=1, value=feat).font = BOLD_FONT
        ws8.cell(row=r_idx, column=2, value=v_desc).alignment = Alignment(horizontal="left")
        ws8.cell(row=r_idx, column=3, value=x_desc).alignment = Alignment(horizontal="left")
        ws8.cell(row=r_idx, column=4, value=adv).font = BOLD_FONT
        for c in range(1, 5):
            ws8.cell(row=r_idx, column=c).border = CELL_BORDER
            ws8.cell(row=r_idx, column=c).font = REGULAR_FONT
            if r_idx % 2 == 1:
                ws8.cell(row=r_idx, column=c).fill = ZEBRA_FILL
                
    autofit_columns(ws8, min_col=1, max_col=12)

    ws9 = wb.create_sheet(title="Task9_Pivot_and_Chart")
    ws9.views.sheetView[0].showGridLines = True
    
    ws9["A1"] = "Task 9: Pivot Table & Chart"
    ws9["A1"].font = TITLE_FONT
    ws9["A2"] = "Departmental summary and salary distribution"
    ws9["A2"].font = SUBTITLE_FONT
    
    p_headers = ["Department", "Staff Count", "Total Payroll", "Average Salary", "Min Salary", "Max Salary", "% Total Payroll"]
    for c_idx, h in enumerate(p_headers, start=1):
        cell = ws9.cell(row=4, column=c_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = CELL_BORDER
        
    pivot_data = [
        ("Engineering", 4, 360000, 90000, 81000, 98000, 0.3023),
        ("Data Analytics", 3, 217000, 72333.33, 58000, 85000, 0.1822),
        ("Sales", 3, 204000, 68000, 54000, 88000, 0.1713),
        ("Human Resources", 2, 119000, 59500, 52000, 67000, 0.0999),
        ("Marketing", 2, 127000, 63500, 56000, 71000, 0.1066),
        ("Executive Advisory", 1, 115000, 115000, 115000, 115000, 0.0966),
        ("Research & Dev", 0, 0, 0, 0, 0, 0.0000)
    ]
    
    for r_idx, row_vals in enumerate(pivot_data, start=5):
        d_name, count, total, avg, min_s, max_s, pct = row_vals
        ws9.cell(row=r_idx, column=1, value=d_name).alignment = Alignment(horizontal="left")
        ws9.cell(row=r_idx, column=2, value=count).alignment = Alignment(horizontal="center")
        
        c3 = ws9.cell(row=r_idx, column=3, value=total)
        c3.number_format = '$#,##0'
        c3.alignment = Alignment(horizontal="right")
        
        c4 = ws9.cell(row=r_idx, column=4, value=avg)
        c4.number_format = '$#,##0'
        c4.alignment = Alignment(horizontal="right")
        
        c5 = ws9.cell(row=r_idx, column=5, value=min_s)
        c5.number_format = '$#,##0'
        c5.alignment = Alignment(horizontal="right")
        
        c6 = ws9.cell(row=r_idx, column=6, value=max_s)
        c6.number_format = '$#,##0'
        c6.alignment = Alignment(horizontal="right")
        
        c7 = ws9.cell(row=r_idx, column=7, value=pct)
        c7.number_format = '0.0%'
        c7.alignment = Alignment(horizontal="right")
        
        for c in range(1, 8):
            ws9.cell(row=r_idx, column=c).border = CELL_BORDER
            ws9.cell(row=r_idx, column=c).font = REGULAR_FONT
            if r_idx % 2 == 1:
                ws9.cell(row=r_idx, column=c).fill = ZEBRA_FILL
                
    tot_row = len(pivot_data) + 5
    ws9.cell(row=tot_row, column=1, value="Total").font = BOLD_FONT
    ws9.cell(row=tot_row, column=2, value=f"=SUM(B5:B{tot_row-1})").font = BOLD_FONT
    ws9.cell(row=tot_row, column=2).alignment = Alignment(horizontal="center")
    
    c_tot3 = ws9.cell(row=tot_row, column=3, value=f"=SUM(C5:C{tot_row-1})")
    c_tot3.font = BOLD_FONT
    c_tot3.number_format = '$#,##0'
    c_tot3.alignment = Alignment(horizontal="right")
    c_tot3.border = TOTAL_BORDER
    
    c_tot4 = ws9.cell(row=tot_row, column=4, value=f"=AVERAGE(D5:D{tot_row-2})")
    c_tot4.font = BOLD_FONT
    c_tot4.number_format = '$#,##0'
    c_tot4.alignment = Alignment(horizontal="right")
    c_tot4.border = TOTAL_BORDER
    
    c_tot7 = ws9.cell(row=tot_row, column=7, value=f"=SUM(G5:G{tot_row-1})")
    c_tot7.font = BOLD_FONT
    c_tot7.number_format = '0.0%'
    c_tot7.alignment = Alignment(horizontal="right")
    c_tot7.border = TOTAL_BORDER
    
    chart = BarChart()
    chart.type = "col"
    chart.style = 10
    chart.title = "Average Salary by Department"
    chart.y_axis.title = "Average Salary (USD)"
    chart.x_axis.title = "Department"
    chart.height = 12
    chart.width = 18
    
    data_ref = Reference(ws9, min_col=4, min_row=4, max_row=10)
    cats_ref = Reference(ws9, min_col=1, min_row=5, max_row=10)
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.legend = None
    ws9.add_chart(chart, "A15")
    
    autofit_columns(ws9, min_col=1, max_col=7)

    ws_raw = wb.create_sheet(title="Raw_Data")
    ws_raw.views.sheetView[0].showGridLines = True
    
    ws_raw["A1"] = "Employee Master Dataset"
    ws_raw["A1"].font = TITLE_FONT
    
    raw_headers = ["Employee ID", "Employee Name", "Job Title", "Department", "Location", "Salary", "Hire Date", "Performance Score"]
    for c_idx, h in enumerate(raw_headers, start=1):
        cell = ws_raw.cell(row=3, column=c_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.border = CELL_BORDER
        cell.alignment = Alignment(horizontal="center")
        
    for r_idx, emp in enumerate(employees_raw, start=4):
        for c_idx, val in enumerate(emp, start=1):
            cell = ws_raw.cell(row=r_idx, column=c_idx, value=val)
            cell.border = CELL_BORDER
            cell.font = REGULAR_FONT
            if c_idx == 6:
                cell.number_format = '$#,##0.00'
                cell.alignment = Alignment(horizontal="right")
            elif c_idx in [1, 7, 8]:
                cell.alignment = Alignment(horizontal="center")
            if r_idx % 2 == 1:
                cell.fill = ZEBRA_FILL
                
    autofit_columns(ws_raw, min_col=1, max_col=8)
    
    wb.save(EXCEL_PATH)
    print("Excel workbook created:", EXCEL_PATH)

if __name__ == "__main__":
    create_workbook()
