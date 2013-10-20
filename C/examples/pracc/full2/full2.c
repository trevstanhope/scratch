/*-*/
/********************************************************
 * Name:						*
 *	full name (V2)					*
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
 * Note: This version does not contain the bug found	*
 *	in program 4_6.c
 ********************************************************/
/*+*/
#include <stdio.h>
#include <string.h>

char first[100];        /* first name of person we are working with */
char last[100];         /* His last name */

/* First and last name of the person (computed) */
char full[100];         

int main() {
    printf("Enter first name: ");
    fgets(first, sizeof(first), stdin);
    /* trim off last character */
    first[strlen(first)-1] = '\0';

    printf("Enter last name: ");
    fgets(last, sizeof(last), stdin);
    /* trim off last character */
    last[strlen(last)-1] = '\0';

    strcpy(full, first);
    strcat(full, " ");
    strcat(full, last);

    printf("The name is %s\n", full);
    return (0);
}
