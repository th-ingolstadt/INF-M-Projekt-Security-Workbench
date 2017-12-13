<?php
include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_UpperPart.html";
?>

<script>
    window.onload = function () {
        var title = "Cross Site Scripting - Reflected";
        document.getElementById("pageTitle").innerHTML = title;
        document.getElementById("titleDiv").innerHTML = title;
        document.getElementById("pageDescription").innerHTML = "Übung 4";
    };
</script>

<div class="row">


    <div class="col-xs-12 col-md-7">
        <div class="box box-default">
            <div class="box-header">
                <h3 class="box-title">Beschreibung</h3>
            </div>
            <div class="box-body">
                Nach den Übungen 1 bis 3 sind Sie nun mit dem Prinzip des "Reflected Cross-Site-Scripting" vertraut.<br>
                Wie Sie möglicherweise schon feststellen konnte sind die vorangegangenen Übungen, in denen Schadecode bzw.
                Scriptcode auf den eigenen Rechner ausgeführt wird, nicht sehr sinnvoll und bedrohlich.<br>
                Wie der Scriptcode in eine bedrohliche Form gebracht und versendet werden kann, wird in den folgenden Übungen
                behandelt.               
            </div> 
            <div class="box-body">

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
                                Zum einbinden des vorgegebenen Formulars bietet sich &ltiframe>&lt/iframe>.
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
                                Mit gewissen Codebefehlen können Sie die Datei so einbinden das, das Formular nicht
                                verdächtig nach Schadecode aussieht.
                                So lässt sich zum Beispiel mit "height='...'" und "width='...'" die größe des Formulars anpassen.
                                <br>
                            </div>
                        </div>
                    </div> 
                    <div class="panel box box-danger">
                        <div class="box-header">
                            <h4 class="box-title">
                                <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">
                                    3. Tipp
                                </a>
                            </h4>
                        </div>
                        <div id="collapseThree" class="panel-collapse collapse">
                            <div class="box-body">
                                Eine mögliche Lösung lautet<br> &ltiframe src="Reflected_XSS_iFrame.php" style="border:4px solid #FF0000;" height="200" width="70%"></iframe>.
                                <br>
                            </div>
                        </div>
                    </div>  
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-xs-12 col-md-7">
        <div class="box box-default">
            <div class="box-header">
                <h3 class="box-title">Aufgabenstellung:</h3>
            </div>
            <div class="box-body">
                Ihre Aufgabe ist es nun ein Schadecode zu integrieren der ein typisches Login-Formular auf der Webanwendung erscheinen lässt.
                Dieses soll den Opfer dazu verleiten seine möglicherweise empfindlichen Daten einzugeben.
                Im Anschluss sollen die möglicherweise empfindlichen Benutzerdaten dem Angreifer zugesendet werden.
                Zur Vereinfachung sollen Sie lediglich das Formular einbinden und möglichst so das es dem Opfer nicht wie integrierten Schadcode vorkommt.
                <br>
                Für diesen Vorgang wird üblicherweise ein Link mittels Scriptcode eingebunden.
                Um dies für Sie etwas zu vereinfachen wird mit "Reflected_XSS_iFrame.php" ein Formular bereit gestellt, das Sie einbinden sollen.
                <br>
                <br>
                Falls Ihnen das gelungen ist können Sie anschließend zur <a href="Reflected_XSS_V.php">Übung 5</a> übergehen.
            </div> 
            <div class="box-body">

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

            if (!isset($_GET['login']) or $_GET['login']) {

                if ((isset($_GET['user'])) && (isset($_GET['pass']))) {

                    if (!empty($_GET['user']) && !empty($_GET['pass'])) {
                        if (isset($_GET['user'])) {
                            echo 'Hallo, ';
                            echo $_GET['user']; //$benutzer;
                            echo ' ';
                        }
                        if (isset($_GET['pass'])) {
                            echo $_GET['pass']; //$passwort;
                        }
                    } else {
                        echo 'Vor- oder Nachname nicht eingegeben, bitte befüllen Sie beide Eingabefelder.';
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