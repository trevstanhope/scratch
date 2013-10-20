#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

split.exe: split.c
	$(CC) $(CFLAGS) -esplit.exe split.c

clean:
	del split.exe 
