#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <readString.h>


int main(void){

	readText myRead;

	string testStr = "Hello world";
	myRead.readStr(testStr);
	return 0;
}