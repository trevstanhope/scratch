#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

def.exe: def.c
	$(CC) $(CFLAGS) -edef.exe def.c

clean:
	del def.exe 
