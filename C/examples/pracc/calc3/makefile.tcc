#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

calc3.exe: calc3.c
	$(CC) $(CFLAGS) -ecalc3.exe calc3.c

clean:
	del calc3.exe 
