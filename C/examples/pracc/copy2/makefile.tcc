#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

copy2.exe: copy2.c
	@echo "This program generates warnings"
	$(CC) $(CFLAGS) -ecopy2.exe copy2.c

clean:
	del copy2.exe 
