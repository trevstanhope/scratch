#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

ptr3.exe: ptr3.c
	$(CC) $(CFLAGS) -eptr3.exe ptr3.c

clean:
	del ptr3.exe 
