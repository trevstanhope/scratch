#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

full1.exe: full1.c
	$(CC) $(CFLAGS) -efull1.exe full1.c

clean:
	del full1.exe 
