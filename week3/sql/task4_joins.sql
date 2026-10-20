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
    COALESCE(d.location, 'Remote') AS location,
    e.salary
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
ORDER BY e.employee_id;

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
ORDER BY d.department_id, e.employee_id;
