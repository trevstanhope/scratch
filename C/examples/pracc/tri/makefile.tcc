#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

tri.exe: tri.c
	@echo "This program will fail to compile"
	$(CC) $(CFLAGS) -etri.exe tri.c

clean:
	del tri.exe 
