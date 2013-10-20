#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

base3.exe: base3.c
	$(CC) $(CFLAGS) -ebase3.exe base3.c

clean:
	del base3.exe 
