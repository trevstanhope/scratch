/********************************************************
 * gen -- Generate a bunch of random data		*
 *							*
 * Usage:						*
 *	gen						*
 *							*
 * Outputs 500 lines of numbers from 1 to 40		*
 ********************************************************/
#include <stdlib.h>
#include <stdio.h>

const int MAX_LINES = 500;	/* Number of lines to write */
const int MAX = 40;		/* Maximum number */
int main()
{
    int index;	/* Loop index */

    for (index = 0; index < MAX_LINES; ++index) {
       int number;	/* A random number */

       number = rand();
       printf("%d\n", (number % (MAX-1)) +1);
    }
    return (0);
}

