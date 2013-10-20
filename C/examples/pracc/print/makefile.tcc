#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

print.exe: print.c
	$(CC) $(CFLAGS) -eprint.exe print.c

clean:
	del print.exe 
