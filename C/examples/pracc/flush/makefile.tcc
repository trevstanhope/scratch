#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

flush.exe: flush.c
	$(CC) $(CFLAGS) -eflush.exe flush.c

clean:
	del flush.exe 
