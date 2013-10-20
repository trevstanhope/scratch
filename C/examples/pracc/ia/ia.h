/********************************************************
 * definitions for the infinite array (ia) package      *
 *                                                      *
 * An infinite array is an array whose size can grow    *
 * as needed.  Adding more elements to the array        *
 * will just cause it to grow.                          *
 *------------------------------------------------------*
 * struct infinite_array                                *
 *      used to hold the information for an infinite    *
 *      array                                           *
 *------------------------------------------------------*
 * Routines                                             *
 *                                                      *
 *      ia_init -- initialize the array.		*
 *      ia_store -- store an element in the array       *
 *      ia_get -- get an element from the array		*
 ********************************************************/

/* number of elements to store in each cell of the infinite array */
#define BLOCK_SIZE      10
	
struct infinite_array {
    /* the data for this block */
    float   data[BLOCK_SIZE];       

    /* pointer to the next array */
    struct infinite_array *next;
};

/********************************************************
 * ia_init -- Initialize the infinite array.		*
 *							*
 * Parameters						*
 *	array_ptr -- The array to initialize		*
 ********************************************************/
#define ia_init(array_ptr)      {(array_ptr)->next = NULL;}

/********************************************************
 * ia_get -- get an element from an infinite array.     *
 *                                                      *
 * Parameters                                           *
 *      array_ptr -- pointer to the array to use        *
 *      index   -- index into the array                 *
 *                                                      *
 * Returns                                              *
 *      the value of the element                        *
 *							*
 * Note: It is possible to get an element that		*
 *	has not previously been stored.  The value	*
 *	of any uninitialized elements is zero.		*
 ********************************************************/
extern int ia_get(struct infinite_array *array_ptr, int index);

/********************************************************
 * ia_store -- store an element into an infinite array. *
 *                                                      *
 * Parameters                                           *
 *      array_ptr -- pointer to the array to use        *
 *      index   -- index into the array                 *
 *      store_data -- data to store                     *
 ********************************************************/
extern void  ia_store(struct infinite_array * array_ptr, 
    int index, int store_data);
