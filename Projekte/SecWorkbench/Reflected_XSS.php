<?php
    include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_UpperPart.html";
?>

<script>
    window.onload = function(){
        var title = "Session Management";
        document.getElementById("pageTitle").innerHTML = title;
        document.getElementById("titleDiv").innerHTML = title;
        document.getElementById("pageDescription").innerHTML = "";        
};
</script>

<!DOCTYPE html>
<html>
<head>
    <title>
        Webanwendung - Logn
    </title>

    <meta name="keywords" content="" />
    <meta name="description" content="" />

    <!--<script src="angriff.js"></script>-->

    </br>

    <center>Anmeldeoberfläche für einen reflektierten XSS-Angriff</center>

    <br />

    
    <style type="text/css">
        #loginf {
            width: 500px;
            margin: 0 auto;
            padding: 30px;
            background: #808080;
        }

            #loginf p {
                width: 500px;
                height: 25px;
                line-height: 25px;
            }

                #loginf p input {
                    float: right;
                    width: 70%;
                    border: 2px solid #ff0000;
                }
    </style>

</head>
<body>

   

<div id='loginf'>

    <form method='get' action='<?php PHP_SELF ?>'>
        <p>
            Vorname:
            <input type="text" name="user" />
        </p>
        <p>
            Nachname:
            <input type="text" name="pass" />
        </p>
       

        <!---->



        <!--<a onklick=>login></a>

        <input onclick="login" type="button" class="btn btn-primary" align="right" value="Login" />-->

        <?php

                $benutzer = $_GET['user'];
                $passwort = $_GET['pass'];
                $loginbutton = $_GET['login'];
                if ($loginbutton){
                    echo $benutzer;
                    echo $passwort;
                }
                //echo $benutzer;
                //echo $passwort;

        ?>
        <br />
        <br />
        <input name="login" type="submit" value="LOGIN" />
        <input name="reset" type="reset" value="RESET" />
    </form>

</div>


</body>

</html>

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

 
 <?php
    include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_LowerPart.html";
?>

// mark sidebar element for this page active
<script> document.getElementById('sbiSessionManagement').className = 'active'; </script>
