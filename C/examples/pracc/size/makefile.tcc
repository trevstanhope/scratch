#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

size.exe: size.c
	$(CC) $(CFLAGS) -esize.exe size.c

clean:
	del size.exe 
