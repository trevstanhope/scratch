#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

len2.exe: len2.c
	$(CC) $(CFLAGS) -elen2.exe len2.c

clean:
	del len2.exe 
