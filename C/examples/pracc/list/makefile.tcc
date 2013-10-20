#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

list.exe: list.c
	$(CC) $(CFLAGS) -elist.exe list.c

clean:
	del list.exe 
