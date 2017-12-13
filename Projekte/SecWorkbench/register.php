<?php if (isset($_POST['registrierung'])) {
     
        $conn = new mysqli("localhost", "root", "", "tutorials");
        
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        // falls man die Erfolgsnachricht ausgeben möchte
        // echo "Connected successfully";
        
        $username = $_POST["username"];
        $passwort =$_POST["passwort"];
        
        $sql = "INSERT INTO users (username, passwort) VALUES ('$username', '$passwort')";

        if ($conn->query($sql) === TRUE) {
            //Falls man die Erfolgsnachricht ausgeben möchte
            //echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
        include ('SessionManagement_FirstExampleResponse.html');
        
              
        $conn->close();
    
}


?>





