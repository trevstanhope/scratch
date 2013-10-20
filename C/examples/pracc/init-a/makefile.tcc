#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

init-a.exe: init-a.c
	@echo "This program will generate a warning"
	$(CC) $(CFLAGS) -einit-a.exe init-a.c

clean:
	del init-a.exe 
