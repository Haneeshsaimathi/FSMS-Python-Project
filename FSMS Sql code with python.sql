create database project;
use project;

create table Menu (name varchar(20), available_kg int, price int, original_price int);

insert into menu values('apple', 50,100,50),
('banana',60,40,20),
('mango',40,500,250),
('cherry',20,300,150),
('guava',30,90,45);

alter table menu add Profit bigint;
alter table menu modify profit bigint not null default 0; 
update menu set available_kg = 100;
select * from menu;




create table buyers(name varchar(20),apple int default 0, banana int default 0, mango int default 0, cherry int default 0, guava int default 0);
select * from buyers;

alter table buyers modify apple float default 0,
modify banana float default 0,
modify mango float default 0,
modify cherry float default 0,
modify guava float default 0;


alter table buyers add date varchar(20);
alter table buyers add phone bigint;


create table cart(fruit varchar(20), kgs_bought int, price int);
alter table cart modify kgs_bought float;

select * from cart;


create table total_profit (profit bigint);
alter table total_profit add over_all_profit bigint;
alter table total_profit modify profit varchar(20);
insert into total_profit(profit) values('profit');
alter table total_profit modify over_all_profit bigint not null;
select * from total_profit;




create table order_(items varchar(20), required_kgs int);
alter table order_ add order_date date, add delivery_date date;
alter table order_ add price bigint;
alter table order_ add name varchar(20), add mobile bigint;
select * from order_;



# without name priority to number
create table buyer(phone bigint,date varchar(20),apple float default 0, banana float default 0, mango float default 0, cherry float default 0, guava float default 0);
alter table buyer add coconut float default 0, add avacado float default 0 ,add seetaphal float default 0;
alter table buyer add sapota float default 0;
alter table buyer add grapes float default 0;
select * from buyer;



create table order___(mobile bigint,order_date date, delivery_date date, items varchar(20), required_kgs int, price bigint);
select * from order___;