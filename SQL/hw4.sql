USE 200424_OS;

SELECT * FROM Orders ORDER BY price DESC;

SELECT * FROM Customer WHERE e_mail LIKE '%@gmail.com';

SELECT *,
     CASE
         WHEN price < 50 THEN 'low'
         WHEN price >= 50 AND price < 100 THEN 'middle'
         ELSE 'high'
     END AS status
 FROM Orders;


SELECT client_id, COUNT(*) AS rating
FROM Orders
GROUP BY client_id
ORDER BY rating DESC;

SELECT * FROM Customer  WHERE city = 'Париж';

SELECT item_number, COUNT(*) AS total_orders
FROM Orders
GROUP BY item_number
ORDER BY total_orders DESC
LIMIT 1;

ALTER TABLE Orders
ADD COLUMN discount DECIMAL(5,2);

UPDATE Orders
SET discount = 
    CASE
        WHEN price>150 and price<200 THEN 50.00
        WHEN price>100 and price<150 THEN 25.00
        WHEN price>50 and price<100 THEN 10.00
        ELSE 0.00
    END;

SELECT *
FROM Orders
WHERE discount = (SELECT MAX(discount) FROM Orders);

SELECT *,
      ROUND(discount / (price / 100))  AS процент_скидки
FROM Orders;
