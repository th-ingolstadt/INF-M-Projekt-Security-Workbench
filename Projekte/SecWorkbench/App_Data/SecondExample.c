
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(int argc, char *argv[])
{
	//flag for authentification check
	int authflag = 1111;
	int checkForHack = -559038737;

	//buffer for userinput
	char buffer[20];

	//write userinput to buffer
	strcpy(buffer, argv[1]);

	char randstr[20];
	srand ( time(NULL) );
	
	//create random Password
	sprintf(randstr, "%d", rand());

	//check if input = Password
	if(strcmp(randstr,buffer)== 0)
	{
		printf("really\n");
		//yeah we got the right pw so we are now authenticated
		authflag = 1;
	}

	if(checkForHack == -559038737)
	{
		//check for Authentication
		if(authflag != 1111)
		{
			printf("Das Passwort ist: %s\n", randstr);
			
			printf("CheckForHack hat den Wert: %d\n", checkForHack);

			printf("Der Eingabepuffer ist: %s\n", buffer);

			printf("Das Authflag hat den Wert: %d\n", authflag);
		}
	}
	else
	{
		printf("CheckForHack hat den Wert: %d\n", checkForHack);
		printf("Hacker detected; Exit program!\n");
	}

}
