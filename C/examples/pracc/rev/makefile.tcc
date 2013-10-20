#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

rev.exe: rev.c
	$(CC) $(CFLAGS) -erev.exe rev.c

clean:
	del rev.exe 
