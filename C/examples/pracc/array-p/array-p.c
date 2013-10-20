/*-*/
/********************************************************
 * Name: Address Demo					*
 *							*
 * Purpose: Demonstrate how array addressing and	*
 *	pointer arithmetic are linked.			*
 *							*
 * Usage: Run the program and see the results.		*
 ********************************************************/
/*+*/
#include <stdio.h>

#define ARRAY_SIZE 10   /* Number of characters in array */
/* Array to print */
char array[ARRAY_SIZE] = "0123456789";   

int main()
{
    int index;  /* Index into the array */

    for (index = 0; index < ARRAY_SIZE; ++index) {
        printf("&array[index]=0x%p (array+index)=0x%p array[index]=0x%x\n",
            &array[index], (array+index), array[index]);
    }
    return (0);
}
