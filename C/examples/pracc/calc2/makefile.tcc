#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

calc2.exe: calc2.c
	$(CC) $(CFLAGS) -ecalc2.exe calc2.c

clean:
	del calc2.exe 
