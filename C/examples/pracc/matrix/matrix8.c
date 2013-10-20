/*-*/
/********************************************************
 * Name: Init matrix 					*
 *							*
 * An example of how to initialize a matrix.		*
 ********************************************************/
/*+*/
#define X_SIZE 60
#define Y_SIZE 30

int matrix[X_SIZE][Y_SIZE];

/********************************************************
 * init_matrix -- set every element of matrix to -1	*
 ********************************************************/
#define init_matrix() \
    memset(matrix, -1, sizeof(matrix));
