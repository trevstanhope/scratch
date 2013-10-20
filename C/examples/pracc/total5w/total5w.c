/*-*/
/********************************************************
 * Program: ADD5 -- Adds up 5 numbers.			*
 *							*
 * Usage:						*
 *	Run it, type in 5 numbers and get a total.	*
 ********************************************************/
/*+*/
#include <stdio.h>

int total;      /* total of all the numbers */
int current;    /* current value from the user */
int counter;    /* while loop counter */

char line[80];  /* Line from keyboard */

int main() {
    total = 0;

    counter = 0;
    while (counter < 5) {
        printf("Number? ");

        fgets(line, sizeof(line), stdin);
        sscanf(line, "%d", &current);
        total += current;

        ++counter;
    }
    printf("The grand total is %d\n", total);
    return (0);
}
