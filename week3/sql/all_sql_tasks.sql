DROP TABLE IF EXISTS sales_records;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL,
    location TEXT NOT NULL,
    budget REAL NOT NULL
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    department_id INTEGER,
    job_title TEXT NOT NULL,
    salary REAL NOT NULL,
    hire_date TEXT NOT NULL,
    performance_score INTEGER CHECK (performance_score BETWEEN 1 AND 5),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE sales_records (
    sale_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    client_name TEXT NOT NULL,
    sale_amount REAL NOT NULL,
    sale_date TEXT NOT NULL,
    region TEXT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO departments (department_id, department_name, location, budget) VALUES
(101, 'Engineering', 'San Francisco', 1250000.00),
(102, 'Data Analytics', 'New York', 950000.00),
(103, 'Marketing', 'Chicago', 600000.00),
(104, 'Sales', 'Austin', 800000.00),
(105, 'Human Resources', 'Boston', 450000.00),
(106, 'Research & Development', 'Seattle', 1100000.00);

INSERT INTO employees (employee_id, first_name, last_name, email, department_id, job_title, salary, hire_date, performance_score) VALUES
(1001, 'Sarah', 'Connor', 'sarah.c@techvanguard.com', 101, 'Lead Data Engineer', 98000.00, '2021-03-15', 5),
(1002, 'Michael', 'Chen', 'michael.c@techvanguard.com', 101, 'Senior Software Engineer', 92000.00, '2020-07-11', 4),
(1003, 'Emily', 'Watson', 'emily.w@techvanguard.com', 102, 'Senior Data Analyst', 85000.00, '2021-09-01', 5),
(1004, 'David', 'Kim', 'david.k@techvanguard.com', 102, 'BI Developer', 74000.00, '2022-01-10', 4),
(1005, 'Jessica', 'Alba', 'jessica.a@techvanguard.com', 103, 'Digital Marketing Manager', 71000.00, '2019-11-20', 3),
(1006, 'James', 'Wilson', 'james.w@techvanguard.com', 104, 'Enterprise Account Exec', 88000.00, '2020-02-14', 4),
(1007, 'Robert', 'Taylor', 'robert.t@techvanguard.com', 104, 'Sales Specialist', 62000.00, '2022-05-18', 3),
(1008, 'Amanda', 'Martinez', 'amanda.m@techvanguard.com', 105, 'HR Business Partner', 67000.00, '2021-08-05', 4),
(1009, 'Brian', 'O''Connor', 'brian.o@techvanguard.com', 101, 'DevOps Engineer', 89000.00, '2021-12-01', 4),
(1010, 'Lisa', 'Ray', 'lisa.r@techvanguard.com', 102, 'Junior Data Analyst', 58000.00, '2023-04-12', 3),
(1011, 'Kevin', 'Patel', 'kevin.p@techvanguard.com', 103, 'Content Strategist', 56000.00, '2023-02-01', 3),
(1012, 'Rachel', 'Green', 'rachel.g@techvanguard.com', 104, 'Inside Sales Rep', 54000.00, '2023-06-15', 2),
(1013, 'Daniel', 'Craig', 'daniel.c@techvanguard.com', 105, 'Recruiting Coordinator', 52000.00, '2023-08-20', 3),
(1014, 'Sophia', 'Loren', 'sophia.l@techvanguard.com', 101, 'Frontend Engineer', 81000.00, '2022-10-01', 4),
(1015, 'Alexander', 'Vance', 'alex.vance@techvanguard.com', NULL, 'Strategic Advisor', 115000.00, '2024-01-05', 5);

INSERT INTO sales_records (sale_id, employee_id, client_name, sale_amount, sale_date, region) VALUES
(501, 1006, 'Acme Corp', 45000.00, '2024-01-15', 'North America'),
(502, 1006, 'Globex Logistics', 32000.00, '2024-02-10', 'North America'),
(503, 1007, 'Initech Systems', 18500.00, '2024-02-22', 'Europe'),
(504, 1012, 'Umbrella Health', 12000.00, '2024-03-05', 'Latin America'),
(505, 1006, 'Soylent Foods', 29000.00, '2024-03-18', 'North America'),
(506, 1007, 'Hooli Networks', 24500.00, '2024-04-02', 'Asia-Pacific');

SELECT * FROM employees;

SELECT employee_id, first_name, last_name, job_title, salary FROM employees;

SELECT 
    employee_id AS "Employee ID",
    first_name || ' ' || last_name AS "Full Name",
    job_title AS "Designation",
    salary AS "Annual Salary (USD)"
FROM employees;

SELECT employee_id, first_name, last_name, job_title, department_id, salary
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
FROM employees;

SELECT 
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
ORDER BY avg_salary DESC;

SELECT 
    e.employee_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.job_title,
    d.department_name,
    d.location,
    e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
ORDER BY e.employee_id;

SELECT 
    e.employee_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.job_title,
    COALESCE(d.department_name, 'Unassigned') AS department_name,
    COALESCE(d.location, 'N/A') AS location,
    e.salary
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
ORDER BY e.employee_id;

SELECT 
    d.department_id,
    d.department_name,
    d.location,
    e.employee_id,
    COALESCE(e.first_name || ' ' || e.last_name, 'Vacant') AS employee_name,
    COALESCE(e.job_title, 'None') AS job_title
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id
ORDER BY d.department_id, e.employee_id;

SELECT 
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
ORDER BY e.salary DESC;
