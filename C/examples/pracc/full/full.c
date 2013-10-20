/*-*/
/********************************************************
 * Name:						*
 *	concat						*
 *							*
 * Purpose:						*
 *	Demonstrates how to put strings together using	*
 *	strcat.						*
 *							*
 * Usage:						*
 * 	Run it and see my full name.			*
 *							*
 * Notes:						*
 *	Don't try to pronounce the last name.		*
 ********************************************************/
/*+*/
#include <string.h>
#include <stdio.h>

char first[100];        /* first name */
char last[100];         /* last name */
char full_name[200];    /* full version of first and last name */

int main()
{
    strcpy(first, "Steve");       /* Initialize first name */
    strcpy(last, "Oualline");     /* Initialize last name */

    strcpy(full_name, first);     /* full = "Steve" */
    /* Note: strcat not strcpy */
    strcat(full_name, " ");       /* full = "Steve " */
    strcat(full_name, last);      /* full = "Steve Oualline" */

    printf("The full name is %s\n", full_name);
    return (0);
}
