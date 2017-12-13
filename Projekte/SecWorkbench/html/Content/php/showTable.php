<!DOCTYPE html>
<html>
<head>
	<style>
	table.visible *{
	border: 1px solid black;
	padding: 5px;
	min-width: 100px;
	}
	</style>
</head>
<body>

<?php

$con = mysqli_connect('localhost','normal_user','master42','vulnerableDB');
$query = 'DESCRIBE secretUserData;';

if (!$con) {
	echo "<p>error</p>";
    die('Could not connect: ' . mysqli_error($con));
}

$results = mysqli_query($con, $query) or die('Datenbank existiert nicht');


echo "<table class='visible'>
	<tr>
	<th>Column Name</th>
	<th>Data Type</th>
	<th>Null</th>
	<th>Key</th>
	<th>Default</th>
	<th>Extra</th>
	</tr>";
	while($row = mysqli_fetch_array($results)){
	  if($row['Default']==""){$row['Default']="NULL";}
	  echo "<tr><td>" . $row['Field'] . "</td><td>" . $row['Type'] . "</td><td>" . $row['Null'] . "</td><td>" . $row['Key'] . "</td><td>" . $row['Default'] . "</td><td>" . $row['Extra'] . "</td></tr>";
	}
echo "</table>";

mysqli_close($con);


?>

</body>
</html>
