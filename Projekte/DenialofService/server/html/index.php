<html>
<head>
<title>Denial of Service Website</title>
<link rel="stylesheet" type="text/css" href="index.css"/>
<script>

setInterval(getTime, 1000);

function getTime(){

	var xmlhttp = new XMLHttpRequest();


	xmlhttp.onreadystatechange = function(){
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
			document.getElementById("clock").innerHTML = xmlhttp.responseText;
		}
	}
	xmlhttp.open("GET", "clock.php", true);
	xmlhttp.send();

}
</script>
</head>

<h1>
Website für Denial of Service Angriffe
</h1>

<p>
Diese Webseite stellt die aktuelle Uhrzeit dar.
Dafür holt der Client sich jede Sekunde die neue Uhrzeit vom Server.
Ein Denial of Service Angriff ist erfolgreich, wenn der Server nicht mehr erreichbar ist und damit die Uhr stehen bleibt.
</p>

<div id="clock" class="clock"></div>

</html>
