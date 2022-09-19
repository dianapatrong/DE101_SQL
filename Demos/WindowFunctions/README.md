```
create table employee (
employee_id int , 
full_name varchar,
department varchar, 
salary float
);

drop table employee; 


insert into employee (employee_id, full_name, department, salary) values 
(100, 'Mary Johns', 'SALES', 1000.00), 
(101, 'Sean Moldy', 'IT', 1500.00),
(102, 'Peter Dugan', 'SALES', 2000.00), 
(103,  'Lilian Penn', 'SALES', 1700.00), 
(104, 'Milton Kowarsky', 'IT', 1200.00), 
(105, 'Mareen Bisset', 'ACCOUNTS', 1200.00),
(106, 'Airton Graue', 'ACCOUNTS', 1000.00);

SELECT	
  employee_id,
  full_name,
  department,
  salary,
    RANK() OVER (ORDER BY salary DESC) AS dept_rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dept_dense_rank,
  ROW_NUMBER() OVER (ORDER BY salary DESC) AS dept_row_number
FROM employee;

```

```
SELECT	
  department,   
  sum(salary) OVER (PARTITION BY department ) AS dept_total_salary
FROM employee;
```