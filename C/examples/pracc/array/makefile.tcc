#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

array.exe: array.c
	$(CC) $(CFLAGS) -earray.exe array.c

clean:
	del array.exe 
