-- Задание 1
SELECT * FROM hr.employees;
-- Задание 2
SELECT salary FROM hr.employees;
-- Задание 3
SELECT  
IF (salary > 10000, '1', '0') AS SALARY_GROUP
FROM hr.employees;
-- Задание 4
-- Если значение salary больше 10000 
-- вывести в поле SLARY_GROUP значение 1 или 0
-- других нет запросов
-- SELECT пустой.jobs
-- Задание 5
SELECT first_name,
IF (salary > 10000, '1', '0') AS SALARY_GROUP
FROM hr.employees;
-- Задание 6
SELECT 
AVG(
CASE 
	WHEN department_id = 60 or department_id = 90 or department_id = 100 
    THEN salary 
    ELSE null END) as avg_dp60_90_100
FROM hr.employees;
-- Задание 7
SELECT first_name, last_name,
CASE 
	WHEN salary < 10000 THEN 'junior'
    WHEN salary < 15000 THEN  'mid' 
    ELSE 'senior' END as level
FROM hr.employees;
-- Задание 8
SELECT job_id,
CASE 
	WHEN max_salary > 10000 THEN 'high_payer'
    ELSE  'low_payer' END AS payer_rank
 FROM hr.jobs;
 -- Задание 9
 SELECT job_id,
 IF (max_salary > 10000, 'high_payer', 'low_payer') AS payer_rank
 FROM hr.jobs;
 -- Задание 10
 SELECT job_id, 
 IF (max_salary > 10000, 'high_payer', 'low_payer') AS payer_rank,
 max_salary
 FROM hr.jobs
 ORDER BY max_salary DESC;