#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

cent.exe: cent.c
	$(CC) $(CFLAGS) -ecent.exe cent.c

clean:
	del cent.exe 
