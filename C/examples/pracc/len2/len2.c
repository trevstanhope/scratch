/*-*/
/********************************************************
 * Answer to question 8.1.				*
 *							*
 * For full details, see the book.			*
 ********************************************************/
/*+*/
#include <stdio.h>

int  length(char string[])
{
    int             index;      /* index into the string */

    /*
     * Loop until we reach the end of string character
     */
    for (index = 0; string[index] != '\0'; ++index)
        continue; /* do nothing */
    return (index);
}

int main()
{
     char line[100];	/* Input line from user */

     while (1) {
        printf("Enter line:");
        fgets(line, sizeof(line), stdin);

	printf("Length (including newline) is: %d\n", length(line));
    }
}
