/*-*/
/********************************************************
 * Question:						*
 *	Why does memset successfully initialize		*
 *	the matrix to -1, but when we try to use it to 	*
 *	set every element to 1, we fail?		*
 ********************************************************/
/*+*/
#define X_SIZE 60
#define Y_SIZE 30

int matrix[X_SIZE][Y_SIZE];

#define init_matrix() \
    memset(matrix, 1, sizeof(matrix));
