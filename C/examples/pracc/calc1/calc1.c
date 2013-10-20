/*-*/
/********************************************************
 * Name: Calculator (Version 0 -- prototype)		*
 *							*
 * Purpose:						*
 *	Act like a simple 4 function calculator.	*
 *							*
 * Usage:						*
 *	Run the program.				*
 *	Type in an operator (+ - * /) and a number.	*
 *	The operaton will be performed on the current	*
 *	result and a new result displayed.		*
 *							*
 * Note:						*
 *	This is the first attempt at doing this program.*
 *	It only works for + and because of a bug, even	*
 *	that fails.					*
 ********************************************************/
/*+*/
#include <stdio.h>
char  line[100];/* line of data from the input */
int   result;   /* the result of the calculations */
char  operator; /* operator the user specified */
int   value;    /* value specified after the operator */

int main()
{
    result = 0; /* initialize the result */

    /* Loop forever (or till we hit the break statement) */
    while (1) {
        printf("Result: %d\n", result);

        printf("Enter operator and number: ");
        fgets(line, sizeof(line), stdin);
        sscanf(line, "%c %d", &operator, &value);

        if (operator = '+') {
            result += value;
        } else {
            printf("Unknown operator %c\n", operator);
        }
    }
}
