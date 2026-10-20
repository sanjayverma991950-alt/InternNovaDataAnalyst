SELECT * 
FROM employees;

SELECT 
    employee_id, 
    first_name, 
    last_name, 
    job_title, 
    salary 
FROM employees;

SELECT 
    employee_id AS "Employee ID",
    first_name || ' ' || last_name AS "Full Name",
    job_title AS "Designation",
    department_id AS "Dept Code",
    '$' || printf('%,d', CAST(salary AS INT)) AS "Annual Compensation"
FROM employees;
