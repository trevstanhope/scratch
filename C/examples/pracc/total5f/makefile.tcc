#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

total5f.exe: total5f.c
	$(CC) $(CFLAGS) -etotal5f.exe total5f.c

clean:
	del total5f.exe 
