#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

die.exe: die.c
	$(CC) $(CFLAGS) -edie.exe die.c

clean:
	del die.exe 
