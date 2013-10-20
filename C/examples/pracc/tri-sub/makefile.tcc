#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

tri-prog.exe: tri-prog.c 
	$(CC) $(CFLAGS) -etri-prog tri-prog.c

clean:
	del tri-prog.exe
