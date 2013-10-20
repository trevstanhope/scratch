#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

base.exe: base.c
	$(CC) $(CFLAGS) -ebase.exe base.c

clean:
	del base.exe 
