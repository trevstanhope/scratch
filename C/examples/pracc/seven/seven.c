/*-*/
/********************************************************
 * Question: 						*
 * 	This program is supposed to count the number	*
 *	of threes and sevens in ourdata, but it gives	*
 *	wrong answers.  Why?				*
 ********************************************************/
/*+*/
#include <stdio.h>
char line[100];     /* line of input */
int seven_count;    /* number of sevens in the data */
int data[5];        /* the data to count 3 and 7 in */
int three_count;    /* the number of threes in the data */
int index;  	    /* index into the data */

int main() {

    seven_count = 0;
    three_count = 0;
    printf("Enter 5 numbers\n");
    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d %d %d %d %d", 
        &data[1], &data[2], &data[3],
        &data[4], &data[5]);

    for (index = 1; index <= 5; ++index) {

        if (data[index] == 3)
            ++three_count;

        if (data[index] == 7)
	    ++seven_count;
    }
    printf("Threes %d Sevens %d\n", 
            three_count, seven_count);
    return (0);
}
