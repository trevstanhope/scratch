#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

twice.exe: twice.c
	$(CC) $(CFLAGS) -etwice.exe twice.c

clean:
	del twice.exe 
