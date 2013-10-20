#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

simple.exe: simple.c
	$(CC) $(CFLAGS) -esimple.exe simple.c

clean:
	del simple.exe 
