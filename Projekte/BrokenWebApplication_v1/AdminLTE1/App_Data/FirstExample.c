#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	//flag for authentification check
	int authflag = 0;	

	//buffer for userinput
	char buffer[8];	

	//write userinput to buffer
	strcpy(buffer, argv[1]);		

	char randstr[8];			

	//create random Password
	sprintf(randstr, "%d", rand());		
	
	//check if input = Password
	if(strcmp(randstr,buffer)== 0) 		
	{
		printf("really\n");
		//yeah we got the right pw so we are now authenticated
		authflag = 1; 					
	}
	
	//check for Authentication
	if(authflag != 0)					
	{
		char* Solution = malloc(sizeof(char)*15);
		char* a = "XX"; 
		char* b = "XX"; 
		char* c = "XX"; 
		char* d = "XX"; 
		char* e = "XX"; 
		char* f =  "XX";

		strcat(Solution,a); 
		strcat(Solution,b); 
		strcat(Solution,c); 
		strcat(Solution,d); 
		strcat(Solution,e); 
		strcat(Solution,f);

		printf("Das Lösungswort ist : %s\n", Solution);
	}
	
}
