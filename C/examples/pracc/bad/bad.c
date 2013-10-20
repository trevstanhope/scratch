/********************************************************
 * Figure 6-2.  An example of a bad program.		*
 ********************************************************/
#include <stdio.h>
#include <stdlib.h>
int   g, l, h, c, n;
char  line[80];
int main()
{
    while (1) {
        /*Not Really*/
        g = rand() % 100 + 1;
        l = 0;
        h = 100;
        c = 0;
        while (1) {
            printf("Bounds %d - %d\n", l, h);
            printf("Value[%d]? ", c);
            ++c;
            fgets(line, sizeof(line), stdin);
            sscanf(line, "%d", &n);
            if (n == g)
                break;
            if (n < g)
                l = n;
            else
                h = n;
        }
        printf("Bingo\n");
    }
    return (0);
}
