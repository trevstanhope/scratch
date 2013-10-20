/*-*/
/********************************************************
 * Name: Triangle					*
 *							*
 * Purpose: Computes the area of three triangles.	*
 *							*
 * Usage: Run it and get the results.			*
 ********************************************************/
/*+*/

#include <stdio.h>

/********************************************
 * triangle -- compute area of a triangle   *
 *                                          *
 * Parameters                               *
 *   width -- width of the triangle         *
 *   height -- height of the triangle       *
 *                                          *
 * Returns                                  *
 *   area of the triangle                   *
 ********************************************/
float triangle(float width, float height)
{
    float area;     /* Area of the triangle */

    area = width * height / 2.0;
    return (area);
}

int main()
{
    printf("Triangle #1 %f\n", triangle(1.3, 8.3));
    printf("Triangle #2 %f\n", triangle(4.8, 9.8));
    printf("Triangle #3 %f\n", triangle(1.2, 2.0));
    return (0);
}

