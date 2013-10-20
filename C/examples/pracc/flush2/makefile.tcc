#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

flush2.exe: flush2.c
	$(CC) $(CFLAGS) -eflush2.exe flush2.c

clean:
	del flush2.exe 
