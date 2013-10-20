#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

div.exe: div.c
	$(CC) $(CFLAGS) -ediv.exe div.c

clean:
	del div.exe 
