#include <stdio.h>

int main()
{
    /* Get the square of a number */
    int i = square(5);

    printf("i is %d\n", i);
    return (0);
}

float square(s)
int s;
{
    return (s * s);
}

