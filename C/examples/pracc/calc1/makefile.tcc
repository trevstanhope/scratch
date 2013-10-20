#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

calc1.exe: calc1.c
	$(CC) $(CFLAGS) -ecalc1.exe calc1.c

clean:
	del calc1.exe 
