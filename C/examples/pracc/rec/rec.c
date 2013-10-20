/*-*/
/********************************************************
 * Question: The following program fails to compile	*
 * because we didn't define the variable "number."	*
 * But "number" is a parameter to a macro, and shouldn't*
 * need to be defined.  What's going on?		*
 ********************************************************/
/*+*/
#include <stdio.h>
#define RECIPROCAL (number) (1.0 / (number))

int main()
{
    float   counter;	/* Counter for our table */

    for (counter = 0.0; counter < 10.0; 
	 counter += 1.0) {

        printf("1/%f = %f\n", 
	       counter, RECIPROCAL(counter));
    }
    return (0);
}
