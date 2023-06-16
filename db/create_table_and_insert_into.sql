CREATE TABLE cars_and_bikes (
   sno INTEGER PRIMARY KEY,
   brand TEXT,
   model TEXT,
   year_of_manufacturing INTEGER,
   price REAL,
   car_or_bike TEXT
 );

INSERT INTO cars_and_bikes (sno,brand, model, year_of_manufacturing, price, car_or_bike) VALUES
('1', 'Reva', 'Electric', 2003, 400000, 'car'),
('2', 'Toyota', 'Corolla', 2017, 1400000, 'Car'),
('3', 'Yamaha', 'FZ', 2019, 120000, 'Bike'),
('4', 'Suzuki', 'Swift', 2016, 1000000, 'Car'),
('5', 'Honda', 'CBR', 2020, 250000, 'Bike'),
('6', 'Hyundai', 'i20', 2015, 900000, 'Car'),
('7', 'Bajaj', 'Pulsar', 2018, 80000, 'Bike'),
('8', 'Maruti', 'WagonR', 2019, 700000, 'Car'),
('9', 'Hero', 'Splendor', 2017, 60000, 'Bike'),
('10', 'Ford', 'EcoSport', 2017, 1100000, 'Car');

(base) ashish@ashish:~/Desktop/ws/gh/public/webDevelopmentCourseUsingFlask/db$ sqlite3
SQLite version 3.39.3 2022-09-05 11:02:23
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open mydb.db
sqlite> .tables
cars_and_bikes
sqlite> select * from cars_and_bikes;
1|reva|electric|2003|400000.0|car
2|Toyota|Corolla|2017|1400000.0|Car
3|Yamaha|FZ|2019|120000.0|Bike
4|Suzuki|Swift|2016|1000000.0|Car
5|Honda|CBR|2020|250000.0|Bike
6|Hyundai|i20|2015|900000.0|Car
7|Bajaj|Pulsar|2018|80000.0|Bike
8|Maruti|WagonR|2019|700000.0|Car
9|Hero|Splendor|2017|60000.0|Bike
10|Ford|EcoSport|2017|1100000.0|Car
sqlite> 


