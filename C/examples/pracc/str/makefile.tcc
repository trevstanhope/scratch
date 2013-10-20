#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

str.exe: str.c
	$(CC) $(CFLAGS) -estr.exe str.c

clean:
	del str.exe 
