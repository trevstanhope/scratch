#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

area.exe: area.c
	$(CC) $(CFLAGS) -earea.exe area.c

clean:
	del area.exe 
