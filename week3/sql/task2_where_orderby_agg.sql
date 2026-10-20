SELECT 
    employee_id,
    first_name,
    last_name,
    job_title,
    department_id,
    salary
FROM employees
WHERE department_id = 101 
  AND salary >= 85000.00;

SELECT 
    employee_id,
    first_name || ' ' || last_name AS employee_name,
    job_title,
    salary
FROM employees
ORDER BY salary DESC;

SELECT 
    employee_id,
    first_name || ' ' || last_name AS employee_name,
    department_id,
    job_title,
    salary
FROM employees
WHERE department_id IS NOT NULL
ORDER BY department_id ASC, salary DESC;

SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_payroll_expense,
    ROUND(AVG(salary), 2) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees;
