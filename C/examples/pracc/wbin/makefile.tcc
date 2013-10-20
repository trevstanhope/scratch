#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

wbin.exe: wbin.c
	$(CC) $(CFLAGS) -ewbin.exe wbin.c

clean:
	del wbin.exe 
