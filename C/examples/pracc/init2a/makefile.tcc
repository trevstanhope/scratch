#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

init2a.exe: init2a.c
	$(CC) $(CFLAGS) -einit2a.exe init2a.c

clean:
	del init2a.exe 
