import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

def generate_task6_visual():
    fig = plt.figure(figsize=(13, 8), dpi=200)
    fig.patch.set_facecolor('#F1F5F9')
    
    plt.suptitle("Task 6: Data Formatting, Sorting & Filtering", 
                 fontsize=14, weight='bold', color='#0F172A', y=0.96)
    plt.figtext(0.5, 0.92, "AutoFilter Enabled | Sorted by Department (A-Z) and Salary (High to Low)",
                fontsize=10, ha='center', color='#475569')

    data = [
        ["1001", "Sarah Connor", "Lead Data Engineer", "Engineering", "San Francisco", "$98,000.00", "2021-03-15", "5"],
        ["1002", "Michael Chen", "Senior Software Engineer", "Engineering", "San Francisco", "$92,000.00", "2020-07-11", "4"],
        ["1009", "Brian O'Connor", "DevOps Engineer", "Engineering", "San Francisco", "$89,000.00", "2021-12-01", "4"],
        ["1014", "Sophia Loren", "Frontend Engineer", "Engineering", "San Francisco", "$81,000.00", "2022-10-01", "4"],
        ["1003", "Emily Watson", "Senior Data Analyst", "Data Analytics", "New York", "$85,000.00", "2021-09-01", "5"],
        ["1004", "David Kim", "BI Developer", "Data Analytics", "New York", "$74,000.00", "2022-01-10", "4"],
        ["1010", "Lisa Ray", "Junior Data Analyst", "Data Analytics", "New York", "$58,000.00", "2023-04-12", "3"],
        ["1015", "Alexander Vance", "Strategic Advisor", "Executive Advisory", "Remote", "$115,000.00", "2024-01-05", "5"],
        ["1008", "Amanda Martinez", "HR Business Partner", "Human Resources", "Boston", "$67,000.00", "2021-08-05", "4"],
        ["1013", "Daniel Craig", "Recruiting Coordinator", "Human Resources", "Boston", "$52,000.00", "2023-08-20", "3"],
        ["1005", "Jessica Alba", "Digital Marketing Manager", "Marketing", "Chicago", "$71,000.00", "2019-11-20", "3"],
        ["1011", "Kevin Patel", "Content Strategist", "Marketing", "Chicago", "$56,000.00", "2023-02-01", "3"],
        ["1006", "James Wilson", "Enterprise Account Exec", "Sales", "Austin", "$88,000.00", "2020-02-14", "4"],
        ["1007", "Robert Taylor", "Sales Specialist", "Sales", "Austin", "$62,000.00", "2022-05-18", "3"],
        ["1012", "Rachel Green", "Inside Sales Rep", "Sales", "Austin", "$54,000.00", "2023-06-15", "2"],
        ["Total / Avg", "15 Employees", "---", "6 Departments", "6 Locations", "$1,162,000.00", "Avg Rating", "3.80"]
    ]
    
    headers = [
        "Emp ID ▼", "Employee Name ▼", "Job Title ▼", "Department ▼", 
        "Location ▼", "Salary ▼", "Hire Date ▼", "Rating ▼"
    ]
    
    ax = fig.add_axes([0.04, 0.10, 0.92, 0.78])
    ax.axis('off')
    
    table = ax.table(
        cellText=data,
        colLabels=headers,
        cellLoc='center',
        loc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1.0, 1.45)
    
    for col_idx in range(len(headers)):
        c = table[(0, col_idx)]
        c.set_facecolor('#1E3A8A')
        c.set_text_props(weight='bold', color='white')
        c.set_edgecolor('#CBD5E1')
        
    for row_idx in range(1, len(data) + 1):
        for col_idx in range(len(headers)):
            c = table[(row_idx, col_idx)]
            c.set_edgecolor('#E2E8F0')
            
            if col_idx in [1, 2, 3, 4]:
                c.set_text_props(ha='left')
            elif col_idx == 5:
                c.set_text_props(ha='right')
                
            if row_idx == len(data):
                c.set_facecolor('#E2E8F0')
                c.set_text_props(weight='bold', color='#0F172A')
                c.set_edgecolor('#94A3B8')
            elif row_idx % 2 == 1:
                c.set_facecolor('#F8FAFC')
            else:
                c.set_facecolor('#FFFFFF')
                
    out_path = os.path.join(SCREENSHOTS_DIR, "task6_formatting_sorting_filtering.png")
    plt.savefig(out_path, bbox_inches='tight', dpi=200)
    plt.close()

def generate_task7_visual():
    fig = plt.figure(figsize=(14, 9), dpi=200)
    fig.patch.set_facecolor('#F8FAFC')
    
    plt.suptitle("Task 7: Conditional Formatting & Excel Functions", 
                 fontsize=14, weight='bold', color='#0F172A', y=0.97)
    plt.figtext(0.5, 0.94, "IF(), COUNTIF(), SUMIF() | Color Scale: Green (>= $85k), Yellow ($65k-$84.9k), Red (< $65k)",
                fontsize=10, ha='center', color='#475569')

    headers = ["Emp ID", "Full Name", "Department", "Salary", "Rating", "Bonus Tier (IF)", "Appraisal Status (IF)"]
    data = [
        ["1001", "Sarah Connor", "Engineering", "$98,000.00", "5", "High (15%)", "Exceeds Expectations"],
        ["1002", "Michael Chen", "Engineering", "$92,000.00", "4", "High (15%)", "Exceeds Expectations"],
        ["1003", "Emily Watson", "Data Analytics", "$85,000.00", "5", "High (15%)", "Exceeds Expectations"],
        ["1004", "David Kim", "Data Analytics", "$74,000.00", "4", "Mid (10%)", "Exceeds Expectations"],
        ["1005", "Jessica Alba", "Marketing", "$71,000.00", "3", "Mid (10%)", "Meets Expectations"],
        ["1006", "James Wilson", "Sales", "$88,000.00", "4", "High (15%)", "Exceeds Expectations"],
        ["1007", "Robert Taylor", "Sales", "$62,000.00", "3", "Base (5%)", "Meets Expectations"],
        ["1008", "Amanda Martinez", "Human Resources", "$67,000.00", "4", "Mid (10%)", "Exceeds Expectations"],
        ["1009", "Brian O'Connor", "Engineering", "$89,000.00", "4", "High (15%)", "Exceeds Expectations"],
        ["1010", "Lisa Ray", "Data Analytics", "$58,000.00", "3", "Base (5%)", "Meets Expectations"],
        ["1011", "Kevin Patel", "Marketing", "$56,000.00", "3", "Base (5%)", "Meets Expectations"],
        ["1012", "Rachel Green", "Sales", "$54,000.00", "2", "Base (5%)", "Meets Expectations"],
        ["1013", "Daniel Craig", "Human Resources", "$52,000.00", "3", "Base (5%)", "Meets Expectations"],
        ["1014", "Sophia Loren", "Engineering", "$81,000.00", "4", "Mid (10%)", "Exceeds Expectations"],
        ["1015", "Alexander Vance", "Executive Advisory", "$115,000.00", "5", "High (15%)", "Exceeds Expectations"]
    ]
    
    ax_table = fig.add_axes([0.03, 0.40, 0.94, 0.52])
    ax_table.axis('off')
    
    table = ax_table.table(
        cellText=data,
        colLabels=headers,
        cellLoc='center',
        loc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.2)
    table.scale(1.0, 1.35)
    
    for c_idx in range(len(headers)):
        c = table[(0, c_idx)]
        c.set_facecolor('#1E3A8A')
        c.set_text_props(weight='bold', color='white')
        c.set_edgecolor('#CBD5E1')
        
    for r_idx in range(1, len(data) + 1):
        for c_idx in range(len(headers)):
            c = table[(r_idx, c_idx)]
            c.set_edgecolor('#E2E8F0')
            
            if c_idx in [1, 2]:
                c.set_text_props(ha='left')
            elif c_idx == 3:
                c.set_text_props(ha='right')
                sal_num = float(data[r_idx-1][3].replace('$', '').replace(',', ''))
                if sal_num >= 85000:
                    c.set_facecolor('#D1FAE5')
                    c.set_text_props(color='#065F46', weight='bold', ha='right')
                elif sal_num >= 65000:
                    c.set_facecolor('#FEF3C7')
                    c.set_text_props(color='#92400E', weight='bold', ha='right')
                else:
                    c.set_facecolor('#FEE2E2')
                    c.set_text_props(color='#991B1B', weight='bold', ha='right')
            else:
                if r_idx % 2 == 1:
                    c.set_facecolor('#F8FAFC')
                else:
                    c.set_facecolor('#FFFFFF')

    ax_fn = fig.add_axes([0.03, 0.05, 0.94, 0.30])
    ax_fn.axis('off')
    
    fn_headers = ["Metric Description", "Formula", "Calculated Value", "Purpose"]
    fn_rows = [
        ["Engineering Headcount", '=COUNTIF(C5:C19, "Engineering")', "4", "Counts employees in Engineering"],
        ["Data Analytics Headcount", '=COUNTIF(C5:C19, "Data Analytics")', "3", "Counts employees in Data Analytics"],
        ["High Performers (Score >= 4)", '=COUNTIF(E5:E19, ">=4")', "9", "Counts staff with rating of 4 or 5"],
        ["Total Engineering Payroll", '=SUMIF(C5:C19, "Engineering", D5:D19)', "$360,000.00", "Sums salaries in Engineering"],
        ["Total Analytics Payroll", '=SUMIF(C5:C19, "Data Analytics", D5:D19)', "$217,000.00", "Sums salaries in Data Analytics"],
        ["Total Sales Payroll", '=SUMIF(C5:C19, "Sales", D5:D19)', "$204,000.00", "Sums salaries in Sales"]
    ]
    
    t_fn = ax_fn.table(
        cellText=fn_rows,
        colLabels=fn_headers,
        cellLoc='center',
        loc='center'
    )
    t_fn.auto_set_font_size(False)
    t_fn.set_fontsize(8.2)
    t_fn.scale(1.0, 1.35)
    
    for c_idx in range(len(fn_headers)):
        c = t_fn[(0, c_idx)]
        c.set_facecolor('#0284C7')
        c.set_text_props(weight='bold', color='white')
        c.set_edgecolor('#CBD5E1')
        
    for r_idx in range(1, len(fn_rows) + 1):
        for c_idx in range(len(fn_headers)):
            c = t_fn[(r_idx, c_idx)]
            c.set_edgecolor('#E2E8F0')
            if c_idx == 0:
                c.set_text_props(ha='left', weight='bold')
            elif c_idx == 1:
                c.set_text_props(ha='left', color='#047857')
            elif c_idx == 2:
                c.set_text_props(ha='right', weight='bold')
            elif c_idx == 3:
                c.set_text_props(ha='left')
            if r_idx % 2 == 1:
                c.set_facecolor('#F8FAFC')
            else:
                c.set_facecolor('#FFFFFF')

    out_path = os.path.join(SCREENSHOTS_DIR, "task7_conditional_formatting_functions.png")
    plt.savefig(out_path, bbox_inches='tight', dpi=200)
    plt.close()

def generate_task8_visual():
    fig = plt.figure(figsize=(14, 9), dpi=200)
    fig.patch.set_facecolor('#F8FAFC')
    
    plt.suptitle("Task 8: VLOOKUP & XLOOKUP", 
                 fontsize=14, weight='bold', color='#0F172A', y=0.97)
    plt.figtext(0.5, 0.94, "Retrieving department details and demonstrating reverse search with XLOOKUP",
                fontsize=10, ha='center', color='#475569')

    ax_top_left = fig.add_axes([0.02, 0.58, 0.54, 0.33])
    ax_top_left.axis('off')
    ax_top_left.set_title("Employee Lookups", fontsize=10, weight='bold', color='#1E3A8A', loc='left')
    
    emp_headers = ["Emp ID", "Full Name", "Dept Code", "VLOOKUP Dept", "VLOOKUP Location", "XLOOKUP Head"]
    emp_data = [
        ["1001", "Sarah Connor", "101", "Engineering", "San Francisco", "Dr. Elena Rostova"],
        ["1003", "Emily Watson", "102", "Data Analytics", "New York", "Marcus Brody"],
        ["1005", "Jessica Alba", "103", "Marketing", "Chicago", "Victoria Sterling"],
        ["1006", "James Wilson", "104", "Sales", "Austin", "Gregory House"],
        ["1008", "Amanda Martinez", "105", "Human Resources", "Boston", "Clara Oswald"],
        ["1010", "Lisa Ray", "102", "Data Analytics", "New York", "Marcus Brody"],
        ["1014", "Sophia Loren", "101", "Engineering", "San Francisco", "Dr. Elena Rostova"],
        ["1015", "Alexander Vance", "999", "Not Found", "N/A", "Not Found"]
    ]
    t_emp = ax_top_left.table(cellText=emp_data, colLabels=emp_headers, cellLoc='center', loc='center')
    t_emp.auto_set_font_size(False)
    t_emp.set_fontsize(7.5)
    t_emp.scale(1.0, 1.3)
    for c_idx in range(len(emp_headers)):
        t_emp[(0, c_idx)].set_facecolor('#1E3A8A')
        t_emp[(0, c_idx)].set_text_props(weight='bold', color='white')
    for r_idx in range(1, len(emp_data) + 1):
        for c_idx in range(len(emp_headers)):
            cell = t_emp[(r_idx, c_idx)]
            cell.set_edgecolor('#CBD5E1')
            if r_idx == len(emp_data) and c_idx >= 3:
                cell.set_facecolor('#FEE2E2')
                cell.set_text_props(color='#991B1B', weight='bold')
            elif r_idx % 2 == 1:
                cell.set_facecolor('#F8FAFC')
            else:
                cell.set_facecolor('#FFFFFF')

    ax_top_right = fig.add_axes([0.58, 0.58, 0.40, 0.33])
    ax_top_right.axis('off')
    ax_top_right.set_title("Department Reference Directory ($H$6:$L$11)", fontsize=10, weight='bold', color='#1E3A8A', loc='left')
    
    dept_headers = ["Dept Code", "Department Name", "Location", "Budget", "Department Head"]
    dept_data = [
        ["101", "Engineering", "San Francisco", "$1,250,000", "Dr. Elena Rostova"],
        ["102", "Data Analytics", "New York", "$950,000", "Marcus Brody"],
        ["103", "Marketing", "Chicago", "$600,000", "Victoria Sterling"],
        ["104", "Sales", "Austin", "$800,000", "Gregory House"],
        ["105", "Human Resources", "Boston", "$450,000", "Clara Oswald"],
        ["106", "Research & Dev", "Seattle", "$1,100,000", "Dr. Emmett Brown"]
    ]
    t_dept = ax_top_right.table(cellText=dept_data, colLabels=dept_headers, cellLoc='center', loc='center')
    t_dept.auto_set_font_size(False)
    t_dept.set_fontsize(7.5)
    t_dept.scale(1.0, 1.45)
    for c_idx in range(len(dept_headers)):
        t_dept[(0, c_idx)].set_facecolor('#0F766E')
        t_dept[(0, c_idx)].set_text_props(weight='bold', color='white')
    for r_idx in range(1, len(dept_data) + 1):
        for c_idx in range(len(dept_headers)):
            cell = t_dept[(r_idx, c_idx)]
            cell.set_edgecolor('#CBD5E1')
            if r_idx % 2 == 1:
                cell.set_facecolor('#F0FDFA')
            else:
                cell.set_facecolor('#FFFFFF')

    ax_mid = fig.add_axes([0.02, 0.36, 0.96, 0.17])
    ax_mid.axis('off')
    ax_mid.set_title("Reverse Lookup with XLOOKUP", fontsize=10, weight='bold', color='#047857', loc='left')
    
    rev_headers = ["Input: Department Head", "XLOOKUP Formula", "Retrieved Dept Code", "Retrieved Dept Name"]
    rev_data = [
        ["Dr. Elena Rostova", '=XLOOKUP("Dr. Elena Rostova", $L$6:$L$11, $H$6:$H$11, "N/A")', "101", "Engineering"],
        ["Marcus Brody", '=XLOOKUP("Marcus Brody", $L$6:$L$11, $H$6:$H$11, "N/A")', "102", "Data Analytics"],
        ["Dr. Emmett Brown", '=XLOOKUP("Dr. Emmett Brown", $L$6:$L$11, $H$6:$H$11, "N/A")', "106", "Research & Dev"]
    ]
    t_rev = ax_mid.table(cellText=rev_data, colLabels=rev_headers, cellLoc='center', loc='center')
    t_rev.auto_set_font_size(False)
    t_rev.set_fontsize(7.8)
    t_rev.scale(1.0, 1.4)
    for c_idx in range(len(rev_headers)):
        t_rev[(0, c_idx)].set_facecolor('#047857')
        t_rev[(0, c_idx)].set_text_props(weight='bold', color='white')
    for r_idx in range(1, len(rev_data) + 1):
        for c_idx in range(len(rev_headers)):
            cell = t_rev[(r_idx, c_idx)]
            cell.set_edgecolor('#CBD5E1')
            if c_idx == 1:
                cell.set_text_props(ha='left', color='#047857')
            if r_idx % 2 == 1:
                cell.set_facecolor('#F0FDF4')

    ax_bot = fig.add_axes([0.02, 0.04, 0.96, 0.28])
    ax_bot.axis('off')
    ax_bot.set_title("Key Differences Between VLOOKUP and XLOOKUP", fontsize=10, weight='bold', color='#1E3A8A', loc='left')
    
    comp_headers = ["Feature", "VLOOKUP", "XLOOKUP", "Key Difference"]
    comp_rows = [
        ["Lookup Direction", "Left-to-right only", "Any direction (left, right, vertical, horizontal)", "XLOOKUP can look to the left"],
        ["Match Default", "Approximate match (TRUE)", "Exact match (0)", "XLOOKUP is safer by default"],
        ["Column Insertion", "Breaks formula if index changes", "Range references update automatically", "XLOOKUP does not break easily"],
        ["Missing Values", "Needs IFERROR() wrapper", "Has built-in if_not_found argument", "XLOOKUP has cleaner syntax"],
        ["Compatibility", "Works on all Excel versions", "Requires Excel 365 or Excel 2021+", "VLOOKUP is better for older Excel versions"]
    ]
    t_bot = ax_bot.table(cellText=comp_rows, colLabels=comp_headers, cellLoc='center', loc='center')
    t_bot.auto_set_font_size(False)
    t_bot.set_fontsize(7.8)
    t_bot.scale(1.0, 1.35)
    for c_idx in range(len(comp_headers)):
        t_bot[(0, c_idx)].set_facecolor('#334155')
        t_bot[(0, c_idx)].set_text_props(weight='bold', color='white')
    for r_idx in range(1, len(comp_rows) + 1):
        for c_idx in range(len(comp_headers)):
            cell = t_bot[(r_idx, c_idx)]
            cell.set_edgecolor('#CBD5E1')
            if c_idx == 3:
                cell.set_text_props(weight='bold', color='#1E3A8A')
            if r_idx % 2 == 1:
                cell.set_facecolor('#F8FAFC')
            else:
                cell.set_facecolor('#FFFFFF')

    out_path = os.path.join(SCREENSHOTS_DIR, "task8_vlookup_xlookup.png")
    plt.savefig(out_path, bbox_inches='tight', dpi=200)
    plt.close()

def generate_task9_visual():
    fig = plt.figure(figsize=(14, 8.5), dpi=200)
    fig.patch.set_facecolor('#F8FAFC')
    
    plt.suptitle("Task 9: Pivot Table & Chart", 
                 fontsize=14, weight='bold', color='#0F172A', y=0.97)
    plt.figtext(0.5, 0.94, "Department summary and salary comparison",
                fontsize=10, ha='center', color='#475569')

    ax_piv = fig.add_axes([0.03, 0.15, 0.52, 0.74])
    ax_piv.axis('off')
    ax_piv.set_title("Pivot Table Summary", fontsize=11, weight='bold', color='#1E3A8A', loc='left')
    
    piv_headers = ["Department", "Staff", "Total Payroll", "Average Salary", "Min", "Max", "% Share"]
    piv_rows = [
        ["Engineering", "4", "$360,000", "$90,000", "$81,000", "$98,000", "30.2%"],
        ["Data Analytics", "3", "$217,000", "$72,333", "$58,000", "$85,000", "18.2%"],
        ["Sales", "3", "$204,000", "$68,000", "$54,000", "$88,000", "17.1%"],
        ["Human Resources", "2", "$119,000", "$59,500", "$52,000", "$67,000", "10.0%"],
        ["Marketing", "2", "$127,000", "$63,500", "$56,000", "$71,000", "10.7%"],
        ["Executive Advisory", "1", "$115,000", "$115,000", "$115,000", "$115,000", "9.7%"],
        ["Research & Dev", "0", "$0", "$0", "$0", "$0", "0.0%"],
        ["Total", "15", "$1,162,000", "$77,467", "$52,000", "$115,000", "100.0%"]
    ]
    t_piv = ax_piv.table(cellText=piv_rows, colLabels=piv_headers, cellLoc='center', loc='center')
    t_piv.auto_set_font_size(False)
    t_piv.set_fontsize(8.2)
    t_piv.scale(1.0, 1.8)
    
    for c_idx in range(len(piv_headers)):
        t_piv[(0, c_idx)].set_facecolor('#1E3A8A')
        t_piv[(0, c_idx)].set_text_props(weight='bold', color='white')
        
    for r_idx in range(1, len(piv_rows) + 1):
        for c_idx in range(len(piv_headers)):
            cell = t_piv[(r_idx, c_idx)]
            cell.set_edgecolor('#CBD5E1')
            if c_idx == 0:
                cell.set_text_props(ha='left')
            elif c_idx in [2, 3, 4, 5, 6]:
                cell.set_text_props(ha='right')
                
            if r_idx == len(piv_rows):
                cell.set_facecolor('#E2E8F0')
                cell.set_text_props(weight='bold', color='#0F172A')
                cell.set_edgecolor('#94A3B8')
            elif r_idx % 2 == 1:
                cell.set_facecolor('#F8FAFC')
            else:
                cell.set_facecolor('#FFFFFF')

    ax_chart = fig.add_axes([0.58, 0.28, 0.39, 0.60])
    departments = ["Executive", "Engineering", "Data Analytics", "Sales", "Marketing", "HR"]
    avg_salaries = [115000, 90000, 72333, 68000, 63500, 59500]
    colors = ['#4338CA', '#1D4ED8', '#0284C7', '#0D9488', '#F59E0B', '#E11D48']
    
    bars = ax_chart.bar(departments, avg_salaries, color=colors, width=0.6, edgecolor='#0F172A', linewidth=0.8, alpha=0.9)
    ax_chart.set_title("Average Salary by Department ($ USD)", fontsize=11, weight='bold', color='#1E3A8A', pad=12)
    ax_chart.set_ylabel("Average Salary ($)", fontsize=9.5, weight='bold')
    ax_chart.grid(axis='y', linestyle='--', alpha=0.4)
    ax_chart.set_ylim(0, 130000)
    ax_chart.yaxis.set_major_formatter('${x:,.0f}')
    plt.xticks(rotation=25, ha='right', fontsize=8.5, weight='bold')
    
    for bar in bars:
        h = bar.get_height()
        ax_chart.text(bar.get_x() + bar.get_width()/2., h + 2200, f'${h:,.0f}',
                      ha='center', va='bottom', fontsize=8, weight='bold', color='#1E293B')
                      
    ax_callout = fig.add_axes([0.58, 0.06, 0.39, 0.16])
    ax_callout.axis('off')
    
    callout_box = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.04", 
                                        edgecolor="#3B82F6", facecolor="#EFF6FF", linewidth=1.2)
    ax_callout.add_patch(callout_box)
    
    insight_text = (
        "Chart Summary:\n"
        "- Executive Advisory has the highest salary ($115,000).\n"
        "- Engineering has the second highest average salary ($90,000).\n"
        "- Engineering takes up the largest share of payroll (30.2%)."
    )
    ax_callout.text(0.04, 0.5, insight_text, fontsize=8, color='#1E3A8A', va='center', weight='bold', linespacing=1.4)

    out_path = os.path.join(SCREENSHOTS_DIR, "task9_pivot_table_and_chart.png")
    plt.savefig(out_path, bbox_inches='tight', dpi=200)
    plt.close()

if __name__ == "__main__":
    generate_task6_visual()
    generate_task7_visual()
    generate_task8_visual()
    generate_task9_visual()
    print("Visuals generated successfully.")
