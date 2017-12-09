<?php

if (isset($_POST['sent'])) {

    $conn = new mysqli("localhost", "root", "", "swb_database");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $comment = $_POST["guestbookentry"];
    $date = date("Y-m-d");
    $sql = "INSERT INTO Guestbook (User, Date, Comment) VALUES ('admin', '".$date."', '".$comment."')";
    if ($conn->query($sql) === TRUE) {
        
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
    
    $conn->close();
}

?>
    