#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

totalb.exe: totalb.c
	$(CC) $(CFLAGS) -etotalb.exe totalb.c

clean:
	del totalb.exe 
