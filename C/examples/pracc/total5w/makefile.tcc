#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

total5w.exe: total5w.c
	$(CC) $(CFLAGS) -etotal5w.exe total5w.c

clean:
	del total5w.exe 
