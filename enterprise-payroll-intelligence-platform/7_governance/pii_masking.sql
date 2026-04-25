-- Column-level masking for salary
SELECT 
  employee_id,
  department,
  CASE 
    WHEN current_role() IN ('HR','FINANCE') THEN salary
    ELSE NULL
  END AS salary_masked
FROM gold_payroll;