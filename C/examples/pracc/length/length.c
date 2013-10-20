/*-*/
/********************************************************
 * Name:						*
 *	length						*
 * 							*
 * Purpose:						*
 *	Computes the length of a line			*
 *							*
 * Usage:						*
 *	Run it, type in a line, get the length.		*
 *							*
 * Limitations						*
 *	Line must be 99 characters long or less		*
 ********************************************************/
/*+*/
#include <string.h>
#include <stdio.h>

char line[100];	/* Line we are looking at */

int main()
{
    printf("Enter a line: ");
    fgets(line, sizeof(line), stdin);

    printf("The length of the line is: %d\n", strlen(line));
    return (0);
}
