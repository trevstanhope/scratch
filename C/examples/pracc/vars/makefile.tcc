#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

vars.exe: vars.c
	$(CC) $(CFLAGS) -evars.exe vars.c

clean:
	del vars.exe 
