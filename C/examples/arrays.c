/*
arrays.c
 */
#include <stdio.h>
int array[3]; /* creates a 3 element array from array[0] to array[2] */
int i; /* counter */
int j; /* another counter */
int main() {
  array[0] = 1;
  array[1] = 2;
  array[2] = 3;
  i = 0;
  j = 10;
  while (i<j) {
    i = (i + j);
    j = (j / i) + j;
    printf("i %d j %d\n", i, j);
  }
}
