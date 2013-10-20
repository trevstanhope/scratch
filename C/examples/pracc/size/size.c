/*-*/
/********************************************************
 * Question:						*
 *	Why does the program compute the wrong value 	*
 *	"size?"						*
 ********************************************************/
/*+*/
#include <stdio.h>

#define SIZE    10;
#define FUDGE   SIZE -2;
int main()
{
    int size;/* size to really use */
    
    size = FUDGE;
    printf("Size is %d\n", size);
    return (0);
}
