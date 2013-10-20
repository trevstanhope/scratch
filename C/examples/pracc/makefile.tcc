#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

PROG.exe: PROG.c
	$(CC) $(CFLAGS) -ePROG.exe PROG.c

clean:
	del PROG.exe 
