#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

sine.exe: sine.c
	$(CC) $(CFLAGS) -esine.exe sine.c

clean:
	del sine.exe 
