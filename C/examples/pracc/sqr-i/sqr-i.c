/*-*/
/********************************************************
 * Name: Square generator				*
 *							*
 * Purpose: Generate a square table.			*
 *							*
 * Usage: Run it and get a table.			*
 *							*
 * Notes: Corrected version of the previous program.	*
 ********************************************************/
/*+*/
#include <stdio.h>
#define SQR(x) ((x) * (x))

int main()
{
    int counter;    /* counter for loop */

    counter = 0;

    while (counter < 5)
        printf("x %d square %d\n", counter, SQR(++counter));

    return (0);
}
