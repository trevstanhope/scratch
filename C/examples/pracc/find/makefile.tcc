#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

find.exe: find.c
	$(CC) $(CFLAGS) -c -efind.exe find.c

clean:
	del find.exe 
