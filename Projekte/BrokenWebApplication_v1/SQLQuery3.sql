CREATE PROC UserAdd
@Id int,
@username varchar(50),
@password varchar(10)
AS
INSERT INTO Users(username,password)
VALUES(@username,@password)