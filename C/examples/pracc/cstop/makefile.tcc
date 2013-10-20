#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

cstop.exe: cstop.c
	$(CC) $(CFLAGS) -c -ecstop.exe cstop.c

clean:
	del cstop.exe 
