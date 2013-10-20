/*-*/
/********************************************************
 * Name: Init matrix 					*
 *							*
 * An example of how to initialize a matrix.		*
 ********************************************************/
/*+*/
#define X_SIZE 60
#define Y_SIZE 32

int matrix[X_SIZE][Y_SIZE];

/********************************************************
 * init_matrix -- set every element of matrix to -1	*
 ********************************************************/
void init_matrix(void)
{
    register int x,y;    /* current element to zero */

    for (y = 0; y < Y_SIZE; ++y) {
        for (x = 0; x < X_SIZE; ++x) {
            matrix[x][y] = -1;
        }
    }
}
