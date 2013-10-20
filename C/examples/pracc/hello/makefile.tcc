#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

hello.exe: hello.c
	$(CC) $(CFLAGS) -ehello.exe hello.c

clean:
	del hello.exe 
