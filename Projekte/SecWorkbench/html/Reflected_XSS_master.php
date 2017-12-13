<?php
include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_UpperPart.html";
?>

<script>
    window.onload = function () {
        var title = "Cross Site Scripting - Reflected";
        document.getElementById("pageTitle").innerHTML = title;
        document.getElementById("titleDiv").innerHTML = title;
        document.getElementById("pageDescription").innerHTML = "Übersichtsseite";
    };
</script>

<div class="row">


    <div class="col-xs-12 col-md-7">
        <div class="box box-default">
            <div class="box-header">
                <h3 class="box-title">Theorie</h3>
            </div>
            <div class="box-body">               
                <center>
                    <figure>
                        <video src="Content/img/Attacks/XSS_Reflected/xss_reflected.mp4" controls width="560" height="315"></video>
                    </figure>
                </center>
                <br>
                Das Reflected-Cross-Site-Scripting ist ein Angriff, 
                bei dem die Eingaben des Benutzers direkt vom Server wieder zurückgesendet und anschließend ausgegeben werden.
                Enthält diese Eingabe ausführbaren Scriptcode, wird dieser Code direkt ausgeführt.<br>
                Ein Beispiel für so ein Verhalten findet man häufig bei der Suchfunktion einer Website.
                Da der eingegebene Suchbegriff meistens in einer Form wie z.B. "... der Suchbegriff "Beispielbegriff" wurde nicht gefunden..." 
                wieder augegeben wird bietet sich dies vom Prinzip her als Angriffsstelle für einen Reflected Cross-Site-Scripting Angriff an.<br>
                Dadurch das bei php die Eingegebenen Daten, wie z.B. ein Suchbegriff nicht selten mittels $GET übergeben werden, wird die
                Eingabedaten in der URL gespeichert. Dies ermöglicht uns das Versenden des Schadecodes, indem man die URL inklusive Schadecodes an
                das Opfer sendet.
                <br>
                <br>
                Dies wird in der folgenden Grafik veranschaulicht:
                <center>
                <img src="Content/img/Attacks/XSS_Reflected/xss_reflected.png" width="560" height="300">
                </center>
            </div> 
            <div class="box-body">

            </div>
        </div>
    </div>
    
    <div class="col-xs-12 col-md-7">
        <div class="box box-default">
            <div class="box-header">
                <h3 class="box-title">Übungen zu Reflected Cross-Site-Scripting</h3>
            </div>
            <div class="box-body">                              
                <a href="Reflected_XSS.php">1. Übung</a><br>
                <a href="Reflected_XSS_II.php">2. Übung</a><br>
                <a href="Reflected_XSS_III.php">3. Übung</a><br>
                <a href="Reflected_XSS_IV.php">4. Übung</a><br>
                <a href="Reflected_XSS_V.php">5. Übung</a><br>
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
