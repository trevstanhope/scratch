#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

init2b.exe: init2b.c
	$(CC) $(CFLAGS) -einit2b.exe init2b.c

clean:
	del init2b.exe 
