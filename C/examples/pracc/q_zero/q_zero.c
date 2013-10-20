/*-*/
/********************************************************
 * Question:						*
 *	Why does the following program print:		*
 *	"The value of 1/3 is 0.0" ?			*
 ********************************************************/
/*+*/
#include <stdio.h>

float answer;	/* The result of our calculation */

int main()
{
    answer = 1/3;
    printf("The value of 1/3 is %f\n", answer);
    return (0);
}
