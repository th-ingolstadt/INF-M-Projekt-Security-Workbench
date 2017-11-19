#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
			char* Solution = malloc(sizeof(char)*15);
			char* a = "XX"; 
			char* b = "XX"; 
			char* c = "XX"; 
			char* d = "XX"; 
			char* e = "XX";

			strcat(Solution,a); 
			strcat(Solution,b); 
			strcat(Solution,c); 
			strcat(Solution,d); 
			strcat(Solution,e);
			printf("Das Lösungswort ist: %s\n", Solution);
		}
	}
	else
	{
		printf("Hacker detected; Exit program!\n");
	}
	
}
