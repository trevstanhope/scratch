#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

call.exe: call.c
	$(CC) $(CFLAGS) -ecall.exe call.c

clean:
	del call.exe 
