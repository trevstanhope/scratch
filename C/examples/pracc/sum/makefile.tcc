#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

sum.exe: sum.c
	@echo "This program fails to compile"
	$(CC) $(CFLAGS) -esum.exe sum.c

clean:
	del sum.exe 
