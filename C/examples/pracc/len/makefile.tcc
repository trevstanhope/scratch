#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

len.exe: len.c
	$(CC) $(CFLAGS) -elen.exe len.c

clean:
	del len.exe 
