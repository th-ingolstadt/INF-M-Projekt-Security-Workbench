<?php
    include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_UpperPart.html";
?>

<!-- <!doctype html>
<html lang="de">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stored XSS</title>

        <link rel="stylesheet" href="../Content/css/AllStyles.css">
        <link rel="stylesheet" href="../Content/css/AdminLTE.min.css">

        <script src="../Content/js/guestbook.js" type="text/javascript"></script>
        <script src="../Content/js/plugins/jquery/jquery-2.2.4.min.js"></script>
        <script src="../Content/js/plugins/bootstrap/bootstrap.min.js"></script>
--> 
        <style>
            .modal-header, h4, .close {
                background-color: #006dcc;
                color: white !important;
                text-align: center;
                font-size: 30px;
            }

            .modal-footer {
                background-color: #f9f9f9;
            }
        </style>
        <script>
            $(document).ready(function () {
                $("#letsGo").click(function () {
                    $("#loginModal").modal();
                });
            });
        </script>  
    </head>
    <!-- DB INSERT SELF FORM VALIDATION --> 
    <?php if (isset($_POST['sent'])) {

        $conn = new mysqli("localhost", "root", "", "swb_database");

       if ($conn->connect_error) {
           die("Connection failed: " . $conn->connect_error);
       }

       $comment = $_POST["guestbookentry"];
       $date = date("Y-m-d");
       $sql = "INSERT INTO Guestbook (User, Date, Comment) VALUES ('admin', '" . $date . "', '" . $comment . "')";
       if ($conn->query($sql) === TRUE) {
           
       } else {
           echo "Error: " . $sql . "<br>" . $conn->error;
       }

       $conn->close();
   }
   ?>

    <body onload="checkCookiesForLoggedinUser();">
        <div class="container">
            <div class="row">
                <div class="col-xs-8 col-md-8">
                    <div class="box box-default">
                        <div class="box-header">
                            <h3 class="box-title">Aufgabenstellung</h3>
                        </div>
                        <div class="box-body">
                            <h5><b><u>Stored Cross Site Scripting</u></b></h5>
                            <p style="text-align: justify;">
                                Gespeicherte XSS ist eine Attake bei der ein Skript injiziiert und permanent auf dem Zielserver z. B. in einer Datenbank, einem Nachrichtenforum oder einem Kommentarfeld gespeichert wird.
                                Sobald dann ein Client ein HTTP-Request nach der Webseite mit den gespeicherten Informationen anfrägt, wird der Server ihm mit dem böswilligen Code antworten. 
                                Stored XSS wird manchmal auch als Persistent oder Type-I XSS bezeichnet. 
                            </p>
                            <div class="col-xs-12 col-md-12">
                                <iframe width="600" height="400" src="http://www.powtoon.com/embed/bqJxlVYaeio/" frameborder="0"></iframe><br />
                           <!--   <img src="~/Content/img/storedXSS.jpg" class="img-responsive" alt="Stored-Cross-Site Scripting"> --> 
                            </div>
                            <h5><b><u>Aufgabe</u></b></h5>
                            <blockquote>
                                <p>
                                    Dieses Tutorial entspricht einem Gästebuch, in dem User eine Nachricht hinterlassen können. Die eingetragenen Daten werden serverseitig in einer
                                    Datenbank gespeichert. Finden Sie eine Möglichkeit, um diese Sicherheitslücke auszunutzen
                                </p>
                            </blockquote>
                            <button type="button" class="btn btn-primary" id="letsGo">Los Geht's</button>
                        </div>
                    </div>

                    <div class="box box-default" id="guestbook" hidden>
                        <div class="box-header">
                            <h3 class="box-title">Aufgabe</h3>
                        </div>
                        <div class="box-body">
                                <form role="form" method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
                                <div class="form-group">
                                    <label id="labelGuestbook" for="guestbookEntry"></label>
                                    <textarea class="form-control" id="guestbookentry" name="guestbookentry" rows="4"></textarea>
                                </div>
                                <button type="submit" name="sent" class="btn btn-primary">Submit</button>
                            </form>
                            <br /><br />
                            <h3 id="guestbookHeader">Gästebuch</h3>
                            <table class="table table-striped" id="guestbook">
                                <thead>
                                    <tr>
                                        <th>Username</th>
                                        <th>Datum</th>
                                        <th>Eintrag</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php
                                    $conn = new mysqli("localhost", "root", "", "swb_database");

                                    if ($conn->connect_error) {
                                        die("Connection failed: " . $conn->connect_error);
                                    }

                                    $sqlQuery = "SELECT * FROM Guestbook";
                                    $result = $conn->query($sqlQuery);
                                    if ($result->num_rows > 0) {
                                        while ($row = $result->fetch_assoc()) {
                                            echo "<tr>";
                                            echo "<td>" . $row["User"] . "</td>";
                                            echo "<td>" . $row["Date"] . "</td>";
                                            echo "<td>" . $row["Comment"] . "</td>";
                                            echo "</tr>";
                                        }
                                    } else {
                                        echo "Sth is wrong with the database :(";
                                    }
                                    $conn->close();
                                    ?>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <div class="col-xs-4 col-md-4">
                    <div class="box box-default collapsed-box">
                        <div class="box-header with-border">
                            <h3 class="box-title">Tipps</h3>
                            <div class="box-tools pull-right">
                                <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i></button>
                                <button type="button" class="btn btn-box-tool" data-widget="remove"><i class="fa fa-remove"></i></button>
                            </div>
                        </div>
                        <div class="box-body">
                            <div class="row">
                                <div class="col-xs-10 col-md-10">
                                    <ul class="list-group">
                                        <li class="list-group-item">Schreibe den Schadcode als JavaScript als einen Gästebucheintrag.</li>
                                        <li class="list-group-item">Die Logindaten werden als Cookie gespeichert. </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="modal fade" id="loginModal" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header" style="padding:35px 50px;">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        <h4><span class="glyphicon glyphicon-lock"></span> Login</h4>
                        <h6>Gültige Credentials: admin/admin, Mr.Robot/hallo123, user/password1</h6>
                    </div>
                    <div class="modal-body" style="padding:40px 50px;">
                        <form role="form">
                            <div class="form-group">
                                <label for="usrname"><span class="glyphicon glyphicon-user"></span> Username</label>
                                <input type="text" class="form-control" name="usrname" id="usrname" placeholder="Enter email">
                            </div>
                            <div class="form-group">
                                <label for="pwd"><span class="glyphicon glyphicon-eye-open"></span> Password</label>
                                <input type="text" class="form-control" id="pwd" name="pwd" placeholder="Enter password">
                            </div>
                            <button class="btn btn-success" id="loginButton" onclick="checkLoginInput();"><span class="glyphicon glyphicon-off"></span> Login</button>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-danger btn-default pull-left" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> Cancel</button>
                        <p>Not a member? <a href="#">Sign Up</a></p>
                        <p>Forgot <a href="#">Password?</a></p>
                    </div>
                </div>
            </div>
        </div>
    </body>

<?php
    include "$_SERVER[DOCUMENT_ROOT]/SecWorkbench/SharedSites/_Layout_LowerPart.html";
?>

<script>    
    // mark the site as active in the nav bar
    document.getElementById('tvXSS').className = 'treeview active'; 
    document.getElementById('sbiStoredXSS').className = 'active';
    
    window.onload = function () {
        var title = "Cross Site Scripting - Stored";
        document.getElementById("pageTitle").innerHTML = title;
        document.getElementById("titleDiv").innerHTML = title;
        document.getElementById("pageDescription").innerHTML = "";
    };
</script>