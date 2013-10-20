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
