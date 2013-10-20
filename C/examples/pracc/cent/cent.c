/*-*/
/********************************************************
 * Question:						*
 *	Why does this program print out:		*
 *							*
 *	Celsius:101 Fahrenheit:213			*
 *							*
 *	and nothing else?				*
 ********************************************************/
/*+*/
#include <stdio.h>
/*
 * This program produces a Celsius to Fahrenheit conversion
 *    chart for the numbers 0 to 100.
 */

/* the current Celsius temperature we are working with */
int celsius;
int main() {
    for (celsius = 0; celsius <= 100; ++celsius);
        printf("Celsius:%d Fahrenheit:%d\n",
            celsius, (celsius * 9) / 5 + 32);
    return (0);
}
