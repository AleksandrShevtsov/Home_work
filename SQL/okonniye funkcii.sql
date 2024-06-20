use hr;
select * from employees;

select job_id, avg(salary) as avg_
from employees
where salary > 3000  -- фильтрация до группировки
group by job_id
having avg_ > 5000; -- фильтрация после группировки




use shop;

select * from ORDERS;


SELECT   ORDER_ID,   ODATE,  AMT,
  SUM(AMT) OVER() AS running_total 
FROM ORDERS;




SELECT   SELL_ID, ORDER_ID,   ODATE,  AMT,
  SUM(AMT) OVER(PARTITION BY SELL_ID) AS running_total ,
   SUM(AMT) OVER() AS total_ 
FROM ORDERS;



-- Вывести средний рейтинг клиентов по городам: для каждого города вывести средний рейтинг клиентов.
SELECT * FROM shop.CUSTOMERS;

SELECT *, 
AVG(RATING) OVER(partition by CITY) avg_rating,
AVG(RATING) OVER() avg_rating_total
from CUSTOMERS
;


-- Вывести информацию о каждом заказе и максимальную сумму заказа в том же месяце для каждой строки.
SELECT * FROM shop.ORDERS;

select *,
MAX(AMT) OVER(PARTITION BY month(odate)) as max_amt
from ORDERS;


-- Для более полного понимания практической значимости прошлого запроса, 
-- добавим подсчет относительного вклада каждого заказа в общий объем продаж месяца.

select *,
SUM(AMT) OVER(PARTITION BY month(odate)) as total_amt,
round(AMT/SUM(AMT) OVER(PARTITION BY month(odate)) * 100, 2) as percent
from ORDERS;



-- Вывести список продавцов с указанием общей суммы их продаж. 
-- Отсортировать продавцов по убыванию суммы продаж.

SELECT * FROM shop.ORDERS;


SELECT *,
IF(SUM(AMT) OVER(PARTITION BY SELL_ID) is NULL, 0, SUM(AMT) OVER(PARTITION BY SELL_ID))
as total_sales
from ORDERS
ORDER BY total_sales DESC;


-- Вывести топ-2 продавцов с самой высокой средней суммой заказа. 

SELECT  DISTINCT SELL_ID, 
AVG(AMT) OVER(PARTITION BY SELL_ID) as avg_
from ORDERS
ORDER BY avg_ desc
LIMIT 2;



SELECT   DISTINCT SELLERS.SELL_ID,   SNAME,

  AVG(AMT) OVER (PARTITION BY SELLERS.SELL_ID) AS AVG_ORDER_AMOUNT
  
FROM SELLERS
LEFT JOIN ORDERS 
ON ORDERS.SELL_ID = SELLERS.SELL_ID
ORDER BY AVG_ORDER_AMOUNT DESC
LIMIT 2;


use shop;

SELECT *, 
row_number() OVER(partition by SELL_ID order by odate) AS number_
FROM ORDERS
;



SELECT *, 
row_number() OVER() AS number_
FROM ORDERS
;





SELECT *, 
rank() OVER(order by SELL_ID) AS number_ -- дает ранг, 1, 1, 3, 3, 3, 6, 6, 8
FROM ORDERS;


SET profiling = 1;
SELECT *, 
row_number() OVER() AS number_
FROM ORDERS;

SHOW PROFILES;



SET profiling = 1;
SELECT count(*)
FROM ORDERS;

SHOW PROFILES;


select *, 
dense_rank() OVER(order by SELL_ID) AS number_
from ORDERS;

select *,
NTILE(3) OVER (order by odate)
from ORDERS;


SELECT 
  *, 
  ROW_NUMBER() OVER (ORDER BY CUST_ID DESC) AS ROW_NUMBER_ID,
  RANK() OVER (ORDER BY CUST_ID DESC) AS RANK_ID,
  DENSE_RANK() OVER (ORDER BY CUST_ID DESC) AS DENSE_RANK_ID,
  NTILE(3) OVER (ORDER BY CUST_ID DESC) AS NTILE_ID
FROM ORDERS;



-- произведите ранжирование департаментов по средней зарплате.
select * from hr.employees;



use hr;
select department_id, avg(salary) as avg_,
dense_rank() over(order by avg(salary) desc) as rank_
from employees
group by department_id;


-- Выведите топ-3 сотрудников с наивысшей зарплатой в каждом департаменте.

select department_id, salary, rank_
from 
(select *,
dense_rank() over(partition by department_id order by salary desc) as rank_
from employees) t1
where rank_ <= 3;



-- Выведите второго по зарплате сотрудника в каждом департаменте.
select distinct department_id, salary, rank_
from 
(select *,
dense_rank() over(partition by department_id order by salary desc) as rank_
from employees) t1
where rank_ = 2;


-- Получить информацию о зарплате сотрудников, а также рассчитать кумулятивную и 
-- относительную кумулятивную сумму зарплаты для каждого сотрудника в пределах своего департамента.


Select employee_id, first_name, salary, department_id,
sum(salary) over(partition by department_id order by employee_id) as kum_in_group,
sum(salary) over(order by employee_id) total_kum_sum
from employees;
















