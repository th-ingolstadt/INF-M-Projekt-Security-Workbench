<?php
include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_UpperPart.html";
?>

<script>
    window.onload = function () {
        var title = "Cross Site Scripting - Reflected";
        document.getElementById("pageTitle").innerHTML = title;
        document.getElementById("titleDiv").innerHTML = title;
        document.getElementById("pageDescription").innerHTML = "Übung 2";
    };
</script>

<div class="row">


    <div class="col-xs-12 col-md-7">
        <div class="box box-default">
            <div class="box-header">
                <h3 class="box-title">Aufgabenstellung:</h3>
            </div>
            <div class="box-body">
                Neben den, in der Einführung erwähnten Beispiel kann ein Ziel eines Reflected-Anfgriffs
                natürlich auch anders aussehen. Im folgenden Beispiel, das von Ihnen attackiert werden soll, 
                finden Sie zwei Eingabefenster, die für Ihren Vor- und Nachname vorgesehen sind. 
                Nach den Betätigen des "LOGIN" - Button sollen Sie mit Ihren vollen Namen begrüßt werden.
                Da Ihre Eingabe, was im Normalfall Ihr Vor- und Nachname ist, direkt wieder ausgegeben wird,
                wird uns so ermöglicht einen Reflected-XSS-Angriff auszuführen. 
            </div> 
            <div class="box-body">

            </div>
        </div>
    </div>

    <div class="col-xs-12 col-md-5">
        <div class="box box-warning">
            <div class="box-header">
                <h3 class="box-title">Media</h3>
            </div>
            <div class="box-body">

            </div>
        </div>
    </div>

    <div class="col-xs-12 col-md-5">
        <div class="box box-success">
            <div class="box-header">
                <h3 class="box-title">Tipps</h3>
            </div>
            <div class="box-body">

            </div>
        </div>
    </div>

    <div class="col-xs-12 col-md-7">
        <div class="box box-default">
            <div class="box-header">
                <h3 class="box-title">Ergänzung zur Aufgabenstellung:</h3>
            </div>
            <div class="box-body">
              Im Grunde bleibt die Aufgabenstellung zu der 1. Übung fast identisch.<br>
              Der einzige Unterschied bezieht sich auf die Zeichen die in den beiden Zeichenfeldern die für 
              Vor- und Nachname zulässig sind. Folglich wird es Ihnen erschwert einen Scriptcode über die Webanwendung
              auszuführen.
              <br>
              <br>
              Nach dem Abschließen dieser Übung können sie zu <a href="Reflected_XSS_III.php">Übung 3</a> übergehen.
            </div>          
            <div class="box-body">

            </div>
        </div>
    </div>

</div>

<br />


<style type="text/css">
    #loginf p 
    {
        width: 500px;
        height: 25px;
        line-height: 25px;
    }

    #loginf p input 
    {
        float: right;
        width: 60%;
    }
</style>


</head>
<body>

    <div id='loginf'>

        <form method='get' action='<?php echo($_SERVER['PHP_SELF']); ?>'>
            <p>Vorname:<input type="text" name="user" /></p>
            <p>Nachname:<input type="text" name="pass" /></p>

            <?php
            //$benutzer = $_GET['user'];
            //$passwort = $_GET['pass'];
            //$loginbutton = $_GET['login'];



            if (!isset($_GET['login']) or $_GET['login']) {

                if ((isset($_GET['user'])) && (isset($_GET['pass']))) {

                    if (!empty($_GET['user']) && !empty($_GET['pass'])) {
                        if ((!preg_match('["|\']', ($_GET['user']))) && !preg_match('["|\']', ($_GET['pass']))) {
                            if (isset($_GET['user'])) {
                                echo 'Hallo, ';
                                echo $_GET['user']; //$benutzer;
                                echo ' ';
                            }
                            if (isset($_GET['pass'])) {
                                echo $_GET['pass']; //$passwort;
                            }
                        } else {
                            echo "Die eingebenenen Zeichenketten enthalten ungültige Zeichen.";
                        }
                    } else {
                        echo "Vor- oder Nachname nicht eingegeben, bitte befüllen Sie beide Eingabefelder.";
                    }
                }
            }
            ?>
            <br />
            <input name="login" type="submit" value="LOGIN" />
            <input name="reset" type="reset" value="RESET" />
        </form>
    </div>


</body>

</html>

<!-- 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
-->


<?php
include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_LowerPart.html";
?>

// mark sidebar element for this page active
<script> document.getElementById('sbiSessionManagement').className = 'active';</script>
