CREATE DATABASE pizza;
USE pizza;

CREATE TABLE pizzas (
    pizza_id INT PRIMARY KEY,
    pizza_name VARCHAR(50),
    size ENUM('Small', 'Medium', 'Large', 'Extra Large'),
    crust_type VARCHAR(30),
    price DECIMAL(6,2),
    calories INT,
    category VARCHAR(20),
    is_vegetarian BOOLEAN
);

INSERT INTO pizzas VALUES
(1, 'Margherita', 'Medium', 'Thin Crust', 12.99, 280, 'Classic', TRUE),
(2, 'Pepperoni Supreme', 'Large', 'Hand Tossed', 18.99, 350, 'Meat', FALSE),
(3, 'Hawaiian Paradise', 'Medium', 'Stuffed Crust', 15.99, 320, 'Specialty', FALSE),
(4, 'Veggie Delight', 'Small', 'Thin Crust', 10.99, 220, 'Vegetarian', TRUE),
(5, 'Meat Lovers', 'Extra Large', 'Thick Crust', 22.99, 450, 'Meat', FALSE),
(6, 'BBQ Chicken', 'Large', 'Hand Tossed', 19.99, 380, 'Specialty', FALSE),
(7, 'Mushroom Magic', 'Medium', 'Thin Crust', 13.99, 260, 'Vegetarian', TRUE),
(8, 'Spicy Italian', 'Large', 'Stuffed Crust', 20.99, 400, 'Specialty', FALSE),
(9, 'Four Cheese', 'Small', 'Hand Tossed', 11.99, 310, 'Classic', TRUE),
(10, 'Buffalo Chicken', 'Medium', 'Thick Crust', 16.99, 340, 'Specialty', FALSE),
(11, 'Garden Fresh', 'Large', 'Thin Crust', 17.99, 290, 'Vegetarian', TRUE),
(12, 'Supreme Deluxe', 'Extra Large', 'Hand Tossed', 24.99, 420, 'Specialty', FALSE);


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    phone VARCHAR(15),
    email VARCHAR(60),
    city VARCHAR(30),
    join_date DATE,
    loyalty_points INT,
    status ENUM('Regular', 'VIP', 'Gold', 'Inactive')
);

INSERT INTO customers VALUES
(201, 'Tony', 'Soprano', '555-0101', 'tony.soprano@email.com', 'Newark', '2023-01-15', 450, 'VIP'),
(202, 'Maria', 'Rossi', '555-0102', 'maria.rossi@email.com', 'Brooklyn', '2023-02-20', 280, 'Regular'),
(203, 'Giuseppe', 'Bianchi', '555-0103', 'giuseppe.b@email.com', 'Manhattan', '2022-11-10', 750, 'Gold'),
(204, 'Isabella', 'Ferrari', '555-0104', 'isabella.f@email.com', 'Queens', '2023-03-05', 120, 'Regular'),
(205, 'Marco', 'Lombardi', '555-0105', 'marco.lombardi@email.com', 'Bronx', '2022-08-18', 890, 'Gold'),
(206, 'Sofia', 'Romano', '555-0106', 'sofia.romano@email.com', 'Brooklyn', '2023-04-12', 65, 'Regular'),
(207, 'Antonio', 'Conti', '555-0107', 'antonio.conti@email.com', 'Staten Island', '2022-12-03', 340, 'VIP'),
(208, 'Francesca', 'Moretti', '555-0108', 'francesca.m@email.com', 'Manhattan', '2023-01-28', 180, 'Regular'),
(209, 'Luca', 'Esposito', '555-0109', 'luca.esposito@email.com', 'Queens', '2022-09-15', 520, 'VIP'),
(210, 'Giulia', 'Ricci', '555-0110', 'giulia.ricci@email.com', 'Bronx', '2023-05-22', 15, 'Inactive');

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    delivery_time TIME,
    total_amount DECIMAL(8,2),
    delivery_type ENUM('Pickup', 'Delivery', 'Dine-in'),
    order_status ENUM('Pending', 'Preparing', 'Ready', 'Delivered', 'Cancelled'),
    special_instructions TEXT
);

INSERT INTO orders VALUES
(301, 201, '2024-01-15', '18:30:00', 45.97, 'Delivery', 'Delivered', 'Extra cheese on all pizzas'),
(302, 202, '2024-01-16', '12:15:00', 23.98, 'Pickup', 'Ready', 'No onions please'),
(303, 203, '2024-01-16', '19:45:00', 67.95, 'Dine-in', 'Delivered', NULL),
(304, 204, '2024-01-17', '20:00:00', 32.99, 'Delivery', 'Preparing', 'Call before delivery'),
(305, 205, '2024-01-17', '13:30:00', 18.99, 'Pickup', 'Ready', 'Extra spicy'),
(306, 206, '2024-01-18', '17:15:00', 28.98, 'Delivery', 'Delivered', NULL),
(307, 207, '2024-01-18', '19:00:00', 41.97, 'Dine-in', 'Cancelled', 'Table for 4'),
(308, 208, '2024-01-19', '14:45:00', 15.99, 'Pickup', 'Delivered', 'Light sauce'),
(309, 209, '2024-01-19', '21:30:00', 52.96, 'Delivery', 'Delivered', 'Ring doorbell twice'),
(310, 210, '2024-01-20', '16:20:00', 12.99, 'Pickup', 'Pending', NULL);


-- Q1. Write a query to display all information about pizzas.
select * from pizzas;

-- Q2. Display only the pizza_name, size, and price from the pizzas table.
select pizza_name, size, price from pizzas;

-- Q3. Show all customer information from the customers table.
select * from customers; 

-- Q4. Display only the first_name, last_name, and city of all customers.
select  first_name, last_name, city from customers;

-- Q5. Find all pizzas that are 'Large' size.
select * from pizzas where size = 'Large';

-- Q6. Display all customers from 'Brooklyn'.
select * from customers where city = 'Brooklyn';

-- Q7. Show all orders with total_amount greater than $40.
select * from orders where total_amount > 40.0;

-- Q8. Find all vegetarian pizzas (is_vegetarian = TRUE).
select * from pizzas where is_vegetarian = TRUE;

-- Q9. Display all customers with 'VIP' status
select * from customers where status = 'VIP';

-- .Q10. Show all orders placed on '2024-01-17'.
select * from orders where order_date = '2024-01-17';

-- Q11. Find all pizzas whose name starts with 'M'.
select * from pizzas where pizza_name like 'M%';

-- Q12. Display all customers whose first name ends with 'a'.
select * from customers where first_name like '%a';

-- Q13. Show all pizzas that contain the word 'Chicken' in their name.
select * from pizzas where pizza_name like '%Chicken%';

-- Q14. Find all customers whose email contains 'gmail' (Note: modify some emails if needed for practice).
select * from customers where email like '%gmail%';

-- Q15. Display all pizzas whose name contains 'Supreme'.
select * from pizzas where pizza_name like '%Supreme%';


-- Q16. Find all pizzas with price between $15 and $20.
select * from pizzas where price >= 15 and price <= 20;

-- Q17. Display customers with loyalty points greater than or equal to 500.
select * from customers where loyalty_points >= 500;

-- Q18. Show all pizzas with calories less than 300.
select * from pizzas where calories <= 300;

-- Q19. Find orders with total_amount less than or equal to $25
select * from orders where total_amount <= 25;

-- .Q20. Display all customers who joined before '2023-01-01'.
select * from customers where join_date < '2023-01-01';

-- Q21. Display pizzas ordered by calories in ascending order.
select * from pizzas order by calories asc;

-- Q22. Show customers ordered by city name alphabetically, then by last name.
select * from customers order by city, last_name;

-- Q23. Display orders ordered by order_date (newest first), then by total_amount (highest first).
select * from orders order by order_date desc, total_amount; 

-- Q24. Show the top 3 most expensive pizzas.
select * from pizzas order by price desc limit 3; 

-- Q25. Display the 5 customers with the most loyalty points.
select * from customers order by loyalty_points desc limit 5;

-- Q26. Show pizzas ranked 4-6 when ordered by price (use OFFSET).
select * from pizzas order by price desc limit 3 offset 3; 


