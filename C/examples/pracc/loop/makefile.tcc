#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

loop.exe: loop.c
	$(CC) $(CFLAGS) -eloop.exe loop.c

clean:
	del loop.exe 
