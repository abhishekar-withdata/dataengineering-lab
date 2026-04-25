-- Payroll Aggregation Query

SELECT 
    department,
    COUNT(employee_id) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS avg_salary,
    SUM(overtime_hours) AS total_overtime
FROM gold_payroll
GROUP BY department;
