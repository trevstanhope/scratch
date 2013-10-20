#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

hello2.exe: hello2.c
	$(CC) $(CFLAGS) -ehello2.exe hello2.c

clean:
	del hello2.exe 
