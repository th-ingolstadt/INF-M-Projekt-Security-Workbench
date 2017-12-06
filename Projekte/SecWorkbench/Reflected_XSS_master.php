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
                <h3 class="box-title">Übersichtsseite:</h3>
            </div>
            <div class="box-body">
                Übersicht..........................
                <br>
                <br>
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

                <a href="javascript:firsttip();">1. Tipp:</a>
                <output id='firsttip'></output>

                <a href="javascript:secondtip();">2. Tipp:</a>
                <output id='secondtip'></output>

                <a href="javascript:thirdtip();">3. Tipp:</a>
                <output id='thirdtip'></output>


                <script>
                    function firsttip()
                    {
                        document.getElementById('firsttip').innerHTML = "Versuchen Sie über eines der beiden Eingabefelder\n\
                            Scriptcode in die Webanwendung zu schleusen.";
                    }

                    function secondtip()
                    {
                        document.getElementById('secondtip').innerHTML = "2.tipp.";
                    }

                    function thirdtip()
                    {
                        document.getElementById('thirdtip').innerHTML = "3.tipp.";
                    }
                </script>


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
