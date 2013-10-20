#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

tmp2.exe: tmp2.c
	$(CC) $(CFLAGS) -etmp2.exe tmp2.c

clean:
	del tmp2.exe 
