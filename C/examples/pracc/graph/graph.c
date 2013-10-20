/*-*/
/********************************************************
 * Name: Graph						*
 *							*
 * Purpose:						*
 *	Show how bitmapped graphics may be used.	*
 *							*
 * Algorithm: Defines a bit array for graphics, 	*
 *	draws a diagonal line across our array and	*
 *	then prints the result.				*
 *							*
 * Usage:						*
 *	Run it and look at the picture.			*
 ********************************************************/
/*+*/
#include <stdio.h>

#define X_SIZE 40  /* size of array in the X direction */
#define Y_SIZE 60  /* size of the array in Y direction */
/*
 * We use X_SIZE/8 since we pack 8 bits per byte
 */
char graphics[X_SIZE / 8][Y_SIZE];   /* the graphics data */

#define SET_BIT(x,y) graphics[(x)/8][y] |= (0x80 >>((x)%8))

int main()
{
    int   loc;        /* current location we are setting */
    void  print_graphics(void); /* print the data */

    for (loc = 0; loc < X_SIZE; ++loc)
        SET_BIT(loc, loc);

    print_graphics();
    return (0);
}
/********************************************************
 * print_graphics -- print the graphics bit array       *
 *              as a set of X and .'s.                  *
 ********************************************************/
void print_graphics(void)
{
    int x;              /* current x BYTE */
    int y;              /* current y location */
    unsigned int bit;   /* bit we are testing in the current byte */

    for (y = 0; y < Y_SIZE; ++y) {
        /* Loop for each byte in the array */
        for (x = 0; x < X_SIZE / 8; ++x) {
            /* Handle each bit */
            for (bit = 0x80; bit > 0; bit = (bit >> 1)) {
                if ((graphics[x][y] & bit) != 0)
                    printf("X");
                else
                    printf(".");
            }
        }
        printf("\n");
    }
}
