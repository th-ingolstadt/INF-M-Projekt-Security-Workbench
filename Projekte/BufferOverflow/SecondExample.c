#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	//flag for authentification check
	int authflag = 1111;
	int checkForHack = -559038737;	
	char buffer[20];			//buffer for userinput
	strcpy(buffer, argv[1]);	//write userinput to buffer

	char randstr[20];			
	sprintf(randstr, "%d", rand());		//create random Password
	
	if(strcmp(randstr,buffer)== 0) 		//check if input = Password
	{
		printf("really\n");
		authflag = 1; 					//yeah we got the right pw so we are now authenticated
	}

	if(checkForHack == -559038737)
	{
		if(authflag != 1111)					//check for Authentication
		{
		char* Solution = malloc(sizeof(char)*15);
		char* a = "XX"; char* b = "XX"; char* c = "XX"; char* d = "XX"; char* e = "XX";

		strcat(Solution,a); strcat(Solution,b); strcat(Solution,c); strcat(Solution,d); strcat(Solution,e);
			printf("Das Lösungswort ist: %s\n", Solution);
		}
	}
	else
	{
		printf("Hacker detected; Exit program!\n");
	}
	
}
