/*-*/
/********************************************************
 * Program: Array initialization			*
 *							*
 * Purpose: Show how to initialize an array.		*
 *							*
 * Usage: Run the program and look at the results.	*
 *							*
 * Note: Same as the previous program but uses 		*
 *	pointer arithmetic instead of array indices.	*
 ********************************************************/
/*+*/
#include <stdio.h>

int array[] = {4, 5, 8, 9, 8, 1, 0, 1, 9, 3};
int *array_ptr;

int main()
{
    array_ptr = array;

    while ((*array_ptr) != 0)
        ++array_ptr;

    printf("Number of elements before zero %d\n",
                  array_ptr - array);
    return (0);
}
