/*-*/
/********************************************************
 * Name: Init matrix 					*
 *							*
 * An example of how to initialize a matrix.		*
 ********************************************************/
/*+*/
#include <memory.h>	/* Gets definition of memset */
#define X_SIZE 60
#define Y_SIZE 30

int matrix[X_SIZE][Y_SIZE];
/********************************************************
 * init_matrix -- set every element of matrix to -1	*
 ********************************************************/
void init_matrix(void)
{
    memset(matrix, -1, sizeof(matrix));
}
