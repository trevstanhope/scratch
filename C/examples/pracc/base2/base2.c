/********************************************************
 * Database -- A very simple database program to        *
 *              lookup names in a hardcoded list.       *
 *                                                      *
 * Usage:                                               *
 *      database [-S<file>]                             *
 *                                                      *
 *      -S<file>        Specify save file for           *
 *                      debugging purposes              *
 *                                                      *
 *              Program will ask you for a name.        *
 *              Enter the name; it will tell you if     *
 *              it is the list.                         *
 *                                                      *
 *              A blank name terminates the program.    *
 ********************************************************/
#include <stdio.h>
#include <stdlib.h>

FILE *save_file = NULL; /* Save file if any */
char *extended_fgets(char *, int, FILE *);

int main(int argc, char *argv[])
{
    char name[80];      /* a name to lookup */
    char *save_file_name; /* Name of the save file */

    int lookup(char const *const name); /* lookup a name */

    while ((argc > 1) && (argv[1][0] == '-')) {
        switch (argv[1][1]) {
	    /* -S<file>  Specify a save file */
            case 'S':
                save_file_name = &argv[1][2];
                save_file = fopen(save_file_name, "w");
                if (save_file == NULL) 
                    fprintf(stderr,
                        "Warning:Unable to open save file %s\n",
                        save_file_name);
                break;
            default:
                fprintf(stderr,"Bad option: %s\n", argv[1]);
                exit (8);
        }
        --argc;
        ++argv;
    }    


    while (1) {
        printf("Enter name: ");
        extended_fgets(name, sizeof(name), stdin);

        /* ... Rest of program ... */
    }
}
