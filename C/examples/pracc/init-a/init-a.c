/*-*/
/********************************************************
 * Name: Zero arrays.					*
 *							*
 * Purpose: Shows two ways an array can be cleared.	*
 *							*
 * Usage: Running it is not very useful. Step through 	*
 *		it with the debugger.			*
 ********************************************************/
/*+*/
#define MAX 10	/* Size of the array */
/********************************************************
 * init_array_1 -- Zero out an array                    *
 *                                                      *
 * Parameters                                           *
 *      data -- the array to zero                       *
 ********************************************************/
void init_array_1(int data[])
{
    int  index;

    for (index = 0; index < MAX; ++index)
        data[index] = 0;
}

/********************************************************
 * init_array_2 -- Zero out an array                    *
 *                                                      *
 * Parameters                                           *
 *      data_ptr -- pointer to array to zero            *
 ********************************************************/
void init_array_2(int *data_ptr)
{
    int index;

    for (index = 0; index < MAX; ++index)
        *(data_ptr + index) = 0;
}
int main()
{
    int  array[MAX];

    void init_array_1();
    void init_array_2();

    /* one way of initializing the array */
    init_array_1(array);

    /* another way of initializing the array */
    init_array_1(&array[0]);

    /* works, but the compiler generates a warning */
    init_array_1(&array);

    /* Similar to the first method but  */
    /*    function is different */
    init_array_2(array);

    return (0);
}
