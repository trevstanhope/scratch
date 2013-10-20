#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

ptr2.exe: ptr2.c
	$(CC) $(CFLAGS) -eptr2.exe ptr2.c

clean:
	del ptr2.exe 
