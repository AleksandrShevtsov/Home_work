use hr;

-- Запрос 1: Вывести список region_id, total_countries
SELECT 
    region_id,
    COUNT(country_id) OVER() AS total_countries
FROM 
    countries;
    
-- Запрос 2: Изменить запрос 1 для подсчета стран в каждом регионе
SELECT 
    region_id,
    COUNT(country_id) OVER(PARTITION BY region_id) AS total_countries
FROM 
    countries;
    
-- Запрос 3: Работа с таблицей departments. Вывести location_id, department_name, dept_total
SELECT 
    location_id,
    department_name,
    COUNT(department_id) OVER(PARTITION BY location_id) AS dept_total
FROM 
    departments;

-- Запрос 4: Изменить запрос 3 для вывода названий городов
-- Для этого запроса вам нужно присоединить таблицу locations для получения названий городов:
SELECT 
    d.location_id,
    l.city,
    d.department_name,
    COUNT(d.department_id) OVER(PARTITION BY d.location_id) AS dept_total
FROM 
    departments d
JOIN 
    locations l ON d.location_id = l.location_id;
    
-- Запрос 5: Работа с таблицей employees. Вывести manager_id, last_name, total_manager_salary

SELECT 
    manager_id,
    last_name,
    SUM(salary) OVER(PARTITION BY manager_id) AS total_manager_salary
FROM 
    employees
WHERE 
    manager_id IS NOT NULL;
    
SELECT manager_id, sum(salary)
FROM employees
GROUP BY manager_id;