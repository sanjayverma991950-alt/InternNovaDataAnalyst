SELECT 
    employee_id,
    first_name || ' ' || last_name AS employee_name,
    job_title,
    department_id,
    salary,
    ROUND((SELECT AVG(salary) FROM employees), 2) AS company_avg_salary,
    ROUND(salary - (SELECT AVG(salary) FROM employees), 2) AS salary_difference
FROM employees
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees
)
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

SELECT 
    e1.employee_id,
    e1.first_name || ' ' || e1.last_name AS employee_name,
    e1.department_id,
    e1.job_title,
    e1.salary,
    ROUND((
        SELECT AVG(e2.salary) 
        FROM employees e2 
        WHERE e2.department_id = e1.department_id
    ), 2) AS dept_avg_salary
FROM employees e1
WHERE e1.department_id IS NOT NULL
  AND e1.salary > (
      SELECT AVG(e2.salary)
      FROM employees e2
      WHERE e2.department_id = e1.department_id
  )
ORDER BY e1.department_id, e1.salary DESC;
