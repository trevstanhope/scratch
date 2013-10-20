#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

scat.exe: scat.c
	@echo "This program will generate an error"
	$(CC) $(CFLAGS) -escat.exe scat.c

clean:
	del scat.exe 
