#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

fib.exe: fib.c
	$(CC) $(CFLAGS) -efib.exe fib.c

clean:
	del fib.exe 
