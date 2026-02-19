-- cross join
use as2;

select * from cinema c
cross join employees e
order by id, emp_id;

-- self join

-- print their manager's first & last names beside each employee's first & last name
use hr;
select employees.employee_id, employees.first_name, employees.last_name, 
employees.manager_id, managers.employee_id, managers.first_name, managers.last_name
from employees
left join employees as managers
on employees.manager_id = managers.employee_id;

select employee_id as id, first_name, last_name, manager_id
from employees;

-- Display employee name of the employees who do not have a manager.

/*
Display employee_id, first_name, last_name, employee's salary, manager_id, manager's first_name, manager's last_name and manager's salary for all the employees
(including those who do not have a manager)
*/

use hr2;
-- Display employees who earn more salary than their manager.
select e1.employee_id, e1.first_name, e1.last_name, e1.salary, e1.manager_id, e2.first_name as manager_first_name, e2.last_name as manager_last_name, 
e2.salary as manager_salary
from employees e1
left join employees e2
on e1.manager_id = e2.employee_id
where e1.salary > e2.salary;

-- Display employees who were hired after their manager.
select e1.employee_id, e1.first_name, e1.last_name, e1.hire_date, e1.manager_id, e2.first_name as manager_first_name, e2.last_name as manager_last_name, 
e2.hire_date as manager_hire_date
from employees e1
left join employees e2
on e1.manager_id = e2.employee_id 
where e1.hire_date > e2.hire_date;
-- OR
select e1.employee_id, e1.first_name, e1.last_name, e1.hire_date, e1.manager_id, e2.first_name as manager_first_name, e2.last_name as manager_last_name, 
e2.hire_date as manager_hire_date
from employees e1
join employees e2
on e1.manager_id = e2.employee_id and e1.hire_date > e2.hire_date;


-- Display managers and the total number of employees reporting to each manager.
select e1.manager_id, 
count(e1.first_name)
-- e2.first_name as manager_first_name, e2.last_name as manager_last_name, 
-- count(e1.employee_id)
from employees e1
left join employees e2
on e1.manager_id = e2.employee_id
group by e1.manager_id;

-- Print each manager's employee_id, their first_name and employee's first name who is working under that manager. Sort your result in ascending order of manager_id.
select m.employee_id as manager_id, m.first_name, 
count(e.employee_id) as no_of_employees
from employees e
left join employees m
on e.manager_id = m.employee_id
group by m.employee_id, m.first_name;


select emp.manager_id, man.first_name as "Manager Fname", man.last_name "Manager Lname", Count(emp.employee_id) total_emp
from employees emp
left join employees man 
on emp.manager_id = man.employee_id
group by emp.manager_id
order by emp.manager_id;

-- Display managers whose average reporting employee salary is greater than 8000.


-- Display managers who have at least one reporting employee earning more than 10000, and show the highest salary among their reporting employees.


-- Subquery
-- Print employees who are earning above average salary
select *
from employees
where salary > (select avg(salary) from employees);

-- Print average salary of all the employees besied first_name, last_name and salary columns.
select first_name, last_name, salary, e.avg_salary
from employees
cross join (
	select avg(salary) avg_salary from employees
) as e;

select first_name, last_name, salary, (select avg(salary) from employees) as avg_salary
from employees;

-- Display employees who earn more than the employee with employee_id = 101.
select *
from employees 
where salary > (select salary from employees where employee_id=101);

-- Display employees who work in the same department as the employee with employee_id = 102
select *
from employees 
where department_id = (select department_id from employees where employee_id=101);

-- Display employees who are working in departments located in the city 'London'.
select employee_id, first_name, last_name, l.city
from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id
where l.city = "London";