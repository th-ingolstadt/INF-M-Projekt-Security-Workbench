<?php if (isset($_POST['login'])) {

        $conn = new mysqli("127.0.0.1", "normal_user", "master42", "vulnerableDB");
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        // falls man die Erfolgsnachricht ausgeben möchte
        // echo "Connected successfully";

        $username = $_POST["username"];
        $passwort =$_POST["passwort"];

        $sql = "SELECT * FROM cookieManagementUsers where username = '$username' and password='$passwort'" ;

       // echo $conn->query($sql);
        $result = $conn->query($sql);

        if( $result->num_rows >0){
            //echo $result->num_rows ;
            //session_start();
            $_SESSION["usernameAufg2"] = $username;

            //echo $_SESSION["usernameAufg2"];
            //echo $username;
            include ('SessionManagement_SecondExampleResponse.html');
        }else{
            echo '<script type="text/javascript">alert("Dein Login war leider nicht erfolgreich!");</script>';
            include ('SessionManagement_SecondExample.html');
        }




        $conn->close();

}


?>
