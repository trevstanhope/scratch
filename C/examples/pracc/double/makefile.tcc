#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

double.exe: double.c
	$(CC) $(CFLAGS) -edouble.exe double.c

clean:
	del double.exe 
