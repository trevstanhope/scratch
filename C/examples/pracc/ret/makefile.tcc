
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

ret.exe: ret.c 
	@echo "The compile is smart enough to catch the error in this file"
	$(CC) $(CFLAGS) -eret.exe ret.c 

clean:
	del ret.exe 
