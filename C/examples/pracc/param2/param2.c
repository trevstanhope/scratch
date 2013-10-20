/*-*/
/********************************************************
 * Question: Why is the area wrong?			*
 ********************************************************/
/*+*/
#include <stdio.h>

float area(width, height)
float width;
float height;
{
    return (width * height);
}

int main()
{
    float size = area(3.0 * 2.0);

    printf("Area is %f\n", size);
    return (0);
}
    
