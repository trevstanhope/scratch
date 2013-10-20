/*-*/
/********************************************************
 * Name: parameter					*
 *							*
 * Purpose: Demonstrate the use of pointers and		*
 *		parameter passing.			*
 *							*
 * Usage: Not useful, look at the source or 		*
 *	step through the program using the debugger.	*
 ********************************************************/
/*+*/
#include <stdio.h>
void inc_count(int *count_ptr)
{
    ++(*count_ptr);
}

int main()
{
    int  count = 0;     /* number of times through */

    while (count < 10)
        inc_count(&count);

    return (0);
}
