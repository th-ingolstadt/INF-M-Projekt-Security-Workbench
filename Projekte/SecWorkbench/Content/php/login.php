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

#read parameters from index.html
$username = $_GET['username'];
$password = $_GET['password'];   

$con = mysqli_connect('localhost','normal_user','master42','vulnerableDB');
if (!$con) {
	echo "<p>error</p>";
    die('Could not connect: ' . mysqli_error($con));
}

$query = 'SELECT * FROM secretUserData WHERE userName = "'.$username.'" AND password = "'.$password.'";';

echo "<p style='color:orange'>Folgende Query wurde gebildet:<br>".$query."</p>";

$userdata_selected = false;
if ($con->multi_query($query)) {
    do {
        /* store first result set */
	
        if ($result = $con->store_result()) {
		if (mysqli_num_rows($result)==0) {
			echo "<p style='color: red'>Kein User mit Namen <b>".$username."</b> und Passwort <b>".$password."</b> vorhanden</p>";
			break;
		}
		if($userdata_selected == false){
			echo "<p>------------------------------------------------------------------------<br>
				Login successful with user:<p>
				<table class='visible'>
				<tr>
				<th>ID</th>
				<th>Name</th>
				<th>Password</th>
				</tr>";
			$userdata_selected = true;
		}
	    	while ($row = $result->fetch_row()) {
			echo "<tr>";
			echo "<td>" . $row[0] . "</td>";
			echo "<td>" . $row[1] . "</td>";
			echo "<td>" . $row[2] . "</td>";
			echo "</tr>";
		}
    		$result->free();
       }
    } while ($con->next_result());
}
echo "</table>";

echo "<p>------------------------------------------------------------------------</p>";
mysqli_close($con);

?>

</body>
</html>
