#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

bad.exe: bad.c
	$(CC) $(CFLAGS) -ebad.exe bad.c

clean:
	del bad.exe 
