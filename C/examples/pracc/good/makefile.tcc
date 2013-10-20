#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

good.exe: good.c
	$(CC) $(CFLAGS) -egood.exe good.c

clean:
	del good.exe 
