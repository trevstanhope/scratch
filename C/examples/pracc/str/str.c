/*-*/
/********************************************************
 * Name:						*
 *	string						*
 *							*
 * Purpose:						*
 *	Demonstrate how to use strcpy (string copy)	*
 *							*
 * Usage:						*
 * 	Run it and find out the name of "Sam"		*
 ********************************************************/
/*+*/
#include <string.h>
#include <stdio.h>
char name[30];    /* First name of someone */
int main()
{
    strcpy(name, "Sam");    /* Initialize the name */
    printf("The name is %s\n", name);
    return (0);
}
