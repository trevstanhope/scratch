/*-*/
/********************************************************
 * Question:						*
 *	Why does the following program print 		*
 *	"John @#$24" instead of John Doe?		*
 *	(Your results may vary.)			*
 ********************************************************/
/*+*/
#include <stdio.h>
#include <string.h>

char first[100];	/* First name of the person */
char last[100];		/* Last name of the person */

/* First and last name combined */
char full[100];

int main() {
    strcpy(first, "John");
    strcpy(last, "Doe");

    strcpy(full, first);
    strcat(full, ' ');
    strcat(full, last);

    printf("The name is %s\n", full);
    return (0);
}
