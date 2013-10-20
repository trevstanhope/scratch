/*-*/
/********************************************************
 * Program: Array initialization			*
 *							*
 * Purpose: Show how to initialize an array.		*
 *							*
 * Usage: Run the program and look at the results.	*
 ********************************************************/
/*+*/
#include <stdio.h>

int array[] = {4, 5, 8, 9, 8, 1, 0, 1, 9, 3};
int index;

int main()
{
    index = 0;
    while (array[index] != 0)
        ++index;

    printf("Number of elements before zero %d\n",
                  index);
    return (0);
}
