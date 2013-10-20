/*-*/
/********************************************************
 * Question: Why does this program loop forever?	*
 ********************************************************/
/*+*/
#include <stdio.h>
int main()
{
    short int i;	/* Loop counter */
    signed char ch;	/* Loop counter of another kind */

    /* Works */
    for (i = 0x80; i != 0; i = (i >> 1)) {
	printf("i is %x (%d)\n", i, i);
    }

    /* Fails */
    for (ch = 0x80; ch != 0; ch = (ch >> 1)) {
	printf("ch is %x (%d)\n", ch, ch);
    }
    return (0);
}
