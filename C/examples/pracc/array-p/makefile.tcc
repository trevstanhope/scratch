#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

array-p.exe: array-p.c
	$(CC) $(CFLAGS) -earray-p.exe array-p.c

clean:
	del array-p.exe 
