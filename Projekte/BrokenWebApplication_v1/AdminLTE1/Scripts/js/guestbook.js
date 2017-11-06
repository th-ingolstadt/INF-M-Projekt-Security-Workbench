function checkCookiesForLoggedinUser() {
    var usrnameCookie = getCookie("username");
    var pwdCookie = getCookie("password"); 

    alert(usrnameCookie + "--Cookie:--" + pwdCookie); 
    if (usrnameCookie === "123" && pwdCookie === "123") {
        document.getElementById("guestbook").removeAttribute("hidden");
        getContentOfGuestbook(); 
    } else {
        alert("hidden...");
    }
}

function getContentOfGuestbook() {
    /*
    var db = Database.Open("Database1");
    var selectQueryString = "SELECT * FROM Guestbook";

    alert("before tableref");
    var tableRef = document.getElementById('guestbook').getElementsByTagName('tbody')[0];
    alert("after tableref"); 
    var row; 
    foreach(row in db.Query(selectQueryString))
    {
        alert("inside forecach"); 
        var newRow = tableRef.insertRow(tableRef.rows.length);
        var newCell = newRow.insertCell(0);
        var newText = document.createTextNode(row.username);
        newCell.appendChild(newText);
        var dateCell = newRow.insertCell(1);
        var dateText = document.createTextNode(row.date);
        dateCell.appendChild(dateText); 
        var commentCell = newRow.insertCell(2);
        var commentText = document.createTextNode(row.comment);
        commentCell.appendChild(commentText); 
    } */
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkLoginInput() {
    var username = document.getElementById("usrname").value;
    var password = document.getElementById("pwd").value;
    alert(username + "--" + password); 
    document.cookie = "username=" + username;
    document.cookie = "password=" + password; 
}
