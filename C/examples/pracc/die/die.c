#include <stdio.h>
#include <stdlib.h>	

#define DIE \
  fprintf(stderr, "Fatal Error:Abort\n");exit(8); 

int main() {     
    /* a random value for testing */
    int value;  
    
    value = 1; 
    if (value < 0) 
        DIE; 

    printf("We did not die\n");
    return (0);
} 
