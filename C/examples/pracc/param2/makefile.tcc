#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

param2.exe: param2.c
	$(CC) $(CFLAGS) -eparam2.exe param2.c

clean:
	del param2.exe 
