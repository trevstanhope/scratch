/*-*/
/********************************************************
 * Question:						*
 *	Why is an incorrect result printed?		*
 ********************************************************/
/*+*/
#include <stdio.h>

float result;	/* Result of the divide */

int main()
{
    result = 7.0 / 22.0;

    printf("The result is %d\n", result);
    return (0);
}
