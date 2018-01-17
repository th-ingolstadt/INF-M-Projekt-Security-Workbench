
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

function startDOMBasedXSS() {
    document.cookie = "username=" + "root";
    document.cookie = "password=" + "hallo123"; 
    document.cookie = "\n Du has dieses Tutorial gelöst!"; 
    
    document.getElementById("hidingList").removeAttribute("hidden");
    hiddenState = true; 
    
    select = document.getElementById('languageList');
    
    var opt = document.createElement('option');
    opt.value = "Englisch";
    opt.innerHTML = "Englisch"; 
    select.appendChild(opt); 

    var opt2 = document.createElement('option');
    opt2.value = "France";
    opt2.innerHTML = "France"; 
    select.appendChild(opt2); 

    var opt3 = document.createElement('option');
    opt3.value = "Italian";
    opt3.innerHTML = "Italian"; 
    select.appendChild(opt3); 

    var opt4 = document.createElement('option');
    opt4.value = "Spanish";
    opt4.innerHTML = "Spanish"; 
    select.appendChild(opt4); 

    var opt5 = document.createElement('option');
    opt5.value = "Chinese";
    opt5.innerHTML = "Chinese"; 
    select.appendChild(opt5); 
}

