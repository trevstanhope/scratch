/*-*/
/********************************************************
 * Question:						*
 *	The following program can't open the file no	*
 *	matter what name we give it. Why?		*
 ********************************************************/
/*+*/
#include <stdio.h>
#include <stdlib.h>	

int main()
{
    char            name[100];  /* name of the file to use  */
    FILE           *in_file;    /* file for input */

    printf("Name? ");
    fgets(name, sizeof(name), stdin);

    in_file = fopen(name, "r");
    if (in_file == NULL) {
        fprintf(stderr, "Could not open file\n");
        exit(8);
    }
    printf("File found\n");
    fclose(in_file);
    return (0);
}
