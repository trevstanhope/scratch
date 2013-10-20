#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

total.exe: total.c
	$(CC) $(CFLAGS) -etotal.exe total.c

clean:
	del total.exe 
