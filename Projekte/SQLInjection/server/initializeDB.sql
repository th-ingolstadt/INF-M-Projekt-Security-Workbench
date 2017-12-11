# create DB
drop database if exists vulnerableDB;
create database vulnerableDB;
grant select, insert, update, delete, alter, drop, create on vulnerableDB.* to "normal_user"@"localhost" identified by "master42";
create table vulnerableDB.secretUserData(userId int primary key auto_increment, userName varchar(255), password varchar(30));

# insert some values in the database table vulnerableDB.secretUserData
insert into vulnerableDB.secretUserData (userId, userName, password) values ('1', 'Douglas Adams', 'DontPanic!');
insert into vulnerableDB.secretUserData (userId, userName, password) values ('2', 'Harry Potter', 'CaputDraconis');
insert into vulnerableDB.secretUserData (userId, userName, password) values ('3', 'James T. Kirk', 'BeamMeUpScotty');
insert into vulnerableDB.secretUserData (userId, userName, password) values ('4', 'Grumpy Cat', 'No!');
insert into vulnerableDB.secretUserData (userId, userName, password) values ('5', 'Dalek', 'Exterminate!');
insert into vulnerableDB.secretUserData (userId, userName, password) values ('6', 'The Doctor', 'Allons-y');
insert into vulnerableDB.secretUserData (userId, userName, password) values ('7', 'Deadpool', 'Chimichanga');

create table vulnerableDB.sqlInjectionRanking(userid int primary key auto_increment, user varchar(20), punkte int);

insert into vulnerableDB.sqlInjectionRanking (userid, user, punkte) values ('1', 'Daniel', '50');
insert into vulnerableDB.sqlInjectionRanking (userid, user, punkte) values ('2', 'Werner', '77');
insert into vulnerableDB.sqlInjectionRanking (userid, user, punkte) values ('3', 'Mr. Robot', '66');
insert into vulnerableDB.sqlInjectionRanking (userid, user, punkte) values ('4', 'Bernd', '44');
insert into vulnerableDB.sqlInjectionRanking (userid, user, punkte) values ('5', 'root', '42');
insert into vulnerableDB.sqlInjectionRanking (userid, user, punkte) values ('6', 'admin', '97');
