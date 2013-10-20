#include <stdio.h>

int sum(i1, i2, i3)
{
   int i1;
   int i2;
   int i3;

   return (i1 + i2 + i3);
}

int main()
{
    printf("Sum is %d\n", sum(1, 2, 3));
    return (0);
}
