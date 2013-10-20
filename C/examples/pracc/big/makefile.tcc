#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

big.exe: big.c
	$(CC) $(CFLAGS) -ebig.exe big.c

clean:
	del big.exe 
