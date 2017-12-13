<?php
include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_UpperPart.html";
?>

<script>
    window.onload = function () {
        var title = "Cross Site Scripting - Reflected";
        document.getElementById("pageTitle").innerHTML = title;
        document.getElementById("titleDiv").innerHTML = title;
        document.getElementById("pageDescription").innerHTML = "Übung 3";
    };
</script>

<div class="row">

    <div class="col-xs-12 col-md-7">
        <div class="box box-default">
            <div class="box-header">
                <h3 class="box-title">Aufgabenstellung:</h3>
            </div>
            <div class="box-body">
                  Wie die Aufgabenstellung der 2. Übung wird Ihnen der Cross-Site-Scripting-Angriff der 3. Übung, durch weitere
                unzulässige Zeichen, wiederrum erschwert.  
                <br>
                <br>
                Nach dem Abschließen dieser Übung können Sie zur <a href="Reflected_XSS_IV.php">Übung 4</a> übergehen.
            </div>       
        </div>
    </div>

    <div class="col-xs-12 col-md-5">
        <div class="box box-default collapsed-box">
            <div class="box-header">
                <h3 class="box-title">Tipps</h3>
                <div class="box-tools pull-right">
                    <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i></button>
                </div>
            </div>
            <div class="box-body">
                <div class="box-group" id="accordion">
                    <div class="panel box box-success">
                        <div class="box-header">
                            <h4 class="box-title">
                                <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">
                                    1. Tipp
                                </a>
                            </h4>
                        </div>
                        <div id="collapseOne" class="panel-collapse collapse">
                            <div class="box-body">
                                Die Zeichen bzw. die Zeichenkette ",' und "script" sind nicht zulässig.
                            </div>
                        </div>
                    </div>
                    <div class="panel box box-warning">
                        <div class="box-header">
                            <h4 class="box-title">
                                <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">
                                    2. Tipp
                                </a>
                            </h4>
                        </div>
                        <div id="collapseTwo" class="panel-collapse collapse">
                            <div class="box-body">
                                Eine Lösung lautet &ltbody onload=alert(String.fromCharCode(84,69,83,84))>.
                            </div>
                        </div>
                    </div>                       
                </div>
            </div>
        </div>
    </div>
</div>    


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
            if ((isset($_GET['user'])) && (isset($_GET['pass']))) {

                if (!empty($_GET['user']) && !empty($_GET['pass'])) {
                    if ((!preg_match('["|\'|script]', ($_GET['user']))) && !preg_match('["|\'|script]', ($_GET['pass']))) {
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
