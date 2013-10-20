#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

full2.exe: full2.c
	$(CC) $(CFLAGS) -efull2.exe full2.c

clean:
	del full2.exe 
