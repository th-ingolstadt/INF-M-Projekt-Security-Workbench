# Linux Keylogger Digispark
Für dieses Szenario muss der angegriffene Linux-Rechner das Terminal mit der Tastenkombination ctrl+alt+t öffnen können.
Außerdem muss Python installiert sein, da die Payload einen Reverse-Shell mittels Python öffnet.
Damit die Reverse-Shell geöffnet werden kann muss der Angreifer vorher auf den eingestellten Port(1234) hören.
Dies geht zum Bespiel mit netcat:

nc -l -p 1234

Die Payload muss auf einem Webserver zur Verfügung gestellt werden.
