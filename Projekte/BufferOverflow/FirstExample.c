#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	//flag for authentification check
	int authflag = 0;			
	char buffer[8];			//buffer for userinput
	strcpy(buffer, argv[1]);		//write userinput to buffer

	char randstr[8];			
	sprintf(randstr, "%d", rand());		//create random Password
	
	if(strcmp(randstr,buffer)== 0) 		//check if input = Password
	{
		printf("really\n");
		authflag = 1; 					//yeah we got the right pw so we are now authenticated
	}
	
	if(authflag != 0)					//check for Authentication
	{
		char* Solution = malloc(sizeof(char)*15);
		//char* a = "XX"; char* b = "XX"; char* c = "XX"; char* d = "XX"; char* e = "XX"; char* f =  "XX";
		char* a = "DE"; char* b = "12"; char* c = "34"; char* d = "56"; char* e = "67"; char* f =  "78";

		strcat(Solution,a); strcat(Solution,b); strcat(Solution,c); strcat(Solution,d); strcat(Solution,e); strcat(Solution,f);
		
		printf("Zugriff gewaehrt! Die Kontodaten von Max Mustermann sind: %s\n", Solution);
	}else printf("Ungueltige Eingabe! -> Zugriff verweigert!\n");
	
}
