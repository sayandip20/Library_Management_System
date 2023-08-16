create database library;

use library;

create table book(
bno int primary key, 
bname varchar(50), 
author varchar(50) , 
price float, 
copy int);

create table member(
id int primary key, 
Name varchar(50),
join_Date date , 
mob varchar(20));

create table Register(
is_no int primary key, 
bno int,
id int,
issue_Date date,
dew_date date,
return_date date);