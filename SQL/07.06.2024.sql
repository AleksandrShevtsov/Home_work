 -- Вывести список сервисных классов со средней стоимостью билета в каждом классе.
use airport;
select * from tickets;

select service_class, avg(price) as avg_price
from tickets
group by service_class;


select service_class, price, 
avg(price) over(partition by service_class)       as avg_price
from tickets;

-- Вывести список сервисных классов со средней ценой в каждой классе и ранком
-- каждого класса в зависимости от средней цены в сервисном классе

use airport;
select * from tickets;

select *, dense_rank() over(order by avg_ desc)
from
(select service_class, avg(price) as avg_
from tickets
group by service_class) t;




-- 8. Вывести топ 2 поездок (trips) по их средней стоимости. Поездка может состоять из
-- нескольких перелетов (поэтому на каждую поездку может приходиться больше
-- одного билета).
select * from tickets;


select trip_id, avg(price) as avg_
from tickets
group by trip_id
order by avg_ desc
limit 2; 





use shop;
SELECT 
  *, 
  ROW_NUMBER() OVER (partition by CUST_ID ORDER BY CUST_ID DESC) AS ROW_NUMBER_ID,
  RANK() OVER (partition by CUST_ID ORDER BY CUST_ID DESC) AS RANK_ID,
  DENSE_RANK() OVER (partition by CUST_ID ORDER BY CUST_ID DESC) AS DENSE_RANK_ID,
  NTILE(3) OVER (partition by CUST_ID ORDER BY CUST_ID DESC) AS NTILE_ID
FROM ORDERS;





use hr;
-- Вывести список region_id, total_countries, где total_countries - количество стран в таблице. 
select * from countries;

select distinct region_id, 
 count(country_name) OVER(partition by region_id) as total_countries
 from countries;
 

-- Работа с таблицей departments. Написать запрос, который выводит 
-- location_id, department_name, dept_total, где dept_total - количество департаментов в location_id.

select * from departments;

select location_id, department_name, 
count(department_name) over(partition by location_id) as dept_total
from departments;


--  вывести количество городов  в каждой стране для каждой страны. 
-- Результат должен содержать CountryCode, CityCount (количество городов в стране)

use world;
select * from city; 

select CountryCode,
max(row_n)
from
(select CountryCode, 
row_number() over(Partition by CountryCode) as row_n
from city) t
group by CountryCode;


-- 
select * from
(SELECT
  Name,
  LifeExpectancy,
  ROW_NUMBER() OVER (ORDER BY LifeExpectancy DESC) AS avg_life_exp
FROM country) t
WHERE avg_life_exp = 3;








