#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

owe0.exe: owe0.c
	$(CC) $(CFLAGS) -eowe0.exe owe0.c

clean:
	del owe0.exe 
