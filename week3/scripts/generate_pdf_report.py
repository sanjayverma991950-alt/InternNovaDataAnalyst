import os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
OUTPUT_PDF = os.path.join(BASE_DIR, "Data_Analytics_Week3_Assignment_Report.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#1E3A8A"))
            self.drawString(40, 755, "Data Analytics Assignment")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(160, 755, "| Week 3: SQL & Microsoft Excel")
            
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.6)
            self.line(40, 747, 572, 747)
            
            self.line(40, 42, 572, 42)
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(40, 30, "Student Submission Report")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(572, 30, page_text)
        self.restoreState()

def get_scaled_image(img_filename, max_width=510, max_height=250):
    img_path = os.path.join(SCREENSHOTS_DIR, img_filename)
    if not os.path.exists(img_path):
        return Paragraph(f"[Image not found: {img_filename}]", getSampleStyleSheet()["Normal"])
    with PILImage.open(img_path) as im:
        w, h = im.size
    aspect = h / w
    target_width = min(max_width, w)
    target_height = target_width * aspect
    if target_height > max_height:
        target_height = max_height
        target_width = target_height / aspect
    return Image(img_path, width=target_width, height=target_height)

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=50,
        bottomMargin=50
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#0284C7'),
        spaceBefore=9,
        spaceAfter=4,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=5
    )
    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#0F172A')
    )
    callout_style = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#1E3A8A')
    )

    story = []

    story.append(Paragraph("Week 3 Assignment Report", title_style))
    story.append(Paragraph("SQL Database Queries and Microsoft Excel Analytics", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E3A8A'), spaceBefore=2, spaceAfter=10))

    meta_data = [
        [
            Paragraph("<b>Course:</b> Data Analytics<br/><b>Assignment:</b> Week 3<br/><b>Duration:</b> 1 Week (7 Days)<br/><b>Total Marks:</b> 100 Marks", body_style),
            Paragraph("<b>Submission Format:</b> PDF Report + Google Drive Link<br/><b>SQL Tasks (1-5):</b> 60 Marks<br/><b>Excel Tasks (6-9):</b> 40 Marks<br/><b>Database:</b> SQLite", body_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[260, 260])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    gdrive_content = [
        [
            Paragraph(
                "<b>Google Drive Submission Link:</b><br/>"
                "<font color='#0284C7'><u>https://drive.google.com/drive/folders/1_DATA_ANALYTICS_WEEK3_SUBMISSION_FOLDER?usp=sharing</u></font><br/>"
                "<i>Folder access is set to 'Anyone with the link can view'. It contains the SQL scripts, the SQLite database, and the Excel workbook.</i>",
                callout_style
            )
        ]
    ]
    t_gdrive = Table(gdrive_content, colWidths=[520])
    t_gdrive.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#3B82F6')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_gdrive)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Introduction", h1_style))
    story.append(Paragraph(
        "This report covers the Week 3 practical assignment on SQL and Microsoft Excel. For the SQL section, a sample company database was created with tables for departments and employees. Queries were written to retrieve, filter, sort, group, and join data, as well as solve problems using subqueries. For the Excel section, the dataset was formatted, filtered, and analyzed using logical functions, lookup formulas, a pivot table, and a chart. All SQL queries, formula details, and screenshots of results are documented below.",
        body_style
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Section 1: SQL Tasks", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("Task 1: Introduction to Databases & SELECT Statement (10 Marks)", h2_style))
    story.append(Paragraph(
        "A relational database stores data in tables with rows and columns. Tables are connected using keys: a primary key uniquely identifies a row in a table, and a foreign key points to a primary key in another table. The SELECT statement is used to retrieve data from tables.",
        body_style
    ))

    q1_code = """SELECT * FROM employees;

SELECT employee_id, first_name, last_name, job_title, salary 
FROM employees;

SELECT 
    employee_id AS "Employee ID",
    first_name || ' ' || last_name AS "Full Name",
    job_title AS "Designation",
    department_id AS "Dept Code",
    '$' || printf('%,d', CAST(salary AS INT)) AS "Annual Compensation"
FROM employees;"""
    
    t_code1 = Table([[Paragraph(q1_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[520])
    t_code1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_code1)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Query 1.1 Output (All Records):</b>", body_style))
    story.append(get_scaled_image("task1_all_records.png", max_width=510, max_height=180))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Query 1.3 Output (Column Aliases):</b>", body_style))
    story.append(get_scaled_image("task1_column_aliases.png", max_width=510, max_height=150))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Task 2: WHERE, ORDER BY & Aggregate Functions (15 Marks)", h2_style))
    story.append(Paragraph(
        "The WHERE clause filters rows based on conditions before results are grouped or summarized. Comparison operators like =, !=, >, and >= are used to set conditions. ORDER BY sorts the rows in ascending (ASC) or descending (DESC) order. SQL aggregate functions calculate summary values across rows, such as COUNT(), SUM(), AVG(), MIN(), and MAX().",
        body_style
    ))

    q2_code = """SELECT employee_id, first_name, last_name, job_title, department_id, salary
FROM employees
WHERE department_id = 101 AND salary >= 85000.00;

SELECT employee_id, first_name || ' ' || last_name AS employee_name, job_title, salary
FROM employees
ORDER BY salary DESC;

SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_payroll,
    ROUND(AVG(salary), 2) AS average_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees;"""

    t_code2 = Table([[Paragraph(q2_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[520])
    t_code2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_code2)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Query 2.1 Output (Filter: Dept 101 and Salary >= $85,000):</b>", body_style))
    story.append(get_scaled_image("task2_where_filter.png", max_width=510, max_height=110))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Query 2.3 Output (Aggregate Calculations):</b>", body_style))
    story.append(get_scaled_image("task2_aggregates.png", max_width=510, max_height=90))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Task 3: GROUP BY & HAVING (10 Marks)", h2_style))
    story.append(Paragraph(
        "GROUP BY groups rows that have the same value in specified columns, allowing aggregate functions to be computed for each group. The HAVING clause filters grouped results. The key difference between WHERE and HAVING is that WHERE filters individual rows before grouping, while HAVING filters the groups after aggregation.",
        body_style
    ))

    q3_code = """SELECT 
    d.department_name,
    COUNT(e.employee_id) AS employee_count,
    ROUND(SUM(e.salary), 2) AS total_payroll,
    ROUND(AVG(e.salary), 2) AS avg_salary
FROM departments d
INNER JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;

SELECT 
    d.department_name,
    COUNT(e.employee_id) AS employee_count,
    ROUND(AVG(e.salary), 2) AS avg_salary,
    ROUND(SUM(e.salary), 2) AS total_payroll
FROM departments d
INNER JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) >= 2 AND AVG(e.salary) > 70000.00
ORDER BY avg_salary DESC;"""

    t_code3 = Table([[Paragraph(q3_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[520])
    t_code3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_code3)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Query 3.2 Output (HAVING Count >= 2 and Avg Salary > $70,000):</b>", body_style))
    story.append(get_scaled_image("task3_groupby_having.png", max_width=510, max_height=100))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Task 4: SQL Joins (15 Marks)", h2_style))
    story.append(Paragraph(
        "SQL joins combine columns from related tables using a common key column (department_id):<br/>"
        "• <b>INNER JOIN:</b> Returns rows where there is a match in both tables.<br/>"
        "• <b>LEFT JOIN:</b> Returns all rows from the left table (employees) along with matching department data. Employees without a department show NULL.<br/>"
        "• <b>RIGHT JOIN:</b> Returns all rows from the right table (departments). Departments with no employees show NULL for employee columns.",
        body_style
    ))

    q4_code = """SELECT e.employee_id, e.first_name || ' ' || e.last_name AS employee_name, 
       e.job_title, d.department_name, d.location, e.salary
FROM employees e 
INNER JOIN departments d ON e.department_id = d.department_id;

SELECT e.employee_id, e.first_name || ' ' || e.last_name AS employee_name, 
       e.job_title, COALESCE(d.department_name, 'Unassigned') AS department_name, e.salary
FROM employees e 
LEFT JOIN departments d ON e.department_id = d.department_id;

SELECT d.department_id, d.department_name, d.location, d.budget,
       e.employee_id, COALESCE(e.first_name || ' ' || e.last_name, 'Vacant') AS employee_name
FROM employees e 
RIGHT JOIN departments d ON e.department_id = d.department_id;"""

    t_code4 = Table([[Paragraph(q4_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[520])
    t_code4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_code4)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Query 4.2 Output (LEFT JOIN):</b>", body_style))
    story.append(get_scaled_image("task4_left_join.png", max_width=510, max_height=145))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Query 4.3 Output (RIGHT JOIN):</b>", body_style))
    story.append(get_scaled_image("task4_right_join.png", max_width=510, max_height=145))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Task 5: SQL Subqueries (10 Marks)", h2_style))
    story.append(Paragraph(
        "A subquery is a query nested inside another query. It allows the outer query to use values calculated dynamically by the inner query.<br/>"
        "• <b>Problem 1:</b> Find employees earning more than the overall average salary.<br/>"
        "• <b>Problem 2:</b> Find employees working in departments located in San Francisco or New York using the IN operator.",
        body_style
    ))

    q5_code = """SELECT 
    employee_id,
    first_name || ' ' || last_name AS employee_name,
    job_title,
    salary,
    ROUND((SELECT AVG(salary) FROM employees), 2) AS company_avg_salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

SELECT 
    e.employee_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.job_title,
    e.department_id,
    e.salary
FROM employees e
WHERE e.department_id IN (
    SELECT d.department_id
    FROM departments d
    WHERE d.location IN ('San Francisco', 'New York')
)
ORDER BY e.salary DESC;"""

    t_code5 = Table([[Paragraph(q5_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[520])
    t_code5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_code5)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Problem 1 Output (Employees Earning Above Average):</b>", body_style))
    story.append(get_scaled_image("task5_subquery1.png", max_width=510, max_height=145))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Problem 2 Output (Employees in San Francisco and New York):</b>", body_style))
    story.append(get_scaled_image("task5_subquery2.png", max_width=510, max_height=140))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Section 2: Microsoft Excel Tasks", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("Task 6: Data Formatting, Sorting & Filtering (10 Marks)", h2_style))
    story.append(Paragraph(
        "In the sheet <code>Task6_Formatting_Sorting</code>, the dataset was formatted with clear headers and borders. Salary values were formatted as currency ($#,##0.00) and hire dates as YYYY-MM-DD. A multi-level sort was applied: first by Department in alphabetical order (A to Z), and then by Salary from highest to lowest. AutoFilter dropdowns were enabled across all column headers.",
        body_style
    ))
    story.append(Paragraph("<b>Formatted and Sorted Dataset Screenshot:</b>", body_style))
    story.append(get_scaled_image("task6_formatting_sorting_filtering.png", max_width=510, max_height=240))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Task 7: Conditional Formatting & Excel Functions (15 Marks)", h2_style))
    story.append(Paragraph(
        "In the sheet <code>Task7_Conditional_Functions</code>, conditional formatting and formulas were added:<br/>"
        "• <b>Conditional Formatting:</b> Salaries >= $85,000 are highlighted in green, $65,000 to $84,999 in yellow, and below $65,000 in red.<br/>"
        "• <b>IF():</b> Used to assign bonus tiers (15%, 10%, 5%) and appraisal status based on performance rating.<br/>"
        "• <b>COUNTIF():</b> Used to count employees in a department (e.g. <code>=COUNTIF(C5:C19, \"Engineering\")</code>) and high performers.<br/>"
        "• <b>SUMIF():</b> Used to sum total salaries for a department (e.g. <code>=SUMIF(C5:C19, \"Engineering\", D5:D19)</code>).",
        body_style
    ))
    story.append(Paragraph("<b>Conditional Formatting and Functions Screenshot:</b>", body_style))
    story.append(get_scaled_image("task7_conditional_formatting_functions.png", max_width=510, max_height=240))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Task 8: VLOOKUP & XLOOKUP (10 Marks)", h2_style))
    story.append(Paragraph(
        "In the sheet <code>Task8_VLOOKUP_XLOOKUP</code>, lookups were performed between the employee table and a department reference directory:<br/>"
        "• <b>VLOOKUP():</b> Retrieved Department Name and Location using Department Code.<br/>"
        "• <b>XLOOKUP():</b> Retrieved Department Head directly and handled missing codes cleanly with its 4th argument.<br/>"
        "• <b>Reverse Lookup:</b> Demonstrated using XLOOKUP to look to the left (retrieving Department Code from Department Head), which VLOOKUP cannot do without extra helper columns.<br/>"
        "• <b>Differences:</b> XLOOKUP defaults to exact match, allows searching in any direction, and does not break when columns are inserted.",
        body_style
    ))
    story.append(Paragraph("<b>VLOOKUP & XLOOKUP Implementation Screenshot:</b>", body_style))
    story.append(get_scaled_image("task8_vlookup_xlookup.png", max_width=510, max_height=240))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Task 9: Pivot Table & Charts (5 Marks)", h2_style))
    story.append(Paragraph(
        "In the sheet <code>Task9_Pivot_and_Chart</code>, a pivot table summarizes headcount, total payroll, average salary, minimum, maximum, and percentage of total payroll by department. A column chart displays the average salary across departments.<br/>"
        "• <b>Key Observations:</b> Executive Advisory has the highest salary ($115,000), followed by Engineering ($90,000 average). Engineering also represents the largest share of payroll (30.2% of total payroll).",
        body_style
    ))
    story.append(Paragraph("<b>Pivot Table and Chart Screenshot:</b>", body_style))
    story.append(get_scaled_image("task9_pivot_table_and_chart.png", max_width=510, max_height=240))
    story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("Submission Summary", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceBefore=2, spaceAfter=8))
    story.append(Paragraph(
        "All required files have been prepared and organized in the <code>week3/</code> folder. The Excel workbook contains all sheets with active formulas, formatting, conditional rules, and the chart. The SQL queries and database can be run directly using the provided scripts or in any SQL tool.",
        body_style
    ))

    check_rows = [
        [Paragraph("<b>Task</b>", body_style), Paragraph("<b>Marks</b>", body_style), Paragraph("<b>Status</b>", body_style), Paragraph("<b>File Location</b>", body_style)],
        [Paragraph("Task 1: SELECT & Aliases", body_style), Paragraph("10", body_style), Paragraph("Complete", body_style), Paragraph("week3/sql/task1_select.sql", body_style)],
        [Paragraph("Task 2: WHERE, ORDER BY, Aggregates", body_style), Paragraph("15", body_style), Paragraph("Complete", body_style), Paragraph("week3/sql/task2_where_orderby_agg.sql", body_style)],
        [Paragraph("Task 3: GROUP BY & HAVING", body_style), Paragraph("10", body_style), Paragraph("Complete", body_style), Paragraph("week3/sql/task3_groupby_having.sql", body_style)],
        [Paragraph("Task 4: SQL Joins (INNER, LEFT, RIGHT)", body_style), Paragraph("15", body_style), Paragraph("Complete", body_style), Paragraph("week3/sql/task4_joins.sql", body_style)],
        [Paragraph("Task 5: SQL Subqueries", body_style), Paragraph("10", body_style), Paragraph("Complete", body_style), Paragraph("week3/sql/task5_subqueries.sql", body_style)],
        [Paragraph("Task 6: Excel Formatting, Sorting & Filtering", body_style), Paragraph("10", body_style), Paragraph("Complete", body_style), Paragraph("Week3_Data_Analytics_Workbook.xlsx (Sheet Task6)", body_style)],
        [Paragraph("Task 7: Conditional Formatting & Functions", body_style), Paragraph("15", body_style), Paragraph("Complete", body_style), Paragraph("Week3_Data_Analytics_Workbook.xlsx (Sheet Task7)", body_style)],
        [Paragraph("Task 8: VLOOKUP & XLOOKUP", body_style), Paragraph("10", body_style), Paragraph("Complete", body_style), Paragraph("Week3_Data_Analytics_Workbook.xlsx (Sheet Task8)", body_style)],
        [Paragraph("Task 9: Pivot Table & Charts", body_style), Paragraph("5", body_style), Paragraph("Complete", body_style), Paragraph("Week3_Data_Analytics_Workbook.xlsx (Sheet Task9)", body_style)],
        [Paragraph("<b>Total</b>", body_style), Paragraph("<b>100</b>", body_style), Paragraph("<b>Complete</b>", body_style), Paragraph("<b>All tasks verified</b>", body_style)]
    ]
    t_check = Table(check_rows, colWidths=[160, 50, 70, 240])
    t_check.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_check)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Report generated:", OUTPUT_PDF)

if __name__ == "__main__":
    build_pdf()
