/*-*/
/********************************************************
 * Question:						*
 *	Why does the following program think		*
 *	everything is two?  				*
 ********************************************************/
/*+*/
#include <stdio.h>
int main()
{
    char line[80];
    int number;

    printf("Enter a number: ");

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d", &number);

    if (number =! 2) 
	printf("Number is not two\n");
    else
	printf("Number is two\n");

    return (0);
}
