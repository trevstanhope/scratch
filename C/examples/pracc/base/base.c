/*-*/
/********************************************************
 * This is an example of a database program before 	*
 * we add debugging and recording code to it.		*
 ********************************************************/
/*+*/
/********************************************************
 * Database -- A very simple database program to        *
 *              look up names in a hardcoded list.      *
 *                                                      *
 * Usage:                                               *
 *      database                                        *
 *              Program will ask you for a name.        *
 *              Enter the name; it will tell you if     *
 *              it is the list.                         *
 *                                                      *
 *              A blank name terminates the program.    *
 ********************************************************/
#define STRING_LENGTH 80        /* Length of typical string */
#include <stdio.h>
#include <string.h>

int main()
{
    char name[STRING_LENGTH];   /* a name to lookup */

    int lookup(char const *const name); /* lookup a name */

    while (1) {
        printf("Enter name: ");
        fgets(name, sizeof(name), stdin);

        /* Check for blank name  */
        /* (remember 1 character for newline) */
        if (strlen(name) <= 1)
            break;

        /* Get rid of newline */
        name[strlen(name)-1] = '\0';

        if (lookup(name)) 
            printf("%s is in the list\n", name);
        else
            printf("%s is not in the list\n", name);
    }
    return (0);
}
/********************************************************
 * lookup -- lookup a name in a list                    *
 *                                                      *
 * Parameters                                           *
 *      name -- name to lookup                          *
 *                                                      *
 * Returns                                              *
 *      1 -- name in the list                           *
 *      0 -- name not in the list                       *
 ********************************************************/
int lookup(char const *const name)
{
    /* List of people in the database */
    /* Note: Last name is a NULL for end of list */
    static char *list[] = {
        "John",
        "Jim",
        "Jane",
        "Clyde",
        NULL
    };

    int index;          /* index into list */

    for (index = 0; list[index] != NULL; ++index) {
        if (strcmp(list[index], name) == 0)
            return (1);
    }
    return (0);
}
