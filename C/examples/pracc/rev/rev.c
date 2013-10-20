/*-*/
/********************************************************
 * Name:						*
 *	print3						*
 *							*
 * Purpose						*
 *	Prints 3 characters forward and backward to	*
 *	demonstrate character printing.			*
 *							*
 * Usage:						*
 *	Run it and see the results.			*
 ******************************************************/
/*+*/
#include <stdio.h>

char char1;     /* first character */
char char2;     /* second character */
char char3;     /* third character */

int main()
{
    char1 = 'A';
    char2 = 'B';
    char3 = 'C';
    printf("%c%c%c reversed is %c%c%c\n",
        char1, char2, char3,
        char3, char2, char1);
    return (0);
}
