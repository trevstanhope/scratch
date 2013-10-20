#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

sqr.exe: sqr.c
	$(CC) $(CFLAGS) -esqr.exe sqr.c

clean:
	del sqr.exe 
