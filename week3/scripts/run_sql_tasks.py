import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
DB_PATH = os.path.join(DATA_DIR, "company_database.db")

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    with open(os.path.join(DATA_DIR, "schema.sql"), "r", encoding="utf-8") as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    
    with open(os.path.join(DATA_DIR, "insert_data.sql"), "r", encoding="utf-8") as f:
        insert_sql = f.read()
    cursor.executescript(insert_sql)
    
    conn.commit()
    conn.close()

def render_table_to_image(df, title, filename):
    fig_width = max(8.5, len(df.columns) * 1.8)
    row_height = 0.38
    fig_height = max(2.5, (len(df) + 2) * row_height + 0.8)
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=200)
    ax.axis('off')
    
    plt.title(title, fontsize=13, weight='bold', pad=12, color='#1E3A8A', loc='left')
    
    cell_text = []
    for row in df.itertuples(index=False):
        formatted_row = []
        for val in row:
            if pd.isna(val) or val is None:
                formatted_row.append("NULL")
            elif isinstance(val, float):
                formatted_row.append(f"{val:,.2f}")
            else:
                formatted_row.append(str(val))
        cell_text.append(formatted_row)
        
    table = ax.table(
        cellText=cell_text,
        colLabels=list(df.columns),
        cellLoc='center',
        loc='center'
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(9.5)
    
    for (i, j), cell in table.get_celld().items():
        cell.set_edgecolor('#CBD5E1')
        cell.set_linewidth(0.8)
        if i == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#1E3A8A')
            cell.set_height(0.08 if len(df) < 5 else 0.05)
        else:
            if i % 2 == 1:
                cell.set_facecolor('#F8FAFC')
            else:
                cell.set_facecolor('#FFFFFF')
            cell.set_height(0.06 if len(df) < 5 else 0.04)
            
    plt.tight_layout()
    out_path = os.path.join(SCREENSHOTS_DIR, filename)
    plt.savefig(out_path, bbox_inches='tight', dpi=200)
    plt.close()
    return out_path

def execute_all_queries():
    conn = sqlite3.connect(DB_PATH)
    
    df1_all = pd.read_sql_query("SELECT * FROM employees;", conn)
    render_table_to_image(df1_all.head(10), "Task 1.1: SELECT * FROM employees (First 10 Rows)", "task1_all_records.png")
    
    q1_2 = "SELECT employee_id, first_name, last_name, job_title, salary FROM employees LIMIT 8;"
    df1_spec = pd.read_sql_query(q1_2, conn)
    render_table_to_image(df1_spec, "Task 1.2: SELECT Specific Columns", "task1_specific_columns.png")
    
    q1_3 = """
    SELECT 
        employee_id AS "Employee ID",
        first_name || ' ' || last_name AS "Full Name",
        job_title AS "Designation",
        department_id AS "Dept Code",
        '$' || printf('%,d', CAST(salary AS INT)) AS "Annual Compensation"
    FROM employees 
    LIMIT 8;
    """
    df1_alias = pd.read_sql_query(q1_3, conn)
    render_table_to_image(df1_alias, "Task 1.3: SELECT with Column Aliases", "task1_column_aliases.png")
    
    q2_1 = """
    SELECT employee_id, first_name, last_name, job_title, department_id, salary
    FROM employees
    WHERE department_id = 101 AND salary >= 85000.00;
    """
    df2_where = pd.read_sql_query(q2_1, conn)
    render_table_to_image(df2_where, "Task 2.1: WHERE Filter (Dept 101, Salary >= 85,000)", "task2_where_filter.png")
    
    q2_2 = """
    SELECT employee_id, first_name || ' ' || last_name AS employee_name, job_title, salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 8;
    """
    df2_order = pd.read_sql_query(q2_2, conn)
    render_table_to_image(df2_order, "Task 2.2: ORDER BY salary DESC", "task2_orderby.png")
    
    q2_3 = """
    SELECT 
        COUNT(*) AS total_employees,
        SUM(salary) AS total_payroll,
        ROUND(AVG(salary), 2) AS average_salary,
        MIN(salary) AS min_salary,
        MAX(salary) AS max_salary
    FROM employees;
    """
    df2_agg = pd.read_sql_query(q2_3, conn)
    render_table_to_image(df2_agg, "Task 2.3: Aggregate Functions", "task2_aggregates.png")
    
    q3_1 = """
    SELECT 
        d.department_name,
        COUNT(e.employee_id) AS employee_count,
        ROUND(SUM(e.salary), 2) AS total_payroll,
        ROUND(AVG(e.salary), 2) AS avg_salary,
        MIN(e.salary) AS min_salary,
        MAX(e.salary) AS max_salary
    FROM departments d
    INNER JOIN employees e ON d.department_id = e.department_id
    GROUP BY d.department_name
    ORDER BY avg_salary DESC;
    """
    df3_group = pd.read_sql_query(q3_1, conn)
    render_table_to_image(df3_group, "Task 3.1: GROUP BY Department", "task3_groupby.png")
    
    q3_2 = """
    SELECT 
        d.department_name,
        COUNT(e.employee_id) AS employee_count,
        ROUND(AVG(e.salary), 2) AS avg_salary,
        ROUND(SUM(e.salary), 2) AS total_payroll
    FROM departments d
    INNER JOIN employees e ON d.department_id = e.department_id
    GROUP BY d.department_name
    HAVING COUNT(e.employee_id) >= 2 AND AVG(e.salary) > 70000.00
    ORDER BY avg_salary DESC;
    """
    df3_having = pd.read_sql_query(q3_2, conn)
    render_table_to_image(df3_having, "Task 3.2: Filter Groups with HAVING", "task3_groupby_having.png")
    
    q4_inner = """
    SELECT 
        e.employee_id,
        e.first_name || ' ' || e.last_name AS employee_name,
        e.job_title,
        d.department_name,
        d.location,
        e.salary
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.department_id
    ORDER BY e.employee_id
    LIMIT 9;
    """
    df4_inner = pd.read_sql_query(q4_inner, conn)
    render_table_to_image(df4_inner, "Task 4.1: INNER JOIN (Employees & Departments)", "task4_inner_join.png")
    
    q4_left = """
    SELECT 
        e.employee_id,
        e.first_name || ' ' || e.last_name AS employee_name,
        e.job_title,
        COALESCE(d.department_name, 'Unassigned') AS department_name,
        COALESCE(d.location, 'N/A') AS location,
        e.salary
    FROM employees e
    LEFT JOIN departments d ON e.department_id = d.department_id
    ORDER BY e.employee_id DESC
    LIMIT 8;
    """
    df4_left = pd.read_sql_query(q4_left, conn)
    render_table_to_image(df4_left, "Task 4.2: LEFT JOIN (All Employees)", "task4_left_join.png")
    
    q4_right = """
    SELECT 
        d.department_id,
        d.department_name,
        d.location,
        d.budget,
        e.employee_id,
        COALESCE(e.first_name || ' ' || e.last_name, 'Vacant') AS employee_name,
        COALESCE(e.job_title, 'None') AS job_title
    FROM employees e
    RIGHT JOIN departments d ON e.department_id = d.department_id
    ORDER BY d.department_id DESC, e.employee_id
    LIMIT 8;
    """
    df4_right = pd.read_sql_query(q4_right, conn)
    render_table_to_image(df4_right, "Task 4.3: RIGHT JOIN (All Departments)", "task4_right_join.png")
    
    q5_1 = """
    SELECT 
        employee_id,
        first_name || ' ' || last_name AS employee_name,
        job_title,
        department_id,
        salary,
        ROUND((SELECT AVG(salary) FROM employees), 2) AS company_avg_salary,
        ROUND(salary - (SELECT AVG(salary) FROM employees), 2) AS diff_from_avg
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
    ORDER BY salary DESC;
    """
    df5_1 = pd.read_sql_query(q5_1, conn)
    render_table_to_image(df5_1, "Task 5.1: Employees Earning Above Company Average", "task5_subquery1.png")
    
    q5_2 = """
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
    ORDER BY e.salary DESC;
    """
    df5_2 = pd.read_sql_query(q5_2, conn)
    render_table_to_image(df5_2, "Task 5.2: Employees in San Francisco or New York", "task5_subquery2.png")
    
    conn.close()

if __name__ == "__main__":
    initialize_database()
    execute_all_queries()
    print("SQL tasks finished successfully.")
