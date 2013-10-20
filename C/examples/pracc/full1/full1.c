/*-*/
/********************************************************
 * Name:						*
 *	full name (V1)					*
 *							*
 * Purpose:						*
 *	Get first and last name and print them 		*
 *	together.					*
 *							*
 * Usage:						*
 *	Run the program.				*
 *	Type in the first name.				*
 *	Type in the second name.			*
 *	Get the result.					*
 *							*
 * BUG: This program contains a bug that causes		*
 *	the names to appear on separate lines.		*
 ********************************************************/
/*+*/
#include <stdio.h>
#include <string.h>

char first[100];        /* first name of person we are working with */
char last[100];         /* His last name */

/* First and last name of the person (computed) */
char full[200];         

int main() {
    printf("Enter first name: ");
    fgets(first, sizeof(first), stdin);

    printf("Enter last name: ");
    fgets(last, sizeof(last), stdin);

    strcpy(full, first);
    strcat(full, " ");
    strcat(full, last);

    printf("The name is %s\n", full);
    return (0);
}
