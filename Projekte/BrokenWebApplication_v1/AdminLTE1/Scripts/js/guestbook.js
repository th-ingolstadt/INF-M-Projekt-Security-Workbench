var id = 1; 

function EntryDTO(id, date, content) {
    this.id = id;
    this.date = date;
    this.content = content

    this.pruefe = function () {
        if (this.content === "") {
            throw "ERROR! Eines der Elemente ist nicht initialisiert";
        } else if (this.date < 0) {
            throw "ERROR! Die Postleitzahl darf nicht negativ sein!";
        }

    }
    this.toString = function () {
        return "{" + this.id + ", " +
            this.date + ", " +
            this.content + "}";
    }
}

function EntryDAO() {
    this.entryArray = [];
    
    this.speichern = function () {
        localStorage.setItem('entryDAO', JSON.stringify(this)); // stringify -> JavaScript obj zu JSON Zeichenkette
    };

    this.laden = function () {
        var gespeichertesDAOalsString = localStorage.getItem('entryDAO');
        var gespeichertesDAO = JSON.parse(gespeichertesDAOalsString); // parse// JSON zu JavaScript

        if (gespeichertesDAO != null)
            this.entryArray = gespeichertesDAO.entryArray;

        for (i = 0; i < this.entryArray.length; ++i) {
            this.entryArray[i] = new PersonDTO(
                this.entryArray[i].id,
                this.entryArray[i].date,
                this.entryArray[i].content);
        }

        console.log('gespeichertesDAO: ', gespeichertesDAO);
    };

	/*
	 * Hilfsfunktionen
	 */
	/*
	 * Liefert true, falls die übergebene Personenbeschreibung 'person' die Präfixe 
	 * für 'name' und 'ort' besitzt bzw. 'name' und 'ort' leer sind (keine Prüfung).
	 * Sonst wird false zurückgegeben.
	 */
    this.filter = function (person, name, ort) {
        // *** (2) ***
        if (name === undefined && ort === undefined) {
            return true;
        } else if (person.name.substr(0, name.length) === name &&
            person.ort.substr(0, ort.length) === ort) {
            return true;
        }

        return false;
    };

    this.findeAlle = function () {
        this.laden();
        var ergebnis = [];
        var j = 0;

        for (i = 0; i < this.entryArray.length; ++i) {
            if (this.entryArray[i].id != -1) {
                ergebnis[j++] = this.entryArray[i];
            }
        }

        ergebnis.sort(
            function (p1, p2) {
                return p1.id - p2.id;
            }
        );

        return ergebnis;
    };

    this.newEntry = function (entry) {
        this.laden();

        for (i = 0; i < this.entryArray.length; ++i) {
            if (this.entryArray[i].id == -1) {
                break;
            }
        }
        entry.id = i;
        this.entryArray[entry.id] = person;
        this.speichern();
    };

    this.actualizeEntry = function (entry) {
        this.laden();
        if (this.findePersonZuId(entry.id) !== "undefined") {
            this.entryArray[entry.id] = person;
            this.speichern();
        }
    };

    this.loeschePerson = function (id) {
        // *** (4) ***
        // First step: Search for the person

        // var index = 0;
        var i;
        for (i = 0; i < this.entryArray.length; i++) {
            if (this.entryArray[i].id === id) {
                this.entryArray[i].id = -1;
                this.speichern();
                break;
            }
        }
		/*this.laden();
		this.personArray[index].id = -1;
		this.speichern();*/
		/* var index = this.findePersonZuId(id);
		if ( index !== "undefined") {
			this.personArray[index].id = -1;
		//	delete this.personArray[index];
		//	this.personArray.splice(index, 1);
		//	localStorage.removeItem(personDAO.personArray[index]);
			this.speichern();
		} else {
			alert("ERROR");
		}*/
    };
}

function gibPersonDAO() {
    var dao = "undefined";

    if (typeof (Storage) !== "undefined") {
        dao = new EntryDAO();
        if (localStorage['entryDAO']) {
            try {
                dao.laden();
                for (i = 0; i < dao.entryArray.length; ++i) {
                    var p = dao.entryArray[i];
                    console.log(p.toString());
                }

            } catch (error) {
                alert(error);
            }
        }
    } else {
        alert("Sorry, your browser does not support web storage…");
    }

    return dao;
}

var entryDAO = gibPersonDAO();

function storeEntry() {
    var date = new Date(); 
    var entry = new EntryDTO(id++,
        document.getElementById("guestbookEntry").value,
        date.toDateString
    );

    try {
        entry.pruefe(); 
        entry
    } catch (errorMsg) {
        alert(errorMsg)
    }
}