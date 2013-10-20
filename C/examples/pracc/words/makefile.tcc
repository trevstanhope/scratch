#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

words.exe: words.c
	$(CC) $(CFLAGS) -ewords.exe words.c

clean:
	del words.exe 
