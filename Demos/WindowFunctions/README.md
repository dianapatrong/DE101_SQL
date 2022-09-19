```
create table employee (
employee_id int primary key, 
full_name varchar,
department varchar, 
salary float
);


insert into employee (employee_id, full_name, department, salary) values 
(100, 'Mary Johns', 'SALES', 1000.00), 
(101, 'Sean Moldy', 'IT', 1500.00),
(102, 'Peter Dugan', 'SALES', 2000.00), 
(103,  'Lilian Penn', 'SALES', 1700.00), 
(104, 'Milton Kowarsky', 'IT', 1800.00), 
(105, 'Mareen Bisset', 'ACCOUNTS', 1200.00),
(106, 'Airton Graue', 'ACCOUNTS', 1100.00);

```


To obtain the rank salary for each department:
```
SELECT	
  employee_id,
  full_name,
  department,
  salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_dense_rank,
  ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_row_number
FROM employee;
```

Think about how to change the query if you want the same report but with all number 1 ranking employees first,
 then all number 2 employees, and so on. This change is left to the reader as practice.

Another interesting example is a query to obtain a metric for every employee about how close they are from the top salary 
of their department.

```
SELECT 
   employee_id,
   full_name,
   department,
   salary,
   salary/MAX(salary) OVER (PARTITION BY department ORDER BY salary DESC)
			AS salary_metric
FROM employee;
```