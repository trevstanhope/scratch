/*-*/
/********************************************************
 * Name: Divide error.					*
 *							*
 * This program contains a bug which causes a divide 	*
 * by zero error.					*
 * 							*
 * However due to buffering the "Before divide" message	*
 * may not apper.					*
 *							*
 * Note: Don't code like this.				*
 ********************************************************/
/*+*/
#include <stdio.h>
int main()
{
    int i,j;    /* two random integers */

    i = 1;
    j = 0;
    printf("Starting\n");
    printf("Before divide...");
    i = i / j;  /* divide by zero error */
    printf("After\n");
    return(0);
}
