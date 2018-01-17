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

# insert some values in the database table vulnerableDB.sqlInjectionRanking
create table vulnerableDB.sqlInjectionRanking(userid int primary key auto_increment, username varchar(20), punkte int);
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('1', 'Daniel', '50');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('2', 'Werner', '77');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('3', 'Mr. Robot', '66');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('4', 'Bernd', '44');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('5', 'root', '42');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('6', 'admin', '97');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('7', 'Mr. Universe', '39');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('8', 'Kaaarl', '13');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('9', 'Denise', '17');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('10', 'Kevin', '0');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('11', 'pr0xy', '10');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('12', '4c1d', '29');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('13', '6r1ff1n', '6r1ff1n');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('14', 'n3m3515', '21');
insert into vulnerableDB.sqlInjectionRanking (userid, username, punkte) values ('15', 'Bu5yB34ver', '81');

# insert some values in the database table vulnerableDB.xssGuestbook
create table vulnerableDB.xssGuestbook(username varchar(20), datum date, kommentar varchar(255));
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('admin', '2017-11-15', 'Guten Tag! Es freut mich sehr, dass ich hiermit den ersten Beitrag in unserem Gästebuch erstellen darf und möchte dich herlich Willkommen heißen! :)');
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('admin', '2017-11-15', 'Was wohl mit diesem stored cross site scripting ales möglich ist');
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('admin', '2017-11-16', 'Wenn ich an Cookies denke, dann frage ich mich manchmal was dort drin steht.. manchmal hab ich auch einfach nur Lust auf einen Cookie :D');
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('Mr. Robot', '2017-11-18', '42');
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('root', '2017-11-20', 'Hello World!');
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('root', '2017-11-21', '1 + 1 = 0');
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('Mr. Robot', '2017-11-22', 'Knock, knock. Race condition. Who’s there.');
insert into vulnerableDB.xssGuestbook (username, datum, kommentar) values ('Mr. Robot', '2017-11-25', 'Why do Java programmers wear glasses? Because they don’t C#!');


# insert some values in the database table vulnerableDB.cookieManagementUsers
create table vulnerableDB.cookieManagementUsers(userid int primary key auto_increment, username varchar(255) not null, password varchar(255) not null);
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('1', 'admin', 'admin');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('2', 'user', 'hallo123');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('3', 'benutzer', 'passwort1');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('4', 'fußballfan', 'schalke04');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('5', 'test', 'test');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('6', 'master', 'master');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('7', 'system', 'system123');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('8', 'superuser', 'super');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('9', 'administrator', '11111');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('10', 'account' , 'abcd');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('11', 'benutzerkonto', 'benutzer');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('12', 'superman', '123456');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('13', 'mr.robot', 'hacker');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('14', 'biene', 'maja');
insert into vulnerableDB.cookieManagementUsers (userid, username, password) values ('15', 'test1', 'password');
