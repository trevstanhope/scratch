#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

term.exe: term.c
	$(CC) $(CFLAGS) -eterm.exe term.c

clean:
	del term.exe 
