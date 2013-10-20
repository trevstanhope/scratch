#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

not2.exe: not2.c
	$(CC) $(CFLAGS) -enot2.exe not2.c

clean:
	del not2.exe 
