<!DOCTYPE html>
<html>
<head>
	<style>
	/*table, tr, th, td{*/

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
if (!$con) {
	echo "<p>error</p>";
    die('Could not connect: ' . mysqli_error($con));
}

$query = 'SELECT * FROM secretUserData;';

$userdata_selected = false;

$result = mysqli_query($con, $query);

if ($result->num_rows > 0) {
	if($userdata_selected == false){
		echo "<table class='visible'>
			<tr>
			<th>ID</th>
			<th>Name</th>
			<th>Password</th>
			</tr>";
		$userdata_selected = true;
	}
    	while($row = $result->fetch_assoc()) {
		echo "<tr>";
		echo "<td>" . $row['userId'] . "</td>";
		echo "<td>" . $row['userName'] . "</td>";
		echo "<td>" . $row['password'] . "</td>";
		echo "</tr>";
	}
echo "</table>";
} else {
    echo "<p style='color: red'>Keine User oder Datenbank vorhanden</p>";
}
$con->close();


?>

</body>
</html>
