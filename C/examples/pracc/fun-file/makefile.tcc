#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

fun-file.exe: fun-file.c
	$(CC) $(CFLAGS) -efun-file.exe fun-file.c

clean:
	del fun-file.exe 
