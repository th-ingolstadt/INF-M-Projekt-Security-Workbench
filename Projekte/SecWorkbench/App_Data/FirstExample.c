
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(int argc, char *argv[80])
{
    //flag for authentication check
    int authflag = 0;
    //buffer for solution word
    char solution[21];
    //buffer for user input
    char buffer[8];

    //write user input to buffer
    strcpy(buffer, argv[1]);

    char randstr[8];
    srand ( time(NULL) );

    //create random Password
    sprintf(randstr, "%d", rand() );

    //check if input = Password
    if(strcmp(randstr,buffer)== 0)
    {
        printf("Really...?\n");
        //yeah we got the right pw so we are now authenticated
        authflag = 1;
    }

    //check for Authentication
    if(authflag != 0)
    {
        printf("Das Passwort ist: %s\n", randstr);

        printf("Der Eingabepuffer ist: %s\n", buffer);

        printf("Das Authflag hat den Wert: %d\n", authflag);

        printf("Das Lösungswort ist : %s\n", solution);
    }
    else
    {
        printf("Fehler: Login fehlgeschlagen!");
    }
}
