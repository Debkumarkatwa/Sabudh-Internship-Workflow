Create database CompanyDB;

Create schema HR;

Create schema Accounting;
Create schema Inventory;

use CompanyDB;

create table HR_Emplooyes(
Emp_ID INT auto_increment primary key,
First_Name varchar(50) Not null,
Last_Name varchar(50) Not Null,
Hire_Date date not null default (current_date),
Position Varchar(20) Not null default 'Employee',
Salary decimal(10,2) not null default 0.00
);

create table Accounting_Client(
Client_ID int auto_increment primary key,
Client_Name varchar(80) Not NUll
);

create table accounting_Invoices(
Invoice_ID int auto_increment primary key,
Client_ID int,
Amount decimal(10,2) not null check (Amount > 0),
Status varchar(20) default 'Pending',
Issuse_Date date Not null,
Due_Date date not null,

foreign key (Client_ID) references Accounting_Client(Client_ID)
);

create table Inventory_Product(
Product_ID int auto_increment primary key,
Product_Name varchar(40) Not null,
Category varchar(20) not null,
Price decimal(10,2) not null,
Added_Date timestamp default current_timestamp,

check (Price > 0)
);

create table Departments(
Dept_ID int auto_increment primary key,
Dept_Name varchar(50) unique Not null
);

create table customer(
Customer_ID int auto_increment primary key,
Name varchar(50) not null
);

create table orders(
Order_ID int auto_increment primary key,
Customer_ID int,
Order_Date date default (current_date),

foreign key (Customer_ID) references customer(Customer_ID)
on delete cascade
on update restrict
);

create table Users(
User_ID int auto_increment primary key,
user_Name varchar(50) not null,
Email varchar(100) unique not null
);

create table Product_With_Discount(
Product_ID int auto_increment primary key,
product_Name varchar(50) not null,
price decimal(10,2) not null,
discount_Price decimal(10,2) not null,
check (discount_Price < price)
);

update HR_Emplooyes set First_Name = 'Unknown' where First_Name = null;
update HR_Emplooyes set Last_Name = 'Unknown' where Last_Name = null;

alter table HR_Emplooyes 
modify column First_Name varchar(50) not null;

create table registration(
Regs_ID int auto_increment primary key,
user_ID int,
regs_Date date default current_timestamp,
status varchar(10) default 'Active'
);

alter table HR_Emplooyes 
add column Email varchar(100) Null;

alter table HR_Emplooyes 
modify column Salary decimal(50,2) not null default 0.00;

alter table HR_Emplooyes 
add column Middle_Name varchar(10) after First_name;

alter table HR_Emplooyes 
drop column Middle_Name;

create index IDX_Last_Name on HR_Emplooyes(Last_name);

alter table HR_Emplooyes
add column Dept_ID int;

create view Employee_Public as select Emp_ID, First_name, Last_name, Dept_ID from HR_Emplooyes;

-- drop table 'Table Name'; 

