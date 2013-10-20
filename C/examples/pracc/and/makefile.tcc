#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

and.exe: and.c
	$(CC) $(CFLAGS) -eand.exe and.c

clean:
	del and.exe 
