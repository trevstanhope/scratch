/*-*/
/********************************************************
 * Question: Why does this program tell us that the	*
 *	answer is 47 when we know that it should be	*
 *	144?						*
 ********************************************************/
/*+*/
#include <stdio.h>

#define FIRST_PART      7 
#define LAST_PART       5 
#define ALL_PARTS       FIRST_PART + LAST_PART 

int main() { 
    printf("The square of all the parts is %d\n", 
	ALL_PARTS * ALL_PARTS); 
    return (0);
} 
