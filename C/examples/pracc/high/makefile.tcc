#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

high.exe: high.c
	$(CC) $(CFLAGS) -ehigh.exe high.c

clean:
	del high.exe 
