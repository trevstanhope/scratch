#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

seven.exe: seven.c
	$(CC) $(CFLAGS) -eseven.exe seven.c

clean:
	del seven.exe 
