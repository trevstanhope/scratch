/*-*/
/********************************************************
 * Name:						*
 *	print terms					*
 *							*
 * Usage:						*
 *	Run it and get some simple answers.		*
 *							*
 * Purpose:						*
 *	Demonstrates printing the results of simple	*
 *	equations.					*
 ********************************************************/
/*+*/
#include <stdio.h>

int term;       /* term used in two expressions */
int main()
{
    term = 3 * 5;
    printf("Twice %d is %d\n", term, 2*term);
    printf("Three times %d is %d\n", term, 3*term);
    return (0);
}
