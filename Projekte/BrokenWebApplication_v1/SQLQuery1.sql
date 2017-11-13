CREATE PROCEDURE addUser
@userName nvarchar(50),
@pwd nvarchar(10)
as 
Begin
Insert into Users(username,password)
Values (@userName,@pwd)
End