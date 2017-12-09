<?php if (isset($_POST['login'])) {
     
        $conn = new mysqli("localhost", "root", "", "tutorials");
        
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        // falls man die Erfolgsnachricht ausgeben möchte
        // echo "Connected successfully";
        
        $username = $_POST["username"];
        $passwort =$_POST["passwort"];
        
        //$sql = "SELECT * FROM users (username, passwort) VALUES ('$username', '$passwort')";
        //$sql = "SELECT userid, username, passwort FROM users";

        //$sql = "SELECT userid, username, passwort FROM users;";
        $sql = "SELECT * FROM users where username = '$username' and passwort='$passwort'" ;
        
       // echo $conn->query($sql);
        $result = $conn->query($sql);
        
        if( $result->num_rows >0){
            //echo $result->num_rows ;
            session_start();
            $_SESSION["username"] = $username;
            
            //echo $_SESSION[$username];
            include ('SessionManagement_SecondExampleResponse.html');
        }else{
            echo '<script type="text/javascript">alert("Dein Login war leider nicht erfolgreich!");</script>';
            include ('SessionManagement_SecondExample.html');
        }
        
        
       
              
        $conn->close();
    
}


?>




