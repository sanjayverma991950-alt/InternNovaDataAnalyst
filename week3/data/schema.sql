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
