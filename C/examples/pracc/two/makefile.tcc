#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

two.exe: two.c
	$(CC) $(CFLAGS) -etwo.exe two.c

clean:
	del two.exe 
