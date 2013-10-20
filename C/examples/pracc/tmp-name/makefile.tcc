#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

tmp-name.exe: tmp-name.c
	$(CC) $(CFLAGS) -etmp-name.exe tmp-name.c

clean:
	del tmp-name.exe 
