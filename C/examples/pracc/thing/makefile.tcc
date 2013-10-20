#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

thing.exe: thing.c
	$(CC) $(CFLAGS) -ething.exe thing.c

clean:
	del thing.exe 
