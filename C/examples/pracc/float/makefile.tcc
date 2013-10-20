#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

float.exe: float.c
	$(CC) $(CFLAGS) -efloat.exe float.c

clean:
	del float.exe 
