/********************************************************
 * words -- scan a file and print out a list of words   *
 *              in ASCII order.                         *
 *                                                      *
 * Usage:                                               *
 *      words <file>                                    *
 ********************************************************/
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>    

struct node {
    struct node    *left;       /* tree to the left */
    struct node    *right;      /* tree to the right */
    char           *word;       /* word for this tree */
};

/* the top of the tree */
static struct node *root = NULL;

/********************************************************
 * memory_error -- write error and die                  *
 ********************************************************/
void memory_error(void)
{
    fprintf(stderr, "Error:Out of memory\n");
    exit(8);
}

/********************************************************
 * save_string -- save a string on the heap             *
 *                                                      *
 * Parameters                                           *
 *      string -- string to save                        *
 *                                                      *
 * Returns                                              *
 *      pointer to malloc-ed section of memory with     *
 *      the string copied into it.                      *
 ********************************************************/
char *save_string(char *string)
{
    char *new_string;   /* where we are going to put string */

    new_string = malloc((unsigned) (strlen(string) + 1));

    if (new_string == NULL)
        memory_error();

    strcpy(new_string, string);
    return (new_string);
}
/********************************************************
 * enter -- enter a word into the tree                  *
 *                                                      *
 * Parameters                                           *
 *      node -- current node we are looking at          *
 *      word -- word to enter                           *
 ********************************************************/
void enter(struct node **node, char *word)
{
    int  result;        /* result of strcmp */

    char *save_string(char *);  /* save a string on the heap */

    /* 
     * If the current node is null, we have reached the bottom
     * of the tree and must create a new node.
     */
    if ((*node) == NULL) {

	/* Allocate memory for a new node */
        (*node) = malloc(sizeof(struct node));
        if ((*node) == NULL)
            memory_error();

	/* Initialize the new node */
        (*node)->left = NULL;
        (*node)->right = NULL;
        (*node)->word = save_string(word);
	return;
    }
    /* Check to see where the word goes */
    result = strcmp((*node)->word, word);

    /* The current node already contains the word, no entry necessary */
    if (result == 0)
        return;

    /* The word must be entered in the left or right sub-tree */
    if (result < 0)
        enter(&(*node)->right, word);
    else
        enter(&(*node)->left, word);
}
/********************************************************
 * scan -- scan the file for words                      *
 *                                                      *
 * Parameters                                           *
 *      name -- name of the file to scan                *
 ********************************************************/
void scan(char *name)
{
    char word[100];     /* word we are working on */
    int  index;         /* index into the word */
    int  ch;            /* current character */
    FILE *in_file;      /* input file */

    in_file = fopen(name, "r");
    if (in_file == NULL) {
        fprintf(stderr, "Error:Unable to open %s\n", name);
        exit(8);
    }
    while (1) {
        /* scan past the whitespace */
        while (1) {
            ch = fgetc(in_file);

            if (isalpha(ch) || (ch == EOF))
                break;
        }

        if (ch == EOF)
            break;

        word[0] = ch;
        for (index = 1; index < sizeof(word); ++index) {
            ch = fgetc(in_file);
            if (!isalpha(ch))
                break;
            word[index] = ch;
        }
        /* put a null on the end */
        word[index] = '\0';

        enter(&root, word);
    }
    fclose(in_file);
}
/********************************************************
 * print_tree -- print out the words in a tree          *
 *                                                      *
 * Parameters                                           *
 *      top -- the root of the tree to print            *
 ********************************************************/
void print_tree(struct node *top)
{
    if (top == NULL)
        return;                 /* short tree */

    print_tree(top->left);
    printf("%s\n", top->word);
    print_tree(top->right);
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "Error:Wrong number of parameters\n");
        fprintf(stderr, "      on the command line\n");
        fprintf(stderr, "Usage is:\n");
        fprintf(stderr, "    words 'file'\n");
        exit(8);
    }
    scan(argv[1]);
    print_tree(root);
    return (0);
}
