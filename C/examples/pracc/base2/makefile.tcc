#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

base2.exe: base2.c
	$(CC) $(CFLAGS) -c -ebase2.exe base2.c

clean:
	del base2.exe 
