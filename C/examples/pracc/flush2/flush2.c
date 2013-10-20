/*-*/
/********************************************************
 * Name: Divide error.					*
 *							*
 * This program contains a divide error.		*
 *							*
 * "printf" calls have been added to isolate the problem*
 ********************************************************/
/*+*/
#include <stdio.h>
int main()
{
    int i,j;    /* two random integers */

    i = 1;
    j = 0;

    printf("Starting\n");
    fflush(stdout);

    printf("Before divide...");
    fflush(stdout);

    i = i / j;  /* divide by zero error */

    printf("After\n");
    fflush(stdout);
    return(0);
}
