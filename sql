DROP DATABASE food_delivery_db;
CREATE DATABASE food_delivery_db;
USE food_delivery_db;
CREATE TABLE food_orders (
    Order_ID VARCHAR(20) PRIMARY KEY,
    Customer_ID VARCHAR(20),
    Customer_Age INT,
    Customer_Gender VARCHAR(10),
    City VARCHAR(50),
    Restaurant_Name VARCHAR(100),
    Cuisine_Type VARCHAR(50),
    Order_Date DATE,
    Order_Time TIME,
    Order_Value FLOAT,
    Final_Amount FLOAT,
    Delivery_Time_Min INT,
    Distance_km FLOAT,
    Delivery_Rating FLOAT,
    Restaurant_Rating FLOAT,
    Discount_Applied FLOAT,
    Profit_Margin FLOAT,
    Payment_Mode VARCHAR(20),
    Order_Status VARCHAR(20),
    Cancellation_Reason VARCHAR(100),
    Order_Day VARCHAR(10),
    Peak_Hour BOOLEAN
);
SELECT Customer_ID, SUM(Final_Amount) AS total_spent
FROM food_orders
GROUP BY Customer_ID
ORDER BY total_spent DESC
LIMIT 10;
SELECT
CASE
    WHEN Customer_Age < 25 THEN 'Youth'
    WHEN Customer_Age BETWEEN 25 AND 40 THEN 'Adult'
    ELSE 'Senior'
END AS age_group,
AVG(Order_Value) AS avg_order_value
FROM food_orders
GROUP BY age_group;
SELECT Order_Day, COUNT(*) AS total_orders
FROM food_orders
GROUP BY Order_Day;
SELECT MONTH(Order_Date) AS month, SUM(Final_Amount) AS revenue
FROM food_orders
GROUP BY month;
SELECT
CASE WHEN Discount_Applied > 0 THEN 'Discounted' ELSE 'No Discount' END AS discount_type,
AVG(Profit_Margin) AS avg_profit_margin
FROM food_orders
GROUP BY discount_type;
SELECT City, SUM(Final_Amount) AS revenue
FROM food_orders
GROUP BY City
ORDER BY revenue DESC;
SELECT City, AVG(Delivery_Time_Min) AS avg_delivery_time
FROM food_orders
GROUP BY City;
SELECT Distance_km, Delivery_Time_Min
FROM food_orders;
SELECT Delivery_Time_Min, Delivery_Rating
FROM food_orders;
SELECT Restaurant_Name, AVG(Restaurant_Rating) AS avg_rating
FROM food_orders
GROUP BY Restaurant_Name
ORDER BY avg_rating DESC
LIMIT 10;
SELECT Restaurant_Name,
COUNT(CASE WHEN Order_Status='Cancelled' THEN 1 END) * 100.0 / COUNT(*) AS cancellation_rate
FROM food_orders
GROUP BY Restaurant_Name;
SELECT Cuisine_Type, COUNT(*) AS orders, SUM(Final_Amount) AS revenue
FROM food_orders
GROUP BY Cuisine_Type;
SELECT Peak_Hour, COUNT(*) AS total_orders
FROM food_orders
GROUP BY Peak_Hour;
SELECT Payment_Mode, COUNT(*) AS total_orders
FROM food_orders
GROUP BY Payment_Mode;
SELECT Cancellation_Reason, COUNT(*) AS total
FROM food_orders
WHERE Order_Status='Cancelled'
GROUP BY Cancellation_Reason;
ALTER TABLE food_orders ADD COLUMN Area VARCHAR(255);
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '4321';
FLUSH PRIVILEGES;
