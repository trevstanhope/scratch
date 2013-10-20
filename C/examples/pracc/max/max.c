/*-*/
/********************************************************
 * Question:						*
 *	Why does the following program generate a	*
 *	warning when we compile it to the effect that	*
 *	"counter may be used before set?"		*
 *							*
 *	After all, we set it in the for loop, right?	*
 ********************************************************/
/*+*/
/* warning, spacing is VERY important */

#include <stdio.h>

#define MAX =10

int main()
{
    int  counter;

    for (counter =MAX; counter > 0; --counter)
        printf("Hi there\n");

    return (0);
}
