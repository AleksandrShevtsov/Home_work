USE 200424_OS;

DROP TABLE IF EXISTS Driver;
-- Таблица Driver
CREATE TABLE Driver (
    driver_id INT PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    license_number VARCHAR(15) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS Car;
-- Таблица Car
CREATE TABLE Car (
    car_id INT PRIMARY KEY,
    driver_id INT,
    license_plate VARCHAR(15) UNIQUE NOT NULL,
    model VARCHAR(15) NOT NULL,
    color VARCHAR(15) NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES Driver(driver_id)
);
DROP TABLE IF EXISTS Passenger;
-- Таблица Passenger
CREATE TABLE Passenger (
    passenger_id INT PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    phone VARCHAR(20) NOT NULL
);
DROP TABLE IF EXISTS Ride;
-- Таблица Ride
CREATE TABLE Ride (
    ride_id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    car_id INT,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    origin VARCHAR(255) NOT NULL,
    destination VARCHAR(255) NOT NULL,
    fare DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES Driver(driver_id),
    FOREIGN KEY (passenger_id) REFERENCES Passenger(passenger_id),
    FOREIGN KEY (car_id) REFERENCES Car(car_id)
);
DROP TABLE IF EXISTS Payment;
-- Таблица Payment
CREATE TABLE Payment (
    payment_id INT PRIMARY KEY,
    ride_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    payment_time DATETIME NOT NULL,
    payment_method VARCHAR(45) NOT NULL,
    FOREIGN KEY (ride_id) REFERENCES Ride(ride_id)
);




