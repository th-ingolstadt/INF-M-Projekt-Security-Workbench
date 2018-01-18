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
                        <video src="Content/videos/ReflectedXSS_mitAudio.mp4" controls width="560" height="315"></video>
                    </figure>
                </center>
                <br>
                Das Reflected-Cross-Site-Scripting (XSS) ist ein Angriff, 
                bei dem die Eingabe des Benutzers direkt vom Server wieder zurückgesendet und anschließend ausgegeben wird.
                Enthält diese Eingabe ausführbaren Scriptcode, wird der Code direkt ausgeführt.<br>
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
                <img src="Content/img/xss_reflected.png" width="560" height="300">
                </center>
            </div> 
            <div class="box-body">

            </div>
        </div>
    </div>
    
    
    
    <div class="col-xs-12 col-md-5">
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
    
    <div class="col-xs-12 col-md-7">
        <div class="panel box collapsed-box">
            <div class="box-header">
                <h3 class="box-title">Schutzmaßnahmen gegen Reflected Cross-Site-Scripting:</h3>
                <div class="box-tools pull-right">
                    <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i></button>
                </div>
            </div>
            <div class="box-body">             
                <u>Schutzmaßnahmen für Webseitenbetreiber:</u>
                <br>
                Um sich gegen Reflected Cross-Site Scripting zu schützen, muss man sich klarmachen, 
                dass XSS ein reines Ausgabeproblem ist.<br> 
                An der Stelle, an der die Benutzereingaben in den Quelltext eingebunden werden, 
                sollten diese so maskiert werden, dass der Browser diese nicht als Code verarbeitet, 
                sondern nur als Daten darstellen kann. 
                Die einfachste Form der Maskierung ist die Ersetzung der einleitenden spitzen Klammer bei HTML-Tags durch ein &amp;lt.
                Dadurch wird das folgende script-Tag vom Browser nicht geparst.
                <br>
                <br>
                <u>Beispiel: Maskierung von HTML-Code</u>
                <br>
                <br>
                &ltscript&gt....&lt/script&gt
                <br>
                &amp;ltscript&gt....&lt/script&gt
                <br>
                <br>
                <u>Schutzmaßnahmen für Webseitennutzer:</u>
                <br>
                Durch Ausschalten der JavaScript-Unterstützung (Active Scripting) im Browser kann man sich gegen clientseitige XSS-Angriffe schützen.<br>
                Allerdings bieten einige Browser weitere Angriffsvektoren. Desweiteren hilft das Ausschalten des Active Scripting nur für XSS das mit JavaScript arbeitet. 
                Wenn nun HTML-Injection verwendet wird, bringt das Abschalten von Active Scripting im Browser keine Verbesserung.
                Außerdem gibt es für einige Browser Erweiterungen, mit denen gezielt mögliche XSS-Angriffe erkannt und verhindert werden.
                
                
                
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
