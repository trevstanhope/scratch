/*-*/
/********************************************************
 * Question: Why does this routine work sometimes and	*
 *		crash others?				*
 ********************************************************/
/*+*/
#include <stdio.h>
#include <string.h>

struct linked_list {
   struct linked_list *next_ptr;	/* Next item in the list */
   char *data;				/* Data for the list */
};

struct linked_list *first_ptr;
/********************************************************
 * find -- look for a data item in the list             *
 *                                                      *
 * Parameters                                           *
 *      name -- name to look for in the list            *
 *                                                      *
 * Returns                                              *
 *      1 if name is found                              *
 *      0 if name is not found                          *
 ********************************************************/
int find(char *name)
{
    /* current structure we are looking at */
    struct linked_list *current_ptr;

    current_ptr = first_ptr;

    while ((strcmp(current_ptr->data, name) != 0) &&
           (current_ptr != NULL))
        current_ptr = current_ptr->next_ptr;

    /*
     * If current_ptr is null, we fell off the end of the list and
     * didn't find the name
     */
    return (current_ptr != NULL);
}
