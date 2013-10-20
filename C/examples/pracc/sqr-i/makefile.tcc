#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

sqr-i.exe: sqr-i.c
	$(CC) $(CFLAGS) -esqr-i.exe sqr-i.c

clean:
	del sqr-i.exe 
