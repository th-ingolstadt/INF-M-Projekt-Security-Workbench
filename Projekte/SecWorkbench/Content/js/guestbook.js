function checkCookiesForLoggedinUser() {
    var usrnameCookie = getCookie("username");
    var pwdCookie = getCookie("password"); 

    if ((usrnameCookie === "123" && pwdCookie === "123")
        || (usrnameCookie === "admin" && pwdCookie === "admin")
        || (usrnameCookie === "user" && pwdCookie === "password1")) {
        document.getElementById("labelGuestbook").innerHTML = "Hinterlasse eine Eintrag in " + usrnameCookie + "'s Gästebuch";
        document.getElementById("guestbookHeader").innerHTML = usrnameCookie + "'s Gästebuch"; 
        document.getElementById("guestbook").removeAttribute("hidden");
    } 
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkLoginInput() {
    var username = document.getElementById("usrname").value;
    var password = document.getElementById("pwd").value;
    document.cookie = "username=" + username;
    document.cookie = "password=" + password; 
}

function checkLoginDOMXSS() {
    var username = document.getElementById("usrname").value;
    var password = document.getElementById("pwd").value; 

    if (username === "admin" && password === "admin") {
        var pos = document.URL.indexOf("context=") + 8;
        document.write(document.URL.substring(pos, document.URL.length));
        document.getElementById("shoppingList").removeAttribute("hidden");
    }
}
