#include <stdio.h>

float area(width, height)
int width;
float height;
{
    return (width * height);
}

int main()
{
    float size = area(3.0, 2);

    printf("Area is %f\n", size);
    return (0);
}
    
