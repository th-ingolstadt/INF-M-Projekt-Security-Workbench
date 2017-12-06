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
<center>
    ACHTUNG: Es ist ein Fehler aufgetreten, füllen Sie bitte nur die folgende Eingabefelder aus, sodass der Vorgang 
    ohne Probleme fortgeführt werden kann.
</center>

<div id='loginf'>
        <form method='get' action='<?php echo($_SERVER['PHP_SELF']); ?>'>
            <p>Vorname:<input type="text" name="user" /></p>
            <p>Nachname:<input type="text" name="pass" /></p>

            <?php

            ?>
            <br />
            <input name="login" type="submit" value="LOGIN" />
            <input name="reset" type="reset" value="RESET" />
        </form>
</div>