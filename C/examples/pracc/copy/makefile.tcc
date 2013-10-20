#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

copy.exe: copy.c
	$(CC) $(CFLAGS) -ecopy.exe copy.c

clean:
	del copy.exe 
