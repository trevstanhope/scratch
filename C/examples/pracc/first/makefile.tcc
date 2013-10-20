#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

first.exe: first.c
	$(CC) $(CFLAGS) -efirst.exe first.c

clean:
	del first.exe 
