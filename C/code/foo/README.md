# Shared Library
## Compile
The following commands will create a c-file, foo.c
along with an header, foo.h and then will compile an xecutable 
from main.c, which is in this case just called test.
	$ DIR=pwd  
	$ gcc -c -Wall -Werror -fpic foo.c  
	$ gcc -shared -o libfoo.so foo.o  
	$ gcc -Wall -o test main.c -lfoo  
	$ gcc -L$CURRENT -Wall -o test main.c -lfoo  
	$ LD_LIBRARY_PATH=$DIR:$LD_LIBRARY_PATH  
	$ export LD_LIBRARY_PATH=$DIR:$LD_LIBRARY_PATH
	
## If you want to use the rpath option instead
	$ unset LD_LIBRARY_PATH
	$ gcc -L/$DIR -Wl,-rpath=$DIR -Wall -o test main.c -lfoo
