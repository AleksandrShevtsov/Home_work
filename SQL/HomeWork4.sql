DROP DATABASE IF EXISTS 200424_OS;

CREATE DATABASE 200424_OS; 

USE 200424_OS;

DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer (
    id SERIAL,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    streer VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(40),
    e_mail VARCHAR(40) NOT NULL,
    registration_day DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders(
    id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT,
    creat_order_day DATE,
    item_number INT,
    product_description TEXT,
    price FLOAT,
    photo_link VARCHAR(100)
);

INSERT INTO Customer (first_name, last_name, streer, city, country, e_mail) VALUE
	('Александр', 'Иванов', '10 Downing Street', 'Лондон', 'Англия', 'ivanov@gmail.com'),
	('Николай', 'Петров', '221B Baker Street', 'Лондон', 'Англия', 'petrov@gmail.com'),
	('Иван', 'Соколов', '5 Rue de Rivoli', 'Париж', 'Франция', 'sokol@mail.ru'),
	('Ольга', 'Быстрова', '30 Rockefeller Plaza', 'Нью-Йорк', 'США', 'bistrova@mail.ru'),
	('Александр', 'Иванов', '10 Downing Street', 'Лондон', 'Англия', 'ivanov@gmail.com'),
	('Николай', 'Петров', '221B Baker Street', 'Лондон', 'Англия', 'petrov@gmail.com'),
	('Остап', 'Бандера', 'ул. Мести, 1', 'Киев', 'Украина', 'OsBand@mail.ru'),
	('Иван', 'Соколов', '5 Rue de Rivoli', 'Париж', 'Франция', 'sokol@mail.ru'),
	('Ольга', 'Быстрова', '30 Rockefeller Plaza', 'Нью-Йорк', 'США', 'bistrova@mail.ru'),
	('Иван', 'Тихонов', '42nd Street & 7th Avenue', 'Нью-Йорк', 'США', 'tih_iv@bk.com'),
	('Анна', 'Тихонова', '42nd Street & 7th Avenue', 'Нью-Йорк', 'США', 'tih_ann@gmail.com'),
	('Игорь', 'Карай', '1 Macquarie Street', 'Сидней', 'Австралия', 'karai@bk.com'),
	('Дмитрий', 'Конов', 'ул. Пушкина, 2', 'Севастополь', 'Украина', 'kn@mail.ru'),
	('Ирина', 'Конова', 'ул. Пушкина, 2', 'Севастополь', 'Украина', 'irina_kn@mail.ru');
    
INSERT INTO Orders (client_id, creat_order_day, item_number, product_description, price, photo_link)
  VALUES
	(5, '2024-05-14', 101, 'Wireless Headphones', 99.99, 'http://example.com/wireless_headphones.jpg'),
	(10, '2024-05-14', 102, 'Smartphone Case', 19.99, 'http://example.com/smartphone_case.jpg'),
	(7, '2024-05-14', 103, 'Coffee Maker', 49.99, 'http://example.com/coffee_maker.jpg'),
	(3, '2024-05-14', 104, 'Bluetooth Speaker', 79.99, 'http://example.com/bluetooth_speaker.jpg'),
	(13, '2024-05-14', 105, 'Digital Camera', 299.99, 'http://example.com/digital_camera.jpg'),
	(8, '2024-05-14', 106, 'Fitness Tracker', 89.99, 'http://example.com/fitness_tracker.jpg'),
	(6, '2024-05-14', 107, 'Gaming Mouse', 59.99, 'http://example.com/gaming_mouse.jpg'),
	(1, '2024-05-14', 108, 'Laptop Backpack', 39.99, 'http://example.com/laptop_backpack.jpg'),
	(4, '2024-05-14', 109, 'Wireless Keyboard', 69.99, 'http://example.com/wireless_keyboard.jpg'),
	(9, '2024-05-14', 110, 'Portable Charger', 29.99, 'http://example.com/portable_charger.jpg'),
	(11, '2024-05-14', 111, 'External Hard Drive', 129.99, 'http://example.com/external_hard_drive.jpg'),
	(2, '2024-05-14', 112, 'Tablet Stand', 24.99, 'http://example.com/tablet_stand.jpg'),
	(14, '2024-05-14', 113, 'Smartwatch', 199.99, 'http://example.com/smartwatch.jpg'),
	(12, '2024-05-14', 114, 'Wireless Earbuds', 149.99, 'http://example.com/wireless_earbuds.jpg'),
	(11, '2024-05-14', 115, 'USB-C Cable', 9.99, 'http://example.com/usb_cable.jpg'),
    (2, '2024-05-14', 101, 'Wireless Headphones', 99.99, 'http://example.com/wireless_headphones.jpg'),
	(13, '2024-05-14', 102, 'Smartphone Case', 19.99, 'http://example.com/smartphone_case.jpg'),
	(7, '2024-05-14', 103, 'Coffee Maker', 49.99, 'http://example.com/coffee_maker.jpg'),
	(3, '2024-05-14', 104, 'Bluetooth Speaker', 79.99, 'http://example.com/bluetooth_speaker.jpg'),
	(13, '2024-05-14', 105, 'Digital Camera', 299.99, 'http://example.com/digital_camera.jpg'),
	(8, '2024-05-14', 106, 'Fitness Tracker', 89.99, 'http://example.com/fitness_tracker.jpg'),
	(11, '2024-05-14', 107, 'Gaming Mouse', 59.99, 'http://example.com/gaming_mouse.jpg'),
	(1, '2024-05-14', 108, 'Laptop Backpack', 39.99, 'http://example.com/laptop_backpack.jpg'),
	(4, '2024-05-14', 109, 'Wireless Keyboard', 69.99, 'http://example.com/wireless_keyboard.jpg'),
	(9, '2024-05-14', 110, 'Portable Charger', 29.99, 'http://example.com/portable_charger.jpg'),
	(11, '2024-05-14', 111, 'External Hard Drive', 129.99, 'http://example.com/external_hard_drive.jpg'),
	(2, '2024-05-14', 112, 'Tablet Stand', 24.99, 'http://example.com/tablet_stand.jpg'),
	(14, '2024-05-14', 113, 'Smartwatch', 199.99, 'http://example.com/smartwatch.jpg'),
	(11, '2024-05-14', 114, 'Wireless Earbuds', 149.99, 'http://example.com/wireless_earbuds.jpg'),
	(14, '2024-05-14', 115, 'USB-C Cable', 9.99, 'http://example.com/usb_cable.jpg'),
    (3, '2024-05-14', 104, 'Bluetooth Speaker', 79.99, 'http://example.com/bluetooth_speaker.jpg'),
	(13, '2024-05-14', 105, 'Digital Camera', 299.99, 'http://example.com/digital_camera.jpg'),
	(8, '2024-05-14', 106, 'Fitness Tracker', 89.99, 'http://example.com/fitness_tracker.jpg'),
	(6, '2024-05-14', 107, 'Gaming Mouse', 59.99, 'http://example.com/gaming_mouse.jpg'),
	(1, '2024-05-14', 108, 'Laptop Backpack', 39.99, 'http://example.com/laptop_backpack.jpg'),
	(2, '2024-05-14', 112, 'Tablet Stand', 24.99, 'http://example.com/tablet_stand.jpg'),
	(14, '2024-05-14', 113, 'Smartwatch', 199.99, 'http://example.com/smartwatch.jpg'),
	(12, '2024-05-14', 114, 'Wireless Earbuds', 149.99, 'http://example.com/wireless_earbuds.jpg'),
	(11, '2024-05-14', 115, 'USB-C Cable', 9.99, 'http://example.com/usb_cable.jpg');


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




