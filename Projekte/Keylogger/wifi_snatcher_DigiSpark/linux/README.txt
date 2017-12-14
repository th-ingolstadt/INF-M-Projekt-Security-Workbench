# Linux Keylogger Digispark
Für dieses Szenario muss der angegriffene Linux-Rechner das Terminal mit der Tastenkombination ctrl+alt+t öffnen können.
Außerdem muss Python installiert sein, da die Payload einen Reverse-Shell mittels Python öffnet.

Damit die Reverse-Shell geöffnet werden kann muss der Angreifer vorher auf den eingestellten Port(1234) hören.
Dies geht zum Bespiel mit netcat:

nc -l -p 1234

Die Payload muss auf einem Webserver zur Verfügung gestellt werden.


Ablauf:
1) Das Opfer schließt sich an lokales Raspberry-Netz
2) Das Opfer startet networking service neu: sudo service networking restart
3) Der Angreifer startet netcat und lauscht auf die Reverse-Shell mit: nc -l -p 1234
4) Das Opfer schließt den Keylogger an und der Angriff wird ausgeführt
