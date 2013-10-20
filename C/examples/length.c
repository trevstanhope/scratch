/*
length.c
gets string and returns length
*/

/* Includes */
#include <string.h>
#include <stdio.h>

/* Declarations */
char line[100];  /* Line we are looking at */

int main() {
  printf("enter a string:");
  fgets(line, sizeof(line), stdin);
  printf("the string length is: %d", strlen(line)); /* strlen(l) */
  return 0;
}
