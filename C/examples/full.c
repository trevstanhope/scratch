/*
full.c
concatenates two string arrays
*/
/* Includes */
#include <string.h>
#include <stdio.h>

/* Definitions */
char first[100];
char last[100];
char full_name[200];

int main() {
  strcopy(first, "steve");
  strcopy(last, "smith");
  strcopy(full_name, first);
  strcat(full_name, " ");
  strcat(full_name, last);
  printf("The full name is %s\n", full_name);
  return(0);
}
