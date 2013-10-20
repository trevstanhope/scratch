#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

full.exe: full.c
	$(CC) $(CFLAGS) -efull.exe full.c

clean:
	del full.exe 
