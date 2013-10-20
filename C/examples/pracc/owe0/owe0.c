/*-*/
/********************************************************
 * Question:						*
 *	Why does the following program print out	*
 *	"You owe nothing" even when you owe something?	*
 ********************************************************/
/*+*/
#include <stdio.h>
char  line[80];         /* input line */
int   balance_owed;     /* amount owed */

int main()
{
    printf("Enter number of dollars owed:");
    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d", &balance_owed);

    if (balance_owed = 0)
        printf("You owe nothing.\n");
    else
        printf("You owe %d dollars.\n", balance_owed);

    return (0);
}
