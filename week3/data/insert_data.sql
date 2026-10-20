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
