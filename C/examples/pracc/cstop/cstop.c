/*-*/
/********************************************************
 * point_color --  gets the color of a single point	*
 *							*
 * Parameters						*
 *	point_number -- index of the point		*
 *							*
 * Returns						*
 *	RGB version of the color.			*
 ********************************************************/
/*+*/
extern float lookup(int index);

float point_color(int point_number)
{
    float correction;  /* color correction factor */
    extern float red,green,blue;/* current colors */

    correction = lookup(point_number);
    return (red*correction * 100.0 + 
            blue*correction * 10.0 +
            green*correction);
}
